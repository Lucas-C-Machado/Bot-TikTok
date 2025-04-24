#!python3.11

import webbrowser
import pyautogui
from time import sleep # Biblioteca que gera um tempo entre as ações executadas

# Abre o navegador e vai para o site do TikTok
webbrowser.open('https://tiktok.com')

# Espera 5 segundos para o usuário poder ver o site
sleep(5)
pyautogui.click(950, 530, duration=2) # Vai pegar a biblioteca e passar as coordenadas do mouse e acrescentar o tempo de duração de 2 segundos

sleep(3)
pyautogui.click(1050, 350, duration=2) # Clica em "Entrar com nome de usuário ou e-mail"
pyautogui.click(949, 402, duration=2) # Clica no e-mail para preenchimento
pyautogui.write("1testegeral0@gmail.com") # Escreve o meu e-mail"

sleep(2)
pyautogui.click(812, 471, duration=2) # Clica na senha para preenchimento
sleep(2)
pyautogui.write("oI5a_w01qHncf04") # Escreve a minha senha
pyautogui.click(954, 589, duration=2) # Entra na conta

sleep(10) # Descansa por 10 segundos para dar tempo de carregar a página

# Abre o navegador e vai para o site do TikTok
webbrowser.open('https://www.tiktok.com/@oreidosites')  # Abre o perfil do TikTok

sleep(5)  # Espera 5 segundos para garantir que a página carregou
pyautogui.click(508, 761, duration=2)  # Clica no vídeo para começar a assistir

while True:
    try:
        # Tenta localizar a imagem da curtida
        imagem = pyautogui.locateOnScreen("curtida.png", confidence=0.8)  # Ajuste o parâmetro "confidence" se necessário
        sleep(3)  # Espera um pouco após encontrar a curtida

        if imagem:
            # Se a curtida for encontrada, significa que o vídeo já foi curtido
            pyautogui.click(1267, 401, duration=2)  # Clica fora da área da curtida (descurtir)
            sleep(3)  # Espera 3 segundos
            pyautogui.press("down")  # Rola para o próximo vídeo
            sleep(3)  # Dá um tempo para a próxima rolagem

        else:
            # Se a curtida não for encontrada, o vídeo não está curtido
            pyautogui.click(1300, 368, duration=2)  # Clica no botão de "Curtir"
            sleep(3)  # Espera 3 segundos
            pyautogui.press("down")  # Rola para o próximo vídeo
            sleep(3)  # Dá um tempo para a próxima rolagem

    except pyautogui.ImageNotFoundException:
        # Caso a imagem da curtida não seja encontrada, apenas rola para o próximo vídeo
        sleep(3)
        pyautogui.press("down")  # Rola para o próximo vídeo
        sleep(3)  # Dá um tempo para a próxima rolagem