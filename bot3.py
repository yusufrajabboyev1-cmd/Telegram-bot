from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ""

# Asosiy menyu tugmalari
main_buttons = [
    ["👤 Men haqimda", "📚 Ko‘nikmalarim"],
    ["💼 Portfolio", "📞 Aloqa"]
]

main_keyboard = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)

# Men haqimda menyusi
about_buttons = [["🔙 Orqaga"]]
about_keyboard = ReplyKeyboardMarkup(about_buttons, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Tugmalardan birini tanlang 👇",
        reply_markup=main_keyboard
    )

# Tugmalar bosilganda ishlaydigan funksiya
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 Men haqimda":
        await update.message.reply_text(
            "👤 Men haqimda:\n\nIsm: Rustam\nKasb: Dasturchi\nQiziqishlar: Python, Telegram botlar",
            reply_markup=about_keyboard
        )

    elif text == "🔙 Orqaga":
        await update.message.reply_text(
            "Asosiy menyu:",
            reply_markup=main_keyboard
        )

    elif text == "📚 Ko‘nikmalarim":
        await update.message.reply_text(
            "📚 Ko‘nikmalarim:\n- Python\n- Telegram bot\n- HTML/CSS\n- Git/GitHub",
            reply_markup=main_keyboard
        )

    elif text == "💼 Portfolio":
        await update.message.reply_text(
            "💼 Portfolio:\n1) Telegram bot\n2) Web sayt\n3) Mini o‘yin",
            reply_markup=main_keyboard
        )

    elif text == "📞 Aloqa":
        await update.message.reply_text(
            "📞 Aloqa:\nTelegram: @username\nEmail: example@mail.com",
            reply_markup=main_keyboard
        )

    else:
        await update.message.reply_text(
            "Tugmalardan birini tanlang 👇",
            reply_markup=main_keyboard
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

app.run_polling()
