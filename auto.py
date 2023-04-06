#Bibliotecas instaladas PyAutoGui, mouseInfo e pillow
import pyautogui
from time import sleep

#Esses numeros são coordenadas da sua tela obtidos com a biblioteca mouseInfo
#Fase de login
pyautogui.click(568,433,duration=0.5)
pyautogui.write('Login')

pyautogui.click(565,459,duration=0.5)
pyautogui.write('Senha')

pyautogui.click(496,493,duration=0.5)
#Fase de leitura do txt e registro no sistema
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(288,419,duration=0.5)
        pyautogui.write(produto)
        
        pyautogui.click(286,448,duration=0.5)
        pyautogui.write(quantidade)
        
        pyautogui.click(284,472,duration=0.5)
        pyautogui.write(preco)
        
        pyautogui.click(208,632,duration=0.5)
        sleep(1)