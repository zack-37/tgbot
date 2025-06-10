import os
import logging
import asyncio
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Отключаем подробные логи python-telegram-bot и urllib3
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram.vendor.ptb_urllib3.urllib3").setLevel(logging.WARNING)
logging.getLogger("telegram.ext._application").setLevel(logging.WARNING)
logging.getLogger("telegram.ext._updater").setLevel(logging.WARNING)
logging.getLogger("telegram.bot").setLevel(logging.WARNING)
logging.getLogger("telegram.request").setLevel(logging.WARNING)
logging.getLogger("telegram.ext._extbot").setLevel(logging.WARNING)

BOT_TOKEN = os.environ['BOT_TOKEN']
ALLOWED_USERS = set(map(int, os.environ.get("ALLOWED_USERS", "").split(",")))

def is_allowed(user_id: int) -> bool:
    return not ALLOWED_USERS or user_id in ALLOWED_USERS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_allowed(user_id):
        await update.message.reply_text(f"🚫 Доступ закрыт. Ваш user id: {user_id}")
        return
    await update.message.reply_text("👋 Привет! Это заготовка Telegram-бота. Добавьте свой функционал.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 *Возможности бота:*\n"
        "/help — показать это сообщение\n"
        "\n"
        "💬 Просто напишите что-нибудь — бот ответит шаблонным сообщением."
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    logger.info(f"User {user_id} wrote: {text}")
    if not is_allowed(user_id):
        await update.message.reply_text(f"🚫 Доступ закрыт. Ваш user id: {user_id}")
        return

    await update.message.reply_text("🔎 Бот-заготовка: здесь будет ваш ответ.")

def main():
    logger.info("Bot starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    commands = [
        BotCommand("help", "Показать справку"),
    ]
    asyncio.get_event_loop().run_until_complete(app.bot.set_my_commands(commands))

    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Application started")
    app.run_polling()

if __name__ == "__main__":
    main()