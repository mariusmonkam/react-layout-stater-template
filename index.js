const { spawn } = require("child_process");
const path = require("path");

// Get the path to main.py
const mainPyPath = path.join(__dirname, "main.py");
console.log(`Running script at: ${mainPyPath}`);

// Run the main.py script as a child process
const pythonProcess = spawn("python", [mainPyPath], { stdio: "inherit" });

// Handle error events
pythonProcess.on("error", (err) => {
  console.error("Failed to start subprocess.");
  console.error(err);
});

// Listen for the Python script to exit
pythonProcess.on("close", (code) => {
  console.log(`Python script exited with code ${code}`);
});
