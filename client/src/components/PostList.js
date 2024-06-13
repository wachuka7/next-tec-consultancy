
import React, { useEffect } from 'react';

const PostList = ({ consultantId, posts, fetchPosts }) => {
  useEffect(() => {
    if (consultantId) {
      fetchPosts(consultantId);
    }
  }, [consultantId, fetchPosts]);

  return (
    <div>
      <h2>Posts</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default PostList;