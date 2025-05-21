# Bot-TikTok

This project is an **automated bot for interacting with the TikTok website**, written in Python. It simulates human actions to automatically log into a TikTok account using the `pyautogui` library, which allows mouse and keyboard control.

## 📁 Project Structure

- `app.py`: Main script. Opens the browser, accesses TikTok, and performs automated login by simulating clicks and typing.
- `mouse-tracker.py`: Auxiliary tool to identify mouse coordinates on the screen, useful to configure `pyautogui` actions.
- `curtida.png`: A visual asset used by the bot (used for image recognition).
- `README.md`: This documentation file.

## ⚙️ How It Works

1. The `app.py` script opens the browser and navigates to the TikTok site.
2. Uses `pyautogui` to:
   - Click on specific screen positions (such as the login button).
   - Type the login email and password.
   - Complete the login and wait for the page to load.

**Important:** The click positions (`pyautogui.click(x, y)`) are fixed. This means the script was made for a specific screen layout/resolution. It is recommended to run `mouse-tracker.py` to adjust coordinates to your monitor.

## 🛠️ Requirements

- Python 3.11+
- Libraries:
  - `pyautogui`
  - `webbrowser`
  - `time` (built-in)

Install dependencies with:

```bash
pip install pyautogui
