// ConsultantProfile.js
import React from 'react';
import { Link } from 'react-router-dom';

const ConsultantProfile = ({ consultant }) => {
  return (
    <div className="consultant-profile">
      <div className="profile-header">
        <img src={consultant.photo} alt={consultant.name} className="profile-photo" />
        <div className="profile-info">
          <h2>{consultant.name}</h2>
          <p>{consultant.bio}</p>
          <p>Location: {consultant.location}</p>
          <p>Services: {consultant.services.join(', ')}</p>
          <div className="social-links">
            <a href={consultant.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href={consultant.twitter} target="_blank" rel="noopener noreferrer">Twitter</a>
            {/* Add more social links as needed */}
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
        <Link to={`/consultants/${consultant.id}`} className="btn">View Profile</Link>
      </div>
    </div>
  );
};

export default ConsultantProfile;
