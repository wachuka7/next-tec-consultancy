import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ConsultantPost = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
  
    useEffect(() => {
      const fetchPost = async () => {
        try {
          const response = await axios.get(`http://localhost:5000/posts/${id}`);
          setPost(response.data);
        } catch (error) {
          console.error('Error fetching post:', error);
        }
      };
  
      fetchPost();
    }, [id]);
  
    if (!post) {
      return <p>Loading...</p>;
    }
    
  return (
    <div className="consultant-post">
      <div className="post-header">
        <img src={post.author.photo} alt={post.author.name} className="author-photo" />
        <div className="author-info">
          <h3>{post.author.name}</h3>
          <p>{post.author.title}</p>
        </div>
      </div>
      <div className="post-content">
        <h2>{post.title}</h2>
        <p>{post.content}</p>
      </div>
      <div className="post-actions">
        <button>Like</button>
        <button>Comment</button>
        <button>Share</button>
      </div>
    </div>
  );
};

export default ConsultantPost;
