
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from game_api import fetch_cr_stats, fetch_coc_stats, fetch_bs_stats
from title_generators import format_clash_royale, format_clash_of_clans, format_brawl_stars

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        game = context.args[0].lower()
        tag = context.args[1]
        if game == "cr":
            stats = fetch_cr_stats(tag)
            title = format_clash_royale(stats)
        elif game == "coc":
            stats = fetch_coc_stats(tag)
            title = format_clash_of_clans(stats)
        elif game == "bs":
            stats = fetch_bs_stats(tag)
            title = format_brawl_stars(stats)
        else:
            title = "❌ Unknown game type. Use cr, coc, or bs."
        await update.message.reply_text(title)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("analyze", analyze))
    app.run_polling()
