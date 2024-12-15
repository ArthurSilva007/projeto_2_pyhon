import pyautogui
import pandas as pd
import time



#Iniciando a automação
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
pyautogui.sleep(4)
pyautogui.press("tab")  
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
#entrar no link
