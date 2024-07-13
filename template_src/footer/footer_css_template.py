from jinja2 import Template

# Define the CSS file for the Footer component
footer_css_template = Template('''

.footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #3498db; /* Accent color */
  padding: 20px 0;
  text-align: center;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
  color: white; /* White text for contrast */
}

.footer-columns {
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
}

.footer-column {
  flex: 1;
  padding: 0 20px;
}

.footer-column h3 {
  margin-top: 0;
}

.footer-copyright {
  border-top: 1px solid #ddd;
  padding-top: 10px;
  font-size: 14px;
  color: #ecf0f1;
}

.footer a {
  color: #ecf0f1; /* Light color for links */
  text-decoration: none;
}

.footer a:hover {
  text-decoration: underline;
}

@media only screen and (max-width: 600px) {
  .footer {
    padding: 10px;
  }

  .footer-columns {
    flex-direction: column;
    align-items: center;
  }

  .footer-column {
    padding: 10px 0;
  }
}


''')
