import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext
from model.goal import Tracking
from services.goal import check_goal

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
            "Hi! Use /set <url> <goal> to start tracking a product.")


async def check(context: CallbackContext):
    tracking = context.job.data

    price, goal_reached = check_goal(tracking)
    if goal_reached:
        context.bot.send_message(tracking.user_id,
                                 f"Price is {price}! Goal reached!")


async def track_product(update: Update,
                        context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_message.chat_id
    try:
        tracking = Tracking(chat_id, context.args[0], float(context.args[1]))
        context.job_queue.run_repeating(check, interval=60, data=tracking)

        await update.effective_message.reply_text(
                "Product URL and price set to track.")

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Usage: /set <ulr> <goal>")


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("set", track_product))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
