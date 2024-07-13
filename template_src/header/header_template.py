from jinja2 import Template

# Define the Header component template
header_template = Template('''
import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";
import Logo from "./Logo";

interface HeaderProps {
  logoText: string;
  navbarItems: string[];
  onMenuToggle: () => void;
  isSidebarOpen: boolean;
}

const Header: React.FC<HeaderProps> = ({ logoText, navbarItems }) => {
  return (
    <header className="header">
      <div className="header__logo">
        <Logo logoText={logoText} />
      </div>
      <nav className="navbar">
        <ul className="navbar__list">
          {navbarItems.map((item, index) => (
            <li key={index} className="navbar__item">
              <Link
                to={`/${
                  item.toLowerCase() === "home" ? "" : item.toLowerCase()
                }`}
                className="navbar__link"
              >
                {item}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
};

export default Header;

''')
