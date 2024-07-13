import os
import sys
import json
import subprocess
import time
from tqdm import tqdm

# Importing templates and other required variables
from template_src.config.config_template import default_config 
from template_src.utils.utils import component_dir,app_file
from template_src.logo.logo_template import logo_template
from template_src.navbar.navbar_template import navbar_template
from template_src.header.header_css_template import header_css_template
from template_src.header.header_template import header_template
from template_src.sidebar.sidebar_css_template import sidebar_css_template
from template_src.sidebar.sidebar_template import sidebar_template
from template_src.footer.footer_template import footer_template
from template_src.footer.footer_css_template import footer_css_template
from template_src.home.home_css_template import home_css_template
from template_src.home.home_template import home_template
from template_src.app.app_template import app_template
from template_src.store.store_template import store_template
from template_src.store.root_reducer_template import root_reducer_template
from template_src.features.slice.slice_template import slice_template
from template_src.features.counter.counter_template import counter_template
from template_src.pages.about_template import about_template, about_css_template
from template_src.pages.contact_template import contact_template, contact_css_template

# Create a dictionary of stages
stages = [
    "Create the project directory",
    "Change to project directory",
    "Create React app with TypeScript template",
    "Install ajv package",
    "Install Redux Toolkit",
    "Install react-router-dom",
    "Create components directory",
    "Generate CSS for Header component",
    "Generate Logo component",
    "Generate Navbar component",
    "Generate Header component",
    "Generate Sidebar component",
    "Generate Sidebar CSS",
    "Generate Home component",
    "Generate Home CSS",
    "Generate Footer component",
    "Generate Footer CSS",
    "Generate Redux store",
    "Generate root reducer",
    "Generate Redux slice",
    "Generate Counter component",
    "Generate About component",
    "Generate CSS for About component",
    "Generate Contact component",
    "Generate CSS for Contact component",
    "Replace App.tsx contents",
    "Start development server"
]

# Load configuration from config_template
config = default_config

# Absolute path to config file
config_path = os.path.join(os.path.dirname(__file__), 'template_config.json')

# Read configuration file if exists and update config
if (os.path.exists(config_path)):
    with open(config_path) as config_file:
        custom_config = json.load(config_file)
        config.update(custom_config)

# Extract variables from config
project_name = config.get("project_name", "my-react-app")
project_path = config.get("project_path", os.getcwd())
logo_text = config.get("logoText", "My Logo")
navbar_items = config.get("navbar", ["Home", "About", "Contact"])
footer_text = config.get("footerText", "Footer Component")
home_content = config.get("homeContent", "Welcome to the Home Page")

# If no project path is provided, use the current directory as the default
if not project_path:
    project_path = os.getcwd()

# Check if the generator is located within the 'node_modules' directory
if 'node_modules' in os.getcwd().split(os.sep):
    # Move up one level to the parent directory
    project_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


# Prompt the user to provide a name for the app
project_name = input("Enter a name for your React application (press Enter for default 'my-react-app'): ").strip()

# Use a default example name if the user doesn't provide one
if not project_name:
    project_name = "my-react-app"

# Create the full path to the project directory
project_dir = os.path.join(project_path, project_name)

# Create progress bar
with tqdm(total=len(stages), bar_format='{l_bar}{bar}{r_bar}{bar:-10b}') as pbar:

    # Stage 0: Create the project directory if it doesn't exist
    pbar.set_description(stages[0])
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 1: Change the current working directory to the project directory
    pbar.set_description(stages[1])
    os.chdir(project_dir)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 2: Run the create-react-app command to create a new React project with TypeScript template
    pbar.set_description(stages[2])
    subprocess.call(['npx', 'create-react-app', '.', '--template', 'typescript'], shell=True)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 3: Install ajv package as a development dependency
    pbar.set_description(stages[3])
    subprocess.call(['npm', 'install', '--save-dev', 'ajv'], shell=True)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 4: Install Redux Toolkit
    pbar.set_description(stages[4])
    subprocess.call(['npm', 'install', '@reduxjs/toolkit', 'react-redux'], shell=True)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 5: Install react-router-dom
    pbar.set_description(stages[5])
    subprocess.call(['npm', 'install', 'react-router-dom'], shell=True)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 6: Create the components directory if it doesn't exist
    pbar.set_description(stages[6])
    if not os.path.exists(component_dir):
        os.makedirs(component_dir)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 7: Generate the CSS file for the Header component
    pbar.set_description(stages[7])
    with open(os.path.join(component_dir, 'Header.css'), 'w') as f:
        f.write(header_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 8: Render logo component
    pbar.set_description(stages[8])
    logo_component = logo_template.render(logoText=logo_text)
    with open(os.path.join(component_dir, 'Logo.tsx'), 'w') as f:
        f.write(logo_component)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 9: Render navbar component
    pbar.set_description(stages[9])
    navbar_component = navbar_template.render(items=navbar_items)
    with open(os.path.join(component_dir, 'Navbar.tsx'), 'w') as f:
        f.write(navbar_component)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 10: Render header component with logo and navbar
    pbar.set_description(stages[10])
    header_component = header_template.render(logoText=logo_text, navbarItems=navbar_items)
    with open(os.path.join(component_dir, 'Header.tsx'), 'w') as f:
        f.write(header_component)
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 11: Generate the Sidebar component
    pbar.set_description(stages[11])
    with open(os.path.join(component_dir, 'Sidebar.tsx'), 'w') as f:
        f.write(sidebar_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 12: Generate the Sidebar CSS file
    pbar.set_description(stages[12])
    with open(os.path.join(component_dir, 'Sidebar.css'), 'w') as f:
        f.write(sidebar_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 13: Generate the Footer component
    pbar.set_description(stages[13])
    with open(os.path.join(component_dir, 'Footer.tsx'), 'w') as f:
        f.write(footer_template.render(text=footer_text))
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 14: Generate the Footer CSS file
    pbar.set_description(stages[14])
    with open(os.path.join(component_dir, 'Footer.css'), 'w') as f:
        f.write(footer_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 15: Generate the Redux store
    pbar.set_description(stages[15])
    store_dir = os.path.join(project_dir, 'src', 'store')
    if not os.path.exists(store_dir):
        os.makedirs(store_dir)
    store_path = os.path.join(store_dir, 'store.ts')
    with open(store_path, 'w') as f:
        f.write(store_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 16: Generate the root reducer
    pbar.set_description(stages[16])
    root_reducer_path = os.path.join(store_dir, 'rootReducer.ts')
    with open(root_reducer_path, 'w') as f:
        f.write(root_reducer_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 17: Generate the Redux slice
    pbar.set_description(stages[17])
    slice_dir = os.path.join(project_dir, 'src', 'features')
    if not os.path.exists(slice_dir):
        os.makedirs(slice_dir)
    slice_path = os.path.join(slice_dir, 'counterSlice.ts')
    with open(slice_path, 'w') as f:
        f.write(slice_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 18: Generate the Counter component
    pbar.set_description(stages[18])
    counter_path = os.path.join(component_dir, 'Counter.tsx')
    with open(counter_path, 'w') as f:
        f.write(counter_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 19: Generate the About component
    pbar.set_description(stages[19])
    pages_dir = os.path.join(project_dir, 'src', 'pages')
    if not os.path.exists(pages_dir):
        os.makedirs(pages_dir)
        
    with open(os.path.join(pages_dir, 'About.tsx'), 'w') as f:
        f.write(about_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 20: Generate the CSS file for the About component
    pbar.set_description(stages[20])
    with open(os.path.join(pages_dir, 'About.css'), 'w') as f:
        f.write(about_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 21: Generate the Contact component
    pbar.set_description(stages[21])
    with open(os.path.join(pages_dir, 'Contact.tsx'), 'w') as f:
        f.write(contact_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 22: Generate the CSS file for the Contact component
    pbar.set_description(stages[22])
    with open(os.path.join(pages_dir, 'Contact.css'), 'w') as f:
        f.write(contact_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)
     # Stage 23: Generate the Home component
    pbar.set_description(stages[23])
    with open(os.path.join(pages_dir, 'Home.tsx'), 'w') as f:
        f.write(home_template.render(content=home_content))
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 24: Generate the Home CSS file
    pbar.set_description(stages[24])
    with open(os.path.join(pages_dir, 'Home.css'), 'w') as f:
        f.write(home_css_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 25: Replace the contents of the App.tsx file with the template
    pbar.set_description(stages[25])
    app_tsx_path = os.path.join(project_dir, 'src', 'App.tsx')
    with open(app_tsx_path, 'w') as f:
        f.write(app_template.render())
    time.sleep(0.5)  # Adding sleep to simulate progress
    pbar.update(1)

    # Stage 26: Run the npm command to start the development server
    pbar.set_description(stages[26])
    subprocess.call(['npm', 'start'], shell=True)
    pbar.update(1)
