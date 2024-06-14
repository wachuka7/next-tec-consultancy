import React from 'react';
import './Home.css';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="home-container">
      <div className="header">
        <h1>Welcome to Consultancy Hub</h1>
        <p className="sub-header">Connecting Clients with Expert Consultants</p>
      </div>

      <section className="section">
        <h2>For Clients</h2>
        <p>
          At Consultancy Hub, we specialize in connecting clients with expert consultants across a wide range of fields. Whether you're looking for guidance in web development, hosting solutions, data analysis, business strategy, investment advice, or any other specialized area, we're here to help you find the right expertise.
        </p>
        <>
          <li>
            <strong>Find Expert Consultants:</strong> Browse our extensive database of consultants who are ready to assist you with their specialized knowledge and skills. Search by industry, expertise, or specific service to find the perfect match for your consultancy needs.
          </li>
          <li>
            <strong>Explore Services:</strong> Discover detailed profiles of consultants showcasing their services, past projects, and client testimonials. Easily compare consultants to make informed decisions.
          </li>
          <li>
            <strong>Post Your Requirements:</strong> Post your consultancy requirements and let consultants bid on your project. Receive proposals tailored to your needs and choose the consultant who best meets your criteria.
          </li>
          <li>
            <strong>Stay Informed:</strong> Access industry insights, trends, and articles authored by our consultants to stay informed about the latest developments in your field of interest.
          </li>
        </>
      </section>

      <section className="section">
        <h2>For Consultants</h2>
        <p>
          Whether you are an experienced consultant or just starting out, Consultancy Hub provides you with the platform to showcase your expertise and connect with clients seeking your consultancy services.
        </p>
        <>
          <li>
            <strong>Showcase Your Expertise:</strong> Create a professional profile highlighting your expertise, experience, and services offered. Showcase your portfolio, case studies, and client success stories to demonstrate your capabilities.
          </li>
          <li>
            <strong>Connect with Clients:</strong> Engage with potential clients who are actively seeking your consultancy services. Respond to inquiries, submit proposals, and build long-lasting client relationships.
          </li>
          <li>
            <strong>Expand Your Reach:</strong> Gain visibility in your industry by publishing insightful articles and blog posts on topics related to your expertise. Position yourself as a thought leader and attract new clients.
          </li>
          <li>
            <strong>Collaborate and Network:</strong> Connect with fellow consultants, collaborate on projects, and share knowledge within our community of experts.
          </li>
        </>
      </section>

      {/* How It Works Section */}
      <section className="section">
        <h2>How It Works</h2>
        <ul>
          <li><strong>Search and Connect:</strong> Clients can easily search for consultants by industry, expertise, or location. Consultants can network with clients seeking their specific skills.</li>
          <li><strong>Post and Bid:</strong> Clients post their consultancy needs, and consultants bid on projects that match their expertise and interests.</li>
          <li><strong>Engage and Deliver:</strong> Consultants engage with clients, provide tailored solutions, and deliver value through their consultancy services.</li>
        </ul>
      </section>

      {/* Call to Action Section */}
      <section className="cta">
        <h2>Start Your Consultancy Journey Today</h2>
        <p>Whether you're a client seeking expert advice or a consultant looking to showcase your skills, Consultancy Hub is your platform to connect, collaborate, and succeed. Join our community today and experience the power of expert consultancy at your fingertips.</p>
        <Link to="/register/client" className="btn">Sign Up Now</Link>
        <p>and unlock a world of consultancy opportunities!</p>
      </section>

    </div>
  );
};

export default Home;
