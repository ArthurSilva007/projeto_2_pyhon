import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5

# Iniciando a automação
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(4)
pyautogui.press("tab")  
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=731, y=491)

# Carregando a tabela
tabela = pd.read_csv("alunos.csv")

time.sleep(3)

for linha in tabela.index:  
    nome = tabela.loc[linha,"Nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")
    
    email = tabela.loc[linha,"Email"]
    pyautogui.write(str(email))
    pyautogui.press("tab")
    
    endereco = tabela.loc[linha,"Endereco"]
    pyautogui.write(str(endereco))
    pyautogui.press("tab")
    
    telefone = tabela.loc[linha,"Telefone"]
    pyautogui.write(str(telefone))
    pyautogui.press("tab")    
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    # Corrigindo erro no scroll
    pyautogui.scroll(5000) 