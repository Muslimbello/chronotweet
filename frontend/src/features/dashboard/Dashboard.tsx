import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [user, setUser] = useState<{ username: string; twitter_id: string } | null>(null);

  useEffect(() => {
    // Fetch user data from Django
    const fetchUser = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/user/');
        setUser(response.data);
      } catch (error) {
        console.error('Failed to fetch user data:', error);
      }
    };

    fetchUser();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome, {user.username}!</h1>
      <p>Twitter ID: {user.twitter_id}</p>
    </div>
  );
};

export default Dashboard;