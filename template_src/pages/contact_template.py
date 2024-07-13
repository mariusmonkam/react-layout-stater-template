from jinja2 import Template

# Define the template for the Contact component
contact_template = Template('''
import React from 'react';
import './Contact.css';

const Contact: React.FC = () => {
  return (
    <div className="Contact">
      <h1>Contact Us</h1>
      <p>This is the Contact page content.</p>
    </div>
  );
}

export default Contact;
''')

# Define the CSS template for the Contact component
contact_css_template = Template('''
.Contact {
  text-align: center;
  margin-top: 50px;
}

.Contact h1 {
  color: #333;
}

.Contact p {
  font-size: 1.2em;
  color: #666;
}
''')
