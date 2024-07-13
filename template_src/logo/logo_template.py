from jinja2 import Template

# Define the logo component template
logo_template = Template('''
import React from "react";
import "./Header.css"; // Import your CSS file for logo styles

interface LogoProps {
  logoText?: string;
  logoImageUrl?: string;
  height?: number;
  width?: number;
}

const Logo: React.FC<LogoProps> = ({
  logoText,
  logoImageUrl,
  height = 50,
  width = 200,
}) => {
  return (
    <div className="logo-container">
      {logoImageUrl ? (
        <img
          src={`${logoImageUrl}`}
          alt="Logo"
          className="logo-image"
        />
      ) : (
        <svg
          className="logo-svg"
          height={`${height}px`}
          width={`${width}px`}
          xmlns="http://www.w3.org/2000/svg"
        >
          <text
            x="10"
            y={height * 0.7}
            className="logo-text"
          >
            {logoText}
          </text>
        </svg>
      )}
    </div>
  );
};

export default Logo;
''')

