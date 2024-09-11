from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler

API_KEY = '7520801855:AAFk_P_Q4wJ7G_cNn3Q9ysZuAjyJcq85LH4'

# 봇 초기화
application = Application.builder().token(API_KEY).build()

# echo 함수 정의
async def echo(update: Update, context):
    user_id = update.effective_chat.id
    user_msg = update.message.text
    print(f"{user_id}, {user_msg}")
    await context.bot.send_message(chat_id=user_id, text=user_msg)  # await 사용

# 핸들러 설정
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
application.add_handler(echo_handler)

# 봇 실행
if __name__ == '__main__':
    application.run_polling()
