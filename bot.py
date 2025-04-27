from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao benvenuto su FKAIRPODS, per ulteriori dettagli su acquisti ed altro scrivi a questo contatto e ti risponderanno 24/7 ✅⬇️\n\n@glockloves"
    )

app = ApplicationBuilder().token('7888458655:AAHVUhc0qJCuAyMDOG84EgTT8pu1DuQE8Tc').build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
