import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === CONFIGURATION ===
FASTAPI_BASE_URL = "http://localhost:8000"  # Change to your FastAPI server URL
TELEGRAM_BOT_TOKEN = "7824610516:AAFzQFbPHnWXKvNl_6DaYd7l4mKaXtxVtuc"

# === LOGGING ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# === COMMAND HANDLERS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a command:\n"
                                    "/delete - Clear all data\n"
                                    "/ingest <URL> - Save text from URL\n"
                                    "Or just ask a question.")

async def delete_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session_id = str(update.effective_chat.id)
    response = requests.get(f"{FASTAPI_BASE_URL}/delete-user-data", params={"session_id": session_id})
    await update.message.reply_text(response.json().get("result", "Error"))


async def ingest_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /ingest <URL>")
        return
    url = context.args[0]
    session_id = str(update.effective_chat.id)
    response = requests.post(f"{FASTAPI_BASE_URL}/ingest", params={"url": url, "session_id": session_id})
    await update.message.reply_text(response.json().get("result", "Error"))


async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    session_id = str(update.effective_chat.id)
    response = requests.post(f"{FASTAPI_BASE_URL}/ask", params={"query": query, "session_id": session_id})
    result = response.json()
    await update.message.reply_text(result.get("response", "Error answering your question."))

# === MAIN ===
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("delete", delete_all))
    app.add_handler(CommandHandler("ingest", ingest_url))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
