
import React, { useContext, useState, useEffect } from 'react';
import axios from 'axios';
import AuthProvider, { AuthContext } from './components/AuthProvider';
import Login from './components/Login';
import RegisterClient from './components/RegisterClient';
import RegisterConsultant from './components/RegisterConsultant';
import UserList from './components/UserList';
import ConsultantList from './components/ConsultantList';
import ProjectList from './components/ProjectList';
import PostList from './components/PostList';

const App = () => {
  const { accessToken, setAccessToken, isLoggedIn, setIsLoggedIn, currentUser, setCurrentUser } = useContext(AuthContext);
  const [users, setUsers] = useState([]);
  const [consultants, setConsultants] = useState([]);
  const [projects, setProjects] = useState([]);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    if (isLoggedIn) {
      fetchUserData();
    }
  }, [isLoggedIn]);

  const fetchUserData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/users', {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      });
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  const fetchConsultants = async () => {
    try {
      const response = await axios.get('http://localhost:5000/consultants');
      setConsultants(response.data);
    } catch (error) {
      console.error('Error fetching consultants:', error);
    }
  };

  const fetchProjects = async () => {
    try {
      const response = await axios.get('http://localhost:5000/projects');
      setProjects(response.data);
    } catch (error) {
      console.error('Error fetching projects:', error);
    }
  };

  const fetchPosts = async (consultantId) => {
    try {
      const response = await axios.get(`http://localhost:5000/consultants/${consultantId}/posts`, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      });
      setPosts(response.data);
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  const handleLogout = () => {
    setAccessToken(null);
    localStorage.removeItem('accessToken');
    setIsLoggedIn(false);
    setCurrentUser(null);
  };

  return (
    <AuthProvider>
      <div className="App">
        {!isLoggedIn ? (
          <>
            <Login setAccessToken={setAccessToken} setIsLoggedIn={setIsLoggedIn} fetchUserData={fetchUserData} />
            <RegisterClient />
            <RegisterConsultant />
          </>
        ) : (
          <>
            <button onClick={handleLogout}>Logout</button>
            <UserList users={users} fetchUserData={fetchUserData} isLoggedIn={isLoggedIn} />
            <ConsultantList consultants={consultants} fetchConsultants={fetchConsultants} />
            <ProjectList projects={projects} fetchProjects={fetchProjects} />
            <PostList consultantId={currentUser?.id} posts={posts} fetchPosts={fetchPosts} />
          </>
        )}
      </div>
    </AuthProvider>
  );
};

export default App;