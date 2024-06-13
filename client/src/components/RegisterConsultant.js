
import React, { useState } from 'react';
import axios from 'axios';

const RegisterConsultant = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [qualification, setQualification] = useState('');
  const [certificateUrl, setCertificateUrl] = useState('');

  const handleRegisterConsultant = async () => {
    try {
      const response = await axios.post('http://localhost:5000/consultant/register', {
        username,
        email,
        password,
        qualification,
        certificateUrl
      });
      console.log(response.data);
      // Handle registration success (e.g., show a message)
    } catch (error) {
      console.error('Error registering consultant:', error);
    }
  };

  return (
    <div>
      <h2>Register Consultant</h2>
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
      <input
        type="text"
        placeholder="Qualification"
        value={qualification}
        onChange={(e) => setQualification(e.target.value)}
      />
      <input
        type="text"
        placeholder="Certificate URL"
        value={certificateUrl}
        onChange={(e) => setCertificateUrl(e.target.value)}
      />
      <button onClick={handleRegisterConsultant}>Register</button>
    </div>
  );
};

export default RegisterConsultant;