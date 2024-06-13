
import React, { useState } from 'react';
import axios from 'axios';

const RegisterConsultant = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    qualification: '',
    certificate_url: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/register/consultant', formData, {
        headers: {
          'Content-Type': 'application/json'
        },
      });
      console.log('Consultant registered:', response.data);
    } catch (error) {
      console.error('Error registering consultant:', error.response.data);
    }
  };

  return (
    <div>
      <h2>Register as Consultant</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="username" placeholder="Username" onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} />
        <input type="text" name="qualification" placeholder="Qualification" onChange={handleChange} />
        <input type="text" name="certificate_url" placeholder="Certificate URL" onChange={handleChange} />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegisterConsultant;