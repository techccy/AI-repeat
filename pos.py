import pyautogui
import time

print("请在 5 秒内把鼠标移动到微信【最后一条消息的左上角】...")
time.sleep(5)
p1 = pyautogui.position()
print(f"起点捕获: {p1}")

print("请在 3 秒内把鼠标移动到微信【最后一条消息的右下角】...")
time.sleep(3)
p2 = pyautogui.position()
print(f"终点捕获: {p2}")

width = p2.x - p1.x
height = p2.y - p1.y
print(f"\n你的 CHAT_REGION 应该是: ({p1.x}, {p1.y}, {width}, {height})")
