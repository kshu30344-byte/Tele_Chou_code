import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

BOT_TOKEN = 8843192101:AAGdvv6PQfN2JtfbZt54mmdiKBkJPr3wyNE 
bot = @Sun_pro_ly_bot.TeleBot(BOT_TOKEN)

# Stop Button ပြရန် Function
def get_stop_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🛑 Stop", callback_data="stop_process"))
    return markup

@bot.message_handler(commands=['start', 'check'])
def start_checker(message):
    msg = bot.send_message(
        message.chat.id, 
        "🎯 Starting Checker...", 
        reply_markup=get_stop_keyboard()
    )
    
    # ဥပမာ- Loop ပတ်ပြီး Data Update လုပ်ပြသည့် ပုံစံ
    hits = 0
    expired = 0
    
    for i in range(100):
        # ဒီနေရာမှာ မိမိ Code / Account စစ်ဆေးသည့် Logic ထည့်ရန်
        current_code = 785100 + i
        hits += 1 if i % 5 == 0 else 0
        expired += 1 if i % 5 != 0 else 0
        
        text = f"""
🎯 **Current Code:** `{current_code}`
🔥 **Hits:** {hits}
❌ **Expired:** {expired}
⚡ **Speed:** 8000 c/m

🔥 **Hit Codes:**
762737 🎫 : 1Hour
        """
        
        try:
            # Message ကို Live Update လုပ်ပေးခြင်း
            bot.edit_message_text(
                chat_id=message.chat.id, 
                message_id=msg.message_id, 
                text=text, 
                parse_mode="Markdown",
                reply_markup=get_stop_keyboard()
            )
        except Exception as e:
            pass
            
        time.sleep(2) # Speed ထိန်းရန်

@bot.callback_query_handler(func=lambda call: call.data == "stop_process")
def stop_callback(call):
    bot.answer_callback_query(call.id, "Stopped!")
    bot.edit_message_text("🛑 Process Stopped by User.", call.message.chat.id, call.message.message_id)

bot.infinity_polling()
