
import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext(null);

const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const storedToken = localStorage.getItem('accessToken');
    if (storedToken) {
      setAccessToken(storedToken);
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <AuthContext.Provider
      value={{ accessToken, setAccessToken, isLoggedIn, setIsLoggedIn, currentUser, setCurrentUser }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;