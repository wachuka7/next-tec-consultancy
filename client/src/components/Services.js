import React from 'react';
import './Services.css';

const Services = () => {
  return (
    <div className="services-container">
      <div className="services-content">
        <h2>Our Services</h2>
        <p>At Consultancy Hub, we offer a wide range of specialized services to meet your consultancy needs across various industries. Whether you're a client seeking expert guidance or a consultant looking to showcase your skills, we provide tailored solutions to drive your success.</p>
        
        <div className="service">
          <h3>Web Development</h3>
          <p>From frontend design to backend development and deployment, our web development consultants offer expertise in creating robust, scalable web solutions tailored to your business needs.</p>
        </div>

        <div className="service">
          <h3>Hosting Solutions</h3>
          <p>Explore reliable hosting solutions with our consultants. From cloud hosting to server management, we ensure seamless performance and security for your applications and websites.</p>
        </div>

        <div className="service">
          <h3>Data Analysis</h3>
          <p>Gain valuable insights from your data with our data analysis consultants. We offer expertise in data mining, statistical analysis, and visualization to drive informed decision-making and business strategies.</p>
        </div>

        <div className="service">
          <h3>Business Analysis</h3>
          <p>Optimize your business processes and strategies with our business analysis consultants. From market research to operational efficiency, we provide actionable insights to enhance your business performance.</p>
        </div>

        <div className="service">
          <h3>Investment Advisory</h3>
          <p>Receive expert guidance on investment opportunities and portfolio management from our consultants. Whether you're a novice investor or seasoned trader, we offer personalized advice to help you achieve your financial goals.</p>
        </div>
        
        {/* Add more services as needed */}
        
      </div>
    </div>
  );
};

export default Services;
