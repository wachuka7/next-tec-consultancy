// NavBar.js
import React, { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from './AuthProvider';
import './NavBar.css';


const NavBar = () => {
  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);
  const [showDropdown, setShowDropdown] = useState(false);

  const handleLogout = () => {
    setIsLoggedIn(false);
    localStorage.removeItem('accessToken');
  };

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
        <li>
          <Link to="/services">Services</Link>
        </li>
        <li>
          <Link to="/consultants">Consultants</Link>
        </li>
        <li>
          <Link to="/posts">Posts</Link>
        </li>
        {!isLoggedIn ? (
          <>
            <li style={{ float: 'right' }}>
              <Link to="/login">Login</Link>
            </li>
            <li style={{ float: 'right', position: 'relative' }}>
              <button
                onClick={toggleDropdown}
                style={{
                  background: 'none',
                  border: 'none',
                  cursor: 'pointer',
                  color: 'blue',
                  textDecoration: 'underline',
                }}
              >
                Register
              </button>
              {showDropdown && (
                <ul
                  style={{
                    position: 'absolute',
                    top: '100%',
                    right: '0',
                    background: 'white',
                    border: '1px solid #ccc',
                    padding: '10px',
                    listStyleType: 'none',
                  }}
                >
                  <li>
                    <Link to="/register/user" onClick={() => setShowDropdown(false)}>
                      Sign up as User
                    </Link>
                  </li>
                  <li>
                    <Link to="/register/consultant" onClick={() => setShowDropdown(false)}>
                      Sign up as Consultant
                    </Link>
                  </li>
                </ul>
              )}
            </li>
          </>
        ) : (
          <li style={{ float: 'right' }}>
            <button onClick={handleLogout}>Logout</button>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default NavBar;
