import pyautogui
import time

image_path = r'D:\Bot.py\pythonProject2\screen\image.png'
confidence = 0.65

print("Опять работа?")

while True:
    time.sleep(10)
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            print("Изображение найдено!")
            print(location)
            pyautogui.moveTo(location)
            pyautogui.click()
            break


    except pyautogui.ImageNotFoundException:
        print("Изображение не найдено. Попробуйте еще раз.")
        pyautogui.hotkey('ctrl','r')