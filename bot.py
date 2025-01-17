from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Токен вашего бота
TOKEN = '8107768907:AAGf3YmniraJ5PEvUvfrzJENTDxahISHdQ4'


# Функция для обработки команды /start
async def start(update: Update, context):
    menu_text = "<b>MENU</b>"
    keyboard = [
        [InlineKeyboardButton("📊 Arbitrage", callback_data='arbitrage')],
        [InlineKeyboardButton("🔗 Referral Program", callback_data='referral_program')],
        [InlineKeyboardButton("⚙️ Settings", callback_data='settings')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(menu_text, parse_mode='HTML', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(menu_text, parse_mode='HTML', reply_markup=reply_markup)


# Функция для команды /arbitrage
async def arbitrage(update: Update, context):
    text = "<b>Choose type:</b>"
    keyboard = [
        [InlineKeyboardButton("🔽 Triangular", callback_data='triangular')],
        [InlineKeyboardButton("🔄 Inter Exchange", callback_data='inter_exchange')],
        [InlineKeyboardButton("< Back", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)


# Функция для команды /referral_program
async def referral_program(update: Update, context):
    user_id = update.effective_user.id
    referral_link = f"https://t.me/ArbitrageScreeenerBot?start={user_id}"
    text = (
        "🎁 <b>INVITE USERS AND GET REWARDS!</b>\n\n"
        "From each purchase of your referral you get <b>50%</b>\n"
        "You have invited: <b>0</b>\n"
        "Earned: <b>$0</b>\n\n"
        f"👇 Use the link below for an invitation:\n"
        f"<a href='{referral_link}'>{referral_link}</a>"
    )
    keyboard = [[InlineKeyboardButton("< Back", callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)


# Функция для команды /settings
async def settings(update: Update, context):
    text = "<b>This feature will be available after payment.</b>"
    keyboard = [[InlineKeyboardButton("< Back", callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)


# Функция для кнопки < Back (Main Menu)
async def main_menu(update: Update, context):
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await start(update, context)

# Функция для кнопки Triangular
async def triangular(update: Update, context):
    text = (
        "🎁 <b>To use the FULL SUBSCRIPTION (INTER-EXCHANGE and TRIANGULAR screener) you need to pay a subscription.</b>\n\n"
        "<b>PRICE LIST:</b>\n"
        "      1 month - 50$\n"
        "      3 months - 100$ (-33%)\n"
        "      6 months - 150$ (-50%)\n"
        "      1 year - 200$ (-60%)\n"
        "      FOREVER - 400$\n\n"
        "<b>HOW TO PAY?</b>\n\n"
        "<code>0x960c8ddb5b6d5026c88615c42499ba8ce92e976c</code>\n"
        "USDT. Network - BSC (BEP20)\n\n"
        "<code>TXaRxKTb35yryUNsvGpAd7d2jGqdrcPRVy</code>\n"
        "USDT. Network - Tron (TRC20)\n\n"
        "After that you must notify support about the payment. Send a screenshot of the transaction from your exchange/wallet or a transaction hash."
    )
    keyboard = [[InlineKeyboardButton("< Back", callback_data='arbitrage')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)


# Основной код для запуска бота
app = ApplicationBuilder().token(TOKEN).build()

# Обработчики команд и кнопок
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", start))
app.add_handler(CommandHandler("arbitrage", arbitrage))
app.add_handler(CommandHandler("referral_program", referral_program))
app.add_handler(CommandHandler("settings", settings))
app.add_handler(CallbackQueryHandler(main_menu, pattern='^main_menu$'))
app.add_handler(CallbackQueryHandler(arbitrage, pattern='^arbitrage$'))
app.add_handler(CallbackQueryHandler(referral_program, pattern='^referral_program$'))
app.add_handler(CallbackQueryHandler(settings, pattern='^settings$'))
app.add_handler(CallbackQueryHandler(triangular, pattern='^triangular$'))  # <-- Перемещено сюда!

# Запуск бота
print("Bot is running...")
app.run_polling()

