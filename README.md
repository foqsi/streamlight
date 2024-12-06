# StreamLights - Streaming Indicator Tool
Simple little program that shows me what I've disabled while streaming.
![image](https://github.com/user-attachments/assets/9f01db3d-7b20-40b8-961a-a460afe219d2)

## Features
- Displays indicators for streaming-related toggles (e.g., microphone, camera, desktop audio).
- Customizable labels and key assignments.
- Works with macro keys F13-F24.

## Usage
If you want to use this program, you can do so as-is. Just remember:
- You need to set up your macro keys to **F13**-**F24**.
- You can customize the text and key assignments by editing <code>main.py</code>.

## Setup Instructions
Follow these steps to set up StreamLights on your system:

### 1. Install Python
Make sure you have Python installed. You can download it from [python.com](http://www.python.org).

### 2. Install PyInstaller
To create a standalone executable, you need to install PyInstaller. Run the following command:
```bash
pip install pyinstaller
```

### 3. Build the Executable
Navigate to the directory containing the <code>main.py</code> script and run:
```bash
pyinstaller --onefile --windowed --name StreamLights --icon=icon.ico main.py
```
- <code>--onefile</code>: Bundles everything into a single executable.
- <code>--windowed</code>: Suppresses the console window for GUI applications.
- <code>--name StreamLights</code>: Sets the name of the generated executable.
- <code>--icon=icon.ico</code>: Sets a custom icon for the executable.

### 4. Running the application
After running PyInstaller, you will find the generated executable in the <code>dist</code> folder. You can now use this executable to run the program.

## Customization
You can easily customize the following aspects of the program:
- **Labels**: Modify the text that appears on the buttons.
- **Key Assignments**: Change the keys that toggle the buttons by editing the <code>key_assignments</code> in <code>main.py</code>.


How to set up yourself

Install python

Install pyinstaller

navigate to the directory and run the following command
pyinstaller --onefile --windowed --name StreamLights --icon=icon.ico --clean main.py
