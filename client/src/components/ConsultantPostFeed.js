
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const ConsultantPostFeed = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const response = await axios.get('http://localhost:5000/posts');
      setPosts(response.data);
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  return (
    <div className="consultant-post-feed">
      <h2>Consultant Posts</h2>
      {posts.map((post) => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <h2>{post.category}</h2> 
          <h2 className="consultant-name">{post.consultant}</h2>
          <p>{post.content}</p>
          <Link to={`/posts/${post.id}`}>View More</Link>
        </div>
      ))}
    </div>
  );
};

export default ConsultantPostFeed;
