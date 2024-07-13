from jinja2 import Template

# Define the navbar component template
navbar_template = Template('''
import React from "react";
import { Link } from "react-router-dom";

interface NavbarProps {
  items: string[];
}

const Navbar: React.FC<NavbarProps> = ({ items }) => {
  return (
    <nav className="navbar">
      <ul className="navbar__list">
        {items.map((item, index) => (
          <li key={index} className="navbar__item">
            <Link to={`/${item.toLowerCase()}`} className="navbar__link">
              {item}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;

''')
