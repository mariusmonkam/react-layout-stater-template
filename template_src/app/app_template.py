from jinja2 import Template

# Define the template for the App.tsx file
app_template = Template('''
import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import { Provider } from "react-redux";
import store from "./store/store";

const App: React.FC = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <Provider store={store}>
      <Router>
        <div className={`app ${sidebarOpen ? "sidebar-open" : ""}`}>
          <Header
            logoText="My Logo"
            navbarItems={["Home", "About", "Contact"]}
            onMenuToggle={toggleSidebar}
            isSidebarOpen={sidebarOpen}
          />
          <Sidebar isOpen={sidebarOpen} onClose={toggleSidebar} />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Navigate to="/home" />} />
              <Route path="/home" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
            </Routes>
          </main>
          <Footer text="Marius Monkam" />
        </div>
      </Router>
    </Provider>
  );
};

export default App;



''')
