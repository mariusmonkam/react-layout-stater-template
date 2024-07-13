from jinja2 import Template

# Define the CSS file for the Header component
header_css_template = Template('''
/* Header.css */

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background-color: #3498db; /* New background color */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  color: white; /* Text color for better contrast */
}

.header__logo {
  display: flex;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.header__toggle-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 30px;
  height: 30px;
  transition: transform 0.3s, opacity 0.3s;
}

.header__toggle-button span {
  display: block;
  width: 100%;
  height: 3px;
  background-color: white; /* White for contrast against the blue background */
  transition: transform 0.3s, opacity 0.3s;
}

.header__toggle-button.open span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.header__toggle-button.open span:nth-child(2) {
  opacity: 0;
}

.header__toggle-button.open span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

.navbar {
  display: flex;
  align-items: center;
}

.navbar__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.navbar__item {
  margin-left: 20px;
}

.navbar__link {
  text-decoration: none;
  color: white;
  font-size: 16px;
  padding: 10px;
  transition: background-color 0.3s, color 0.3s;
}

.navbar__link:hover {
  background-color: #2980b9;
  color: #fff;
  border-radius: 5px;
}

/* Logo styles */
.logo-container {
  display: flex;
  align-items: center;
}

.logo-image {
  height: 100%;
  width: auto;
  max-width: 100%; /* Adjust max-width as needed */
}

.logo-svg {
  height: 100%; /* Adjust height as needed */
  width: 100%; /* Adjust width as needed */
}

.logo-text {
  fill: #d8e0e6; /* Default text color */
  font-family: 'Poppins', sans-serif;
  font-size: 30px; /* Adjust font-size as needed */
  font-weight: bold;
}

@media only screen and (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: stretch;
  }

  .header__toggle-button {
    order: 2;
  }

  .navbar {
    margin-top: 10px;
    order: 1;
  }

  .navbar__list {
    flex-direction: column;
    align-items: stretch;
  }

  .navbar__item {
    margin: 0;
    padding: 10px 0;
    border-top: 1px solid #ccc;
  }
}


''')
