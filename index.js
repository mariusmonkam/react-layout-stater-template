const { spawn } = require("child_process");
const path = require("path");

// Get the path to main.py and requirements.txt
const mainPyPath = path.join(__dirname, "main.py");
const requirementsPath = path.join(__dirname, "requirements.txt");

console.log(`Running script at: ${mainPyPath}`);
console.log(`Installing Python packages from: ${requirementsPath}`);

// Function to run a shell command and return a promise
function runCommand(command, args) {
  return new Promise((resolve, reject) => {
    const process = spawn(command, args, { stdio: "inherit" });
    process.on("close", (code) => {
      if (code !== 0) {
        reject(`Command failed with code ${code}`);
      } else {
        resolve();
      }
    });
  });
}

// Check if the main.py file exists
const fs = require("fs");
if (!fs.existsSync(mainPyPath)) {
  console.error("Error: main.py does not exist at the specified path.");
  process.exit(1);
}

// Install Python packages from requirements.txt
runCommand("pip", ["install", "-r", requirementsPath])
  .then(() => {
    // Run the main.py script as a child process
    return runCommand("python", [mainPyPath]);
  })
  .then(() => {
    console.log("Python script executed successfully.");
  })
  .catch((error) => {
    console.error("An error occurred:");
    console.error(error);
  });
