import pyautogui
import easyocr
import time
import sys
import pyperclip
from openai import OpenAI

# --- 配置区 ---
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY"
)

# 使用 DeepSeek-V3.2，中文理解力强且响应极快
MODEL = "deepseek-ai/deepseek-v3.2"
# MODEL = "nvidia/llama-3.1-nemotron-nano-4b-v1.1"
# MODEL = "openai/gpt-oss-120b"

# 初始化 OCR
print("正在初始化 OCR 引擎...")
reader = easyocr.Reader(['ch_sim', 'en'])

# --- 坐标捕获流程 ---
print("请在 5 秒内把鼠标移动到微信【最后一条消息的左上角】...")
time.sleep(5)
p1 = pyautogui.position()
print(f"起点捕获: {p1}")

print("请在 3 秒内把鼠标移动到微信【最后一条消息的右下角】...")
time.sleep(3)
p2 = pyautogui.position()
print(f"终点捕获: {p2}")

print("请在 3 秒内把鼠标移动到微信【输入框】...")
time.sleep(3)
p3 = pyautogui.position()
print(f"输入框捕获: {p3}")

# 计算区域
width = p2.x - p1.x
height = p2.y - p1.y
CHAT_REGION = (p1.x, p1.y, width, height)
INPUT_POS = (p3.x, p3.y)

# 判定阈值：消息左边界在截图区域宽度的 30% 以内才认为是好友消息
# 你可以根据实际气泡位置微调这个比例

LEFT_THRESHOLD = width * 0.3        # 左边缘阈值，根据截图宽度计算


def update_status(msg):
    sys.stdout.write(f"\r\033[K[监控中] {msg}")
    sys.stdout.flush()

def run_mac_bot():
    print(f"\n🖥️ Mac Desktop AI Assistant Started | Model: {MODEL}")
    print(f"判定阈值: 左边缘 {LEFT_THRESHOLD:.1f} 像素以内")
    print("-" * 50)
    last_text = ""

    while True:
        try:
            update_status("正在扫描并分析左右坐标...")
            
            # 1. 截图并识别（开启 detail=1 获取详细坐标）
            screenshot = pyautogui.screenshot(region=CHAT_REGION)
            screenshot.save("debug_shot.png")
            
            # result 格式: [([[x,y],[x,y],[x,y],[x,y]], text, confidence), ...]
            results = reader.readtext("debug_shot.png", detail=1)
            
            # 过滤出所有靠左侧的文字块
            friend_text_chunks = []
            for (bbox, text, prob) in results:
                # bbox[0][0] 是文字块左上角的相对 X 坐标
                msg_left_x = bbox[0][0]
                
                # 如果文字块起点在左侧，则判定为对方消息
                if msg_left_x < LEFT_THRESHOLD:
                    friend_text_chunks.append(text)
            
            current_text = "".join(friend_text_chunks).strip()
            
            # 2. 判断是否有新消息
            if current_text and current_text != last_text:
                print(f"\n📩 收到好友消息: {current_text}")
                
                update_status("Thinking...")
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": current_text}]
                )
                ai_reply = response.choices[0].message.content
                
                # 3. 模拟回复
                update_status("正在发送回复...")
                pyautogui.click(INPUT_POS)
                time.sleep(0.2)
                pyperclip.copy(ai_reply)
                pyautogui.hotkey('command', 'v')
                time.sleep(0.3)
                pyautogui.press('enter')
                
                print(f"🤖 AI 已回复: {ai_reply[:20]}...")
                last_text = current_text
                
            time.sleep(2) # 扫描频率

        except KeyboardInterrupt:
            print("\n👋 程序已停止")
            break
        except Exception as e:
            update_status(f"⚠️ 出错: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_mac_bot()
