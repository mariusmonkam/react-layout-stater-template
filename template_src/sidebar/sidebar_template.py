from jinja2 import Template

# Define the Sidebar component template
sidebar_template = Template('''
import React from "react";
import "./Sidebar.css";
import { Link } from "react-router-dom";

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen, onClose }) => {
  return (
    <div className={`sidebar ${isOpen ? "open" : ""}`}>
      <div className="sidebar__content">
        <h1>Sidebar Component</h1>
        <ul className="sidebar__list">
          <li className="sidebar__item">
            <Link to="/" className="sidebar__link" onClick={onClose}>
              Home
            </Link>
          </li>
          <li className="sidebar__item">
            <Link to="/about" className="sidebar__link" onClick={onClose}>
              About
            </Link>
          </li>
          <li className="sidebar__item">
            <Link to="/contact" className="sidebar__link" onClick={onClose}>
              Contact
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;

''')
