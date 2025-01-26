import logging
from celery import shared_task
from django.utils import timezone
from .models import ScheduledTweet
from ..services.twitter_api import TwitterAPIClient  # Your X API client

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 30},
)
def post_tweet_task(self, tweet_id):
    """
    Task to post individual tweet with retry logic
    """
    try:
        tweet = ScheduledTweet.objects.get(id=tweet_id, is_posted=False)
        client = TwitterAPIClient(tweet.user.access_token)

        # Post to X API
        response = client.post_tweet(tweet.content)

        # Update DB
        tweet.is_posted = True
        tweet.posted_at = timezone.now()
        tweet.tweet_id = response["data"]["id"]
        tweet.save()

    except ScheduledTweet.DoesNotExist:
        logger.error(f"Tweet {tweet_id} not found or already posted")
    except Exception as e:
        logger.error(f"Failed to post tweet {tweet_id}: {str(e)}")
        raise self.retry(exc=e)


@shared_task
def safety_net_check():
    """
    Periodic task to catch missed tweets
    """
    try:
        pending = ScheduledTweet.objects.filter(
            scheduled_at__lte=timezone.now(), is_posted=False
        )

        for tweet in pending:
            post_tweet_task.apply_async(
                args=[tweet.id], eta=tweet.scheduled_at  # Original scheduled time
            )

    except Exception as e:
        logger.error(f"Safety net check failed: {str(e)}")
