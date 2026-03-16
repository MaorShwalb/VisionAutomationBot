


## **VisionAutomationBot.**
**A Python automation project originally prototyped in Jupyter Notebook and later developed into a structured application using the pyautogui and keyboard libraries.  
"VisionAutomationBot" demonstrates automated interaction through image recognition, timed key sequences, and multi-threaded event handling to simulate responsive gameplay actions.  
This project focuses on experimentation with computer vision–based automation and input control in Python.  
I intentionally do not specify which game this automation is designed for, and I do not support the use of automation tools that violate the rules or terms of service of any game.**

___

### **Table of Contents:**
- [Introduction](#VisionAutomationBot)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [The Architecture](#the-architecture)
- [Technologies Used](#technologies-used)
- [Contact and Support](#contact-and-support)

___

### **Features.**

**1. Image Recognition Automation**
- Detects visual elements on the screen using image matching.
- Triggers automated actions only when the defined patterns appear.

**2. Multi-Threaded Event Handling**
- Background threads monitor timed events.
- Enables independent actions to run alongside the main automation loop.

**3. Human-Like Interaction Timing**
- Randomized delays simulate natural user behavior.
- Prevents repetitive or robotic input patterns.

**4. Automated Keyboard Input**
- Simulates complex key press sequences.
- Allows precise control of automated actions.

**5. Modular Automation Structure**
- Separates the GUI controller, automation engine, and monitoring threads.
- Makes the project easier to maintain and expand.

___

### **Usage**

#### The automation system is controlled through a simple graphical interface.

**Start**
- Launches the automation script.
- Activates the main automation loop and background monitoring threads.

**Stop**
- Safely terminates the automation process.

**Timer**
- Displays how long the automation has been running.

During execution, the bot continuously scans the screen for predefined images and performs automated input actions based on the detected results.

___

### **Installation**

To run the VisionAutomationBot locally, follow these steps:

1. Clone the repository

```
https://github.com/MaorShwalb/VisionAutomationBot
```

2. Install required Python libraries
   (Ensure Python (3.8+) is installed.)
```
pip install pyautogui keyboard opencv-python
```

3. Run the main GUI controller

```
python gui_controller.py
```

4. Press **Start** in the interface to begin automation.

___

### **The Architecture**

The project is structured around several main components:

**GUI Controller**
- Provides a simple interface for starting and stopping the automation.

**Automation Engine**
- Main loop responsible for scanning the screen and executing actions.

**Image Recognition Module**
- Detects predefined images on the screen using PyAutoGUI.

**Input Controller**
- Sends keyboard commands to simulate user interaction.

**Thread Monitoring System**
- Background threads manage timed triggers and additional actions.
-
___

### **Technologies Used.**

**Python:** high-level, versatile programming language widely used for software development, automation, data analysis, artificial intelligence, and machine learning.

**IntelliJ IDEA Community Edition:** a powerful and widely used integrated development environment (IDE) by JetBrains for software development. It provides advanced code editing, debugging, and project management tools, making development more efficient.

**Jupyter Notebook (Anaconda):** interactive development environment commonly used for data analysis, machine learning, and experimentation with Python. It allows combining code, visualizations, and documentation in a single notebook.

<a href="https://www.python.org" target="_blank"><img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="300"></a>
<a href="https://www.jetbrains.com/idea/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" alt="IntelliJ IDEA Logo" width="100"></a>
<a href="https://www.anaconda.com/products/distribution" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="Jupyter Logo" width="100"></a>

___

### **Contact and Support.**

**If you have any questions about this project, need assistance, or have found any bugs or issues in the application, please don't hesitate to reach out.  
Your feedback is valuable and helps improve the quality of this project and my knowledge.  
I appreciate your time and effort!  
Thank you for your contribution and support!**