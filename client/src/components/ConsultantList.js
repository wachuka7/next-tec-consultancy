
import React, { useEffect } from 'react';

const ConsultantList = ({ consultants, fetchConsultants }) => {
  useEffect(() => {
    fetchConsultants();
  }, [fetchConsultants]);

  return (
    <div>
      <h2>Consultants</h2>
      <ul>
        {consultants.map(consultant => (
          <li key={consultant.id}>{consultant.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default ConsultantList;