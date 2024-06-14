// ConsultantProfile.js

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ConsultantProfile = () => {
  const { id } = useParams();
  const [consultant, setConsultant] = useState(null);

  useEffect(() => {
    const fetchConsultant = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/consultants/${id}`);
        setConsultant(response.data);
      } catch (error) {
        console.error('Error fetching consultant:', error);
      }
    };

    fetchConsultant(); // Initial fetch when id changes
  }, [id]); // Dependency array includes id

  if (!consultant) {
    return <div>Loading...</div>; // Add loading state
  }

  return (
    <div className="consultant-profile">
      <div className="profile-header">
        <img src={consultant.photo} alt={consultant.username} className="profile-photo" />
        <div className="profile-info">
          <h2>{consultant.username}</h2>
          <p>{consultant.bio}</p>
          <p>Location: {consultant.location}</p>
          <p>Services: {consultant.services.join(', ')}</p>
          <div className="social-links">
            <a href={consultant.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href={consultant.twitter} target="_blank" rel="noopener noreferrer">Twitter</a>
          </div>
        </div>
      </div>
      <div className="profile-details">
        <h3>About Me</h3>
        <p>{consultant.about}</p>
        <h3>Past Projects</h3>
        <ul>
          {consultant.projects.map((project, index) => (
            <li key={index}>{project}</li>
          ))}
        </ul>
        <h3>Client Testimonials</h3>
        <ul>
          {consultant.testimonials.map((testimonial, index) => (
            <li key={index}>{testimonial}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ConsultantProfile;
