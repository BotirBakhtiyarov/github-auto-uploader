# GitHub Project Automation Script Documentation

## Overview

This script automates the process of creating a new GitHub repository, adding a README file, initializing the repository, committing changes, setting the default branch, adding a remote origin, and pushing the initial commit using Selenium and command-line operations.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Script Explanation](#script-explanation)
4. [Running the Script](#running-the-script)
5. [Considerations](#considerations)
6. [Conclusion](#conclusion)

## Prerequisites

- Python installed on your system.
- `Selenium` library installed.
- Microsoft Edge WebDriver or any other WebDriver compatible with your browser installed and its path specified in the script.
- Active GitHub account credentials.

## Installation

1. **Install Selenium**:
   ```bash
   pip install selenium
   ```

2. **Download WebDriver**:
   Download the appropriate WebDriver for your browser and operating system. In this script, it's set to Microsoft Edge WebDriver (`msedgedriver.exe`).

## Script Explanation

### Importing Libraries

```python
from selenium import webdriver
from time import sleep
import os
```

- `webdriver`: Allows browser automation.
- `sleep`: Delays script execution.
- `os`: Provides operating system interfaces for executing command-line operations.

### User Inputs

The script prompts the user to input their GitHub username, password, and the name of the project.

### Opening GitHub and Logging In

The script opens the GitHub website, enters the login details provided by the user, and logs in.

### Creating a New Repository

After logging in, the script waits for account verification and then proceeds to create a new repository with the provided project name.

### Adding README File and Committing Changes

The script then prompts the user to input the content for the README file. It uses `echo` command to create a README file with the provided content, initializes the Git repository, adds all files, commits changes, and sets the default branch.

### Pushing Changes to GitHub

Finally, the script adds the remote origin and pushes the initial commit to GitHub.

## Running the Script

1. Ensure you have the required libraries installed and WebDriver downloaded.
2. Run the script:
   ```bash
   python auto-git.py
   ```
3. Enter your GitHub username, password, and project name when prompted.
4. Verify your GitHub account within the specified time.
5. Wait for the script to complete the automation process.

## Considerations

- **WebDriver Path**: Ensure the path to your WebDriver is correctly specified in the script.
- **GitHub Verification**: The script waits for account verification, ensure you complete this step within the specified time.
- **Internet Connection**: Ensure a stable internet connection as the script interacts with the GitHub website.

## Conclusion

This script provides a convenient way to automate the process of creating a new GitHub repository and pushing the initial commit. Use it responsibly and adjust it as needed for your specific use case.