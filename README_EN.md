# WeChat AI Assistant (Mac) |WeChat AI Intelligent Assistant
**WeChat AI Assistant (Mac)** is a WeChat automated assistant. It uses **EasyOCR** for real-time screen recognition, combines the **DeepSeek-V3** model provided by **NVIDIA NIM** to achieve intelligent dialogue, and is equipped with a geek **Rich** terminal dashboard, avoiding the risk of requiring API access such as GeWeChat and WeChatPadPro, making it suitable for novice experience
---
## Project Features
* ** Native Mac optimization **: Designed for Mac desktop WeChat UI, Retina screen coordinate adaptation is supported.
* ** Intelligent visual recognition **: Use `easyocr` to achieve millisecond-level text extraction, and accurately remove friend nicknames through Y-axis coordinate filtering.
* ** Top model-driven **: Connecting NVIDIA's integrated **DeepSeek-V3** model will provide more accurate understanding of the Chinese context and faster response.
* ** Two-way isolation logic **: Based on relative coordinate determination, it perfectly solves the repeater problem of AI "talking to itself".
---
## Environmental requirements
* ** Operating System **: macOS (Mac Mini or MacBook is recommended).
* ** Running environment **: Python 3.10+ (recommended to use **Conda** for environment management).
* ** Core dependencies **: `pyautogui`, `easyocr`, `openai`, `pyperclip`.
* ** Model support **: Valid NVIDIA NIM API Key.
---
## Start quickly
### 1. Cloning projects and installation dependencies
```bash
git clone https://github.com/YourUsername/WeChat-AI-Assistant-Mac.git
cd WeChat-AI-Assistant-Mac
pip install -r requirements.txt
```
### 3. Configuration and operation
1. ** Quick Start **
```bash
python main.py
```
2. ** Debugging options **: You can use pos.py to determine the mouse coordinates and fill in main.py directly. When debugging frequently, you don't need to wait a few seconds to determine the coordinates, which is more convenient
```bash
python pos.py
```
---
## Project structure
```text
├── main.py           #Main program
├── pos.py          #Coordinate detection gadget
├── requirements.txt #Project Dependency List
└── README.md       #Project Description Document
```
---
## ⚠️Disclaimer
This tool is only used for technical research and learning. Please use it on the premise of complying with relevant laws and regulations and the WeChat service agreement. The developer is not responsible for any account risks caused by improper use.
