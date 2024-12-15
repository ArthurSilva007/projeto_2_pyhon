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
pyautogui.press("enter")

pyautogui.sleep(5)
pyautogui.click(x=1147, y=688)
pyautogui.write("Teste de nome")
pyautogui.press("tab")

#VARIAVEIS

tabela = pd.read_csv("alunos.csv")

time.sleep(3)

for linha in tabela.index:  
    Lucas   lucas@email.com Avenida G, 987  (81) 23456-7890 
    Giovana giovana@email.com
    pyautogui.write(tabela.loc[linha, "Nome"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "Email"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "Endereco"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "Telefone"])
    pyautogui.press("tab")Joo    
    pyautogui.press("enter")C, 789  (51) 65432-1432 
    F, 567  (71) 34567-8765