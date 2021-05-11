import pyautogui
import time

t=0.25
pyautogui.moveTo(1773, 11, duration=t)
pyautogui.click()

for i in range(10):
    pyautogui.moveTo(1053, 575, duration=t)
    pyautogui.click()
    pyautogui.moveTo(704, 742, duration=t)
    pyautogui.click()
    pyautogui.moveTo(964, 555, duration=t)
    pyautogui.click()

    pyautogui.moveTo(695, 566, duration=t)
    pyautogui.click()
    pyautogui.moveTo(704, 742, duration=t)
    pyautogui.click()
    pyautogui.moveTo(964, 555, duration=t)
    pyautogui.click()
    pyautogui.moveTo(695, 566, duration=t)
    pyautogui.click()
    pyautogui.moveTo(704, 742, duration=t)
    pyautogui.click()
    pyautogui.moveTo(964, 555, duration=t)
    pyautogui.click()

'''
coordenada=pyautogui.position()
print(coordenada)
'''
