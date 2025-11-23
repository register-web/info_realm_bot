# Aiogram Telegram Bot for Render (Webhook)

## Running locally
1. Export environment variables:
   - `BOT_TOKEN` — Telegram bot token
   - `WEBHOOK_BASE` — public URL that Telegram can reach (e.g., from ngrok)
2. Start the app:
   ```bash
   python main.py
   ```

## Deploying to Render
- No custom start command required; Render will use the Docker `CMD` defined in `Dockerfile` (`python main.py`).
- Set environment variables in Render:
  - `BOT_TOKEN=your_telegram_token`
  - `WEBHOOK_BASE=https://<your-render-service>.onrender.com`

The bot works **only via webhooks**. On startup it deletes the previous webhook and sets a new one to `${WEBHOOK_BASE}/webhook`.
