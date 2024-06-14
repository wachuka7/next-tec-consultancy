
// import React, { useContext, useState, useEffect } from 'react';
// import axios from 'axios';
// import AuthProvider, { AuthContext } from './components/AuthProvider';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './components/Home';
import About from './components/About';
import Services from './components/Services';
// import Login from './components/Login';
import RegisterClient from './components/RegisterClient';
import RegisterConsultant from './components/RegisterConsultant';
import ConsultantProfile from './components/ConsultantProfile'; 
import ConsultantPost from './components/ConsultantPost';
import ConsultantPostFeed from './components/ConsultantPostFeed';
import ConsultantDirectory from './components/ConsultantDirectory';

import './App.css';

const App = () => {
  // const { accessToken, setAccessToken, isLoggedIn, setIsLoggedIn, currentUser, setCurrentUser } = useContext(AuthContext);
  // const [users, setUsers] = useState([]);
  // const [consultants, setConsultants] = useState([]);
  // const [projects, setProjects] = useState([]);
  // const [posts, setPosts] = useState([]);


  // useEffect(() => {
  //   if (isLoggedIn) {
  //     fetchUserData();
  //   }
  // }, [isLoggedIn]);

  // const fetchUserData = async () => {
  //   try {
  //     const response = await axios.get('http://localhost:5000/users', {
  //       headers: {
  //         Authorization: `Bearer ${accessToken}`
  //       }
  //     });
  //     setUsers(response.data);
  //   } catch (error) {
  //     console.error('Error fetching user data:', error);
  //   }
  // };

  // const fetchConsultants = async () => {
  //   try {
  //     const response = await axios.get('http://localhost:5000/consultants', {
  //       headers: {
  //         Authorization: `Bearer ${accessToken}`
  //       }
  //     });
  //     setConsultants(response.data);
  //   } catch (error) {
  //     console.error('Error fetching consultants:', error);
  //   }
  // };

  // const fetchProjects = async () => {
  //   try {
  //     const response = await axios.get('http://localhost:5000/projects', {
  //       headers: {
  //         Authorization: `Bearer ${accessToken}`
  //       }
  //     });
  //     setProjects(response.data);
  //   } catch (error) {
  //     console.error('Error fetching projects:', error);
  //   }
  // };


  // const handleLogout = () => {
  //   setAccessToken(null);
  //   localStorage.removeItem('accessToken');
  //   setIsLoggedIn(false);
  //   setCurrentUser(null);
  // };

  return (
    // <AuthProvider>
      <BrowserRouter>
        <div className="App">
          <NavBar  />
          {/* isLoggedIn={isLoggedIn} handleLogout={handleLogout} */}
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/services" element={<Services />} />
            {/* <Route path="/login" element={<Login setAccessToken={setAccessToken} setIsLoggedIn={setIsLoggedIn} fetchUserData={fetchUserData} />} /> */}
            <Route path="/consultants/:id" component={ConsultantProfile} />
            <Route path="/posts/:id" component={ConsultantPost} />
            <Route path="/posts" element={<ConsultantPostFeed />} />
            <Route path="/consultants" element={<ConsultantDirectory />} />
            <Route path="/consultants/:id" element={<ConsultantProfile />} />
            <Route path="/register/consultant" component={RegisterConsultant} />
            <Route path="/register/client" component={RegisterClient} />
            {/* {!isLoggedIn && (
              <>
                <Route path="/register/client" element={<RegisterClient />} />
                <Route path="/register/consultant" element={<RegisterConsultant />} />
              </>
            )}
            {isLoggedIn && (
              <> */}

          </Routes>
        </div>
      </BrowserRouter>
    // </AuthProvider>
  );
};

export default App;