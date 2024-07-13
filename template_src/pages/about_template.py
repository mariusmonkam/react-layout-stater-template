from jinja2 import Template

# Define the template for the About component
about_template = Template('''
import React from 'react';
import './About.css';

const About: React.FC = () => {
  return (
    <div className="About">
      <h1>About Us</h1>
      <p>This is the about page content.</p>
    </div>
  );
}

export default About;
''')

# Define the CSS template for the About component
about_css_template = Template('''
.About {
  text-align: center;
  margin-top: 50px;
}

.About h1 {
  color: #333;
}

.About p {
  font-size: 1.2em;
  color: #666;
}
''')
