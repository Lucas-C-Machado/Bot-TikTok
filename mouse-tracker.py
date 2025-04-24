import pyautogui

try: # Tenta fazer o que está dentro do bloco try
    while True:
        x, y = pyautogui.position() # Pega a posição atual do mouse na tela como (x, y).
        print(x, y)
except KeyboardInterrupt: # Quando eu apertar o ctrl+c, o programa vai parar de rodar
    print('\nDone.') # E vai aparecer essa mensagem de finalização
