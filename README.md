# Bot-TikTok

Este projeto é um **bot automatizado para interação com o site do TikTok**, escrito em Python. Ele simula ações humanas para logar automaticamente em uma conta TikTok utilizando a biblioteca `pyautogui`, que permite controle do mouse e teclado.

## 📁 Estrutura do Projeto

- `app.py`: Script principal. Abre o navegador, acessa o TikTok, e realiza login automatizado simulando cliques e digitação.
- `mouse-tracker.py`: Ferramenta auxiliar para identificar as coordenadas do mouse na tela, útil para configurar as ações do `pyautogui`.
- `curtida.png`: Um recurso visual usado pelo bot (Uusado para reconhecimento de imagem).
- `README.md`: Este arquivo de documentação.

## ⚙️ Como Funciona

1. O script `app.py` abre o navegador e acessa o site do TikTok.
2. Usa `pyautogui` para:
   - Clicar em posições específicas da tela (como o botão de login).
   - Digitar o e-mail e senha de login.
   - Finalizar o login e aguardar o carregamento da página.

**Importante:** As posições dos cliques (`pyautogui.click(x, y)`) são fixas. Isso significa que o script foi feito para um layout de tela/resolução específicos. É recomendado rodar o `mouse-tracker.py` para ajustar as coordenadas ao seu monitor.

## 🛠️ Requisitos

- Python 3.11+
- Bibliotecas:
  - `pyautogui`
  - `webbrowser`
  - `time` (nativa)

Instalação das dependências:

```bash
pip install pyautogui
```

---

## 🚨 **Avisos Importantes**  

- Este projeto é **apenas para fins educacionais**.  

- Automatizar interações em plataformas como o TikTok pode violar os termos de uso da plataforma. Use com responsabilidade e por sua conta e risco.  

- As credenciais estão atualmente hardcoded no código (`app.py`). **Remova-as antes de versionar ou compartilhar o projeto.**

---

## 📌 **Sugestões Futuras**  

- Tornar as coordenadas dinâmicas ou responsivas.  
- Adicionar interface gráfica para configuração.
