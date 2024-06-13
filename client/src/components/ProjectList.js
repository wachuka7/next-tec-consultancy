
import React, { useEffect } from 'react';

const ProjectList = ({ projects, fetchProjects }) => {
  useEffect(() => {
    fetchProjects();
  }, [fetchProjects]);

  return (
    <div>
      <h2>Projects</h2>
      <ul>
        {projects.map(project => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectList;