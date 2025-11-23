# Telegram Bot for Render

This bot runs on Render.com using Python and TeleBot (pyTelegramBotAPI).
Do NOT hardcode your bot token anywhere in the project.
Instead, open your Render service → Environment → Add Environment Variable:

BOT_TOKEN=your_telegram_token

Then redeploy your service.

Start Command on Render:
python3 main.py
