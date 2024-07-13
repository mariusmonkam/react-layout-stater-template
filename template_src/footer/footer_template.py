from jinja2 import Template

# Define the Footer component template
footer_template = Template('''
import React from "react";
import "./Footer.css";

const Footer: React.FC<{ text: string }> = ({ text }) => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer-columns">
        <div className="footer-column">
          <h3>Column 1</h3>
          <p>Some content here</p>
        </div>
        <div className="footer-column">
          <h3>Column 2</h3>
          <p>Some content here</p>
        </div>
        <div className="footer-column">
          <h3>Column 3</h3>
          <p>Some content here</p>
        </div>
      </div>
      <div className="footer-copyright">
        <p>
          &copy; {currentYear}{" "}
          <a href="https://mardevpro.azurewebsites.net/" target="_blank" rel="noopener noreferrer">
            {text}
          </a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;



''')
