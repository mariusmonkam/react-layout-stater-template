from jinja2 import Template

# Define the CSS file for the Home component
home_css_template = Template('''
.home {
  text-align: center;
}

.hero-section {
  width: 100%;
  max-width: 1280px;
  padding: 60px 55px;
  background: #ffffff; /* Light background */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  gap: 40px;
  margin: 0 auto;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

.hero-text {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center; /* Centered text */
  gap: 20px;
  width: 100%;
}

.hero-title {
  text-align: center;
  color: #2c3e50; /* Darker shade for text */
  font-size: 60px; /* Adjusted for better responsiveness */
  font-family: "Poppins", sans-serif;
  font-weight: 700;
  line-height: 1.2;
  word-wrap: break-word;
  width: 100%;
}

.hero-subtitle {
  text-align: left; /* Adjusted alignment */
  color: #34495e; /* Slightly lighter than the title for contrast */
  font-size: 20px; /* Adjusted for better responsiveness */
  font-family: "Mulish", sans-serif;
  font-weight: 400;
  line-height: 1.5;
  word-wrap: break-word;
  width: 100%;
}

.feature-columns {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.feature-column {
  flex: 1;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.check-icon {
  flex-shrink: 0;
}

.hero-buttons {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 18px;
}

.hero-button {
  padding: 16px 50px;
  background: #3498db; /* New accent color for button */
  border-radius: 30px; /* More rounded corners */
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow for button */
  cursor: pointer;
}

.button-text {
  text-align: center;
  color: white;
  font-size: 16px;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  line-height: 24px;
  word-wrap: break-word;
}

@media only screen and (max-width: 768px) {
  .hero-title {
    font-size: 40px;
    line-height: 1.2;
  }

  .hero-subtitle {
    font-size: 18px;
    line-height: 1.5;
  }

  .hero-section {
    padding: 40px 20px;
  }

  .feature-columns {
    flex-direction: column;
  }

  .feature-item {
    align-items: flex-start;
  }
}

@media only screen and (max-width: 600px) {
  .hero-title {
    font-size: 30px;
    line-height: 1.2;
  }

  .hero-subtitle {
    font-size: 16px;
    line-height: 1.5;
  }

  .hero-section {
    padding: 30px 10px;
  }

  .hero-button {
    padding: 12px 30px;
  }

  .button-text {
    font-size: 14px;
  }
}


''')
