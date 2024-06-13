// ConsultantDirectory.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const ConsultantDirectory = () => {
  const [consultants, setConsultants] = useState([]);

  useEffect(() => {
    fetchConsultants();
  }, []);

  const fetchConsultants = async () => {
    try {
      const response = await axios.get('http://localhost:5000/consultants');
      setConsultants(response.data);
    } catch (error) {
      console.error('Error fetching consultants:', error);
    }
  };

  return (
    <div className="consultant-directory">
      <h2>Find Expert Consultants</h2>
      {consultants.map((consultant) => (
        <div key={consultant.id}>
          <h3>{consultant.name}</h3>
          <p>{consultant.bio}</p>
          <Link to={`/consultants/${consultant.id}`}>View Profile</Link>
        </div>
      ))}
    </div>
  );
};

export default ConsultantDirectory;
