import os
from telegram import Update
from telegram.ext import Application

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
