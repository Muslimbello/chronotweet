import React from 'react';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Redirect to Django's OAuth initiation endpoint
    window.location.href = 'http://localhost:8000/auth/twitter/';
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Login with X</h1>
      <Button
        variant="contained"
        color="primary"
        onClick={handleLogin}
        startIcon={<span>🐦</span>}  // Replace with an X/Twitter icon if available
      >
        Login with X
      </Button>
    </div>
  );
};

export default Login;