
import React, { useState } from 'react';
import axios from 'axios';

const RegisterClient = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegisterClient = async () => {
    try {
      const response = await axios.post('http://localhost:5000/register/client', {
        username,
        email,
        password
      });
      console.log(response.data);
    } catch (error) {
      console.error('Error registering client:', error);
    }
  };

  return (
    <div>
      <h2>Register Client</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegisterClient}>Register</button>
    </div>
  );
};

export default RegisterClient;