from jinja2 import Template

# Generate the Home component
home_template = Template('''
import React from "react";
import "./Home.css"; // Ensure this path is correct
import Counter from "../components/Counter";

const Home: React.FC = () => {
  const handleGetStartedClick = () => {
    window.location.href =
      "https://github.com/mariusmonkam/react-layout-stater-template";
  };

  return (
    <div className="home">
      <Counter />
      <div className="hero-section">
        <div className="hero-text">
          <div className="hero-title">
            {" "}
            Jumpstart Your React Projects with React Layout Starter Template
          </div>
          <div className="hero-subtitle">
            <div className="feature-columns">
              <div className="feature-column">
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Responsive Layout
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Pre-built Components
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Typescript Ready
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  State Management with Redux Toolkit
                </div>
              </div>
              <div className="feature-column">
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Navigation System with React Router DOM
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Menu Bar Ready
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  Logo Ready
                </div>
                <div className="feature-item">
                  <svg
                    className="check-icon"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="green"
                    width="24px"
                    height="24px"
                  >
                    <path d="M0 0h24v24H0z" fill="none" />
                    <path d="M9 16.17l-3.5-3.5L4 14.59l5 5 12-12-1.41-1.42z" />
                  </svg>
                  SVG Ready
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="hero-buttons">
          <div className="hero-button" onClick={handleGetStartedClick}>
            <div className="button-text">Get Started</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;



''')
