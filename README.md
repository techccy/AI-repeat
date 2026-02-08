# WeChat AI Assistant (Mac) | 微信 AI 智能助手

**WeChat AI Assistant (Mac)** 是一款专为 macOS 设计的微信自动化助手。它利用 **EasyOCR** 进行实时屏幕识别，结合 **NVIDIA NIM** 提供的 **DeepSeek-V3** 模型 实现智能对话，并配备了极客风的 **Rich** 终端仪表盘。

---

## 🌟 项目特性

* **原生 Mac 优化**：针对 Mac 桌面端微信 UI 设计，支持 Retina 屏幕坐标适配。
* **智能视觉识别**：使用 `easyocr` 实现毫秒级文字提取，并通过 Y 轴坐标过滤精准剔除好友昵称。
* **顶级模型驱动**：接入 NVIDIA 集成的 **DeepSeek-V3** 模型，中文语境理解更精准、响应更快。
* **双向隔离逻辑**：基于相对坐标判定，完美解决 AI “自言自语”的复读机问题。

---

## 🛠️ 环境要求

* **操作系统**: macOS (推荐使用 Mac Mini 或 MacBook)。
* **运行环境**: Python 3.10+ (建议使用 **Conda** 进行环境管理)。
* **核心依赖**: `pyautogui`, `easyocr`, `openai`, `pyperclip`。
* **模型支持**: 有效的 NVIDIA NIM API Key。

---

## 🚀 快速开始

### 1. 克隆项目与安装依赖

```bash
git clone https://github.com/YourUsername/WeChat-AI-Assistant-Mac.git
cd WeChat-AI-Assistant-Mac
pip install -r requirements.txt

```

### 3. 配置与运行

1. **快速启动**
```bash
python main.py

```
2. **调试选项**：可以利用pos.py来确定鼠标坐标，直接填入main.py，在经常调试时不需要每次等个几秒确定坐标，比较方便
```bash
python pos.py

```

---

## 📂 项目结构

```text
├── main.py           # 主程序
├── pos.py          # 坐标探测小工具
├── requirements.txt # 项目依赖清单
└── README.md       # 项目说明文档

```

---

## ⚠️ 免责声明

本工具仅用于技术研究与学习。请在遵守相关法律法规及微信服务协议的前提下使用，开发者不对任何因不当使用导致的账号风险负责。
