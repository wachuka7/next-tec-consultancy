
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ConsultantProfile = () => {
  const { id } = useParams();
  const [consultant, setConsultant] = useState(null);
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const fetchConsultant = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/consultants/${id}`);
        setConsultant(response.data);
      } catch (error) {
        console.error('Error fetching consultant:', error);
      }
    };

    fetchConsultant(); 
  }, [id]); 

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/projects?consultant_id=${id}`);
        setProjects(response.data);
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    };

    fetchProjects();
  }, [id]);

  if (!consultant) {
    return <div>Loading...</div>; 
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
          {projects.map(project => (
            <li key={project.id}>
              <h4>{project.name}</h4>
              <p>{project.description}</p>
            </li>
          ))}
        </ul>
        <h3>Client Testimonials:</h3>
        <p>{consultant.testimonials.join(', ')}</p>
      </div>
    </div>
  );
};

export default ConsultantProfile;
