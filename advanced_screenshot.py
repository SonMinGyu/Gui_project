import time
import keyboard
from PIL import ImageGrab


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png" .format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9키를 누르면 스크린 샷 저장

keyboard.wait("esc")  # esc 누르면 프로그램 종료
