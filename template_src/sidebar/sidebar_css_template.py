from jinja2 import Template

# Define the CSS file for the Sidebar component
sidebar_css_template = Template('''
.sidebar {
  background-color: #ecf0f1; /* Light gray background */
  padding: 20px;
  width: 250px; /* Fixed width for larger screens */
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  transform: translateX(-100%);
  transition: transform 0.3s ease-out;
  z-index: 1000; /* Ensure sidebar is above other content */
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.sidebar.open {
  transform: translateX(0);
}

.sidebar__content {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.sidebar__list {
  list-style-type: none;
  padding: 0;
}

.sidebar__item {
  margin-bottom: 10px;
}

.sidebar__link {
  text-decoration: none;
  color: #2c3e50;
  font-size: 16px;
  display: block;
  padding: 10px;
  transition: background-color 0.3s, color 0.3s;
}

.sidebar__link:hover {
  background-color: #bdc3c7;
  color: #2c3e50;
}

@media only screen and (max-width: 768px) {
  .sidebar {
    width: 100%; /* Full width for smaller screens */
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .sidebar.open {
    transform: translateX(0);
  }
}


''')
