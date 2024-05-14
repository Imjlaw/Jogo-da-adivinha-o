import pyautogui as py
import time

py.PAUSE = 0.9


# Abrir o navegador (Opera)
py.press("win")
py.write("opera")
py.press("enter")
py.click(x=1311, y=389)

time.sleep(5)

py.click(x=317, y=457)
py.write("Como eu amo ser um bot <3")
py.press("enter")