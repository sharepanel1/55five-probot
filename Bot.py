from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from core.predictor import predict_next
from core.error_handler import ErrorHandler

error_handler = ErrorHandler()

def start(update: Update, context: CallbackContext):
    try:
        buttons = [
            [InlineKeyboardButton("🎯 Prediksi 1M", callback_data="prediksi_1m")],
            [InlineKeyboardButton("📈 Statistik", callback_data="stats")]
        ]
        update.message.reply_text(
            "🔥 55FIVE AI BOT siap!\nPilih menu:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        error_handler.critical_error(e)
