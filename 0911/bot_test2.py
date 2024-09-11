from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import random

API_KEY = '7520801855:AAFk_P_Q4wJ7G_cNn3Q9ysZuAjyJcq85LH4'  # 자신의 API 키로 교체하세요.

# 사용자 선택 상태를 저장할 변수
user_state = {}


# 기능 목록을 보여주는 함수
async def start(update: Update, context):
    user_id = update.effective_chat.id
    user_state[user_id] = None  # 초기화
    await context.bot.send_message(chat_id=user_id,
                                   text="원하는 기능을 선택하세요:\n1. 랜덤 숫자 생성기\n2. 가위바위보 게임\n3. 주사위 굴리기\n종료를 입력하면 다시 선택할 수 있습니다.")


# 사용자가 기능을 선택하면 그에 맞는 기능 실행
async def handle_message(update: Update, context):
    user_id = update.effective_chat.id
    user_msg = update.message.text.lower()

    if user_id not in user_state or user_msg == '종료':
        await start(update, context)  # 종료 시 다시 선택
    elif user_state[user_id] is None:
        if user_msg == '1':
            user_state[user_id] = '랜덤 숫자'
            await context.bot.send_message(chat_id=user_id, text="랜덤 숫자 생성기를 선택했습니다! 숫자를 생성합니다.")
            random_number = random.randint(1, 100)
            await context.bot.send_message(chat_id=user_id, text=f"랜덤 숫자: {random_number}")
        elif user_msg == '2':
            user_state[user_id] = '가위바위보'
            await context.bot.send_message(chat_id=user_id, text="가위, 바위, 보 중 하나를 선택하세요.")
        elif user_msg == '3':
            user_state[user_id] = '주사위'
            await context.bot.send_message(chat_id=user_id, text="주사위를 굴립니다.")
            dice_number = random.randint(1, 6)
            await context.bot.send_message(chat_id=user_id, text=f"주사위 결과: {dice_number}")
        else:
            await context.bot.send_message(chat_id=user_id, text="잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
    elif user_state[user_id] == '가위바위보':
        user_choice = user_msg
        bot_choice = random.choice(['가위', '바위', '보'])
        if user_choice in ['가위', '바위', '보']:
            if user_choice == bot_choice:
                result = "비겼습니다!"
            elif (user_choice == '가위' and bot_choice == '보') or (user_choice == '바위' and bot_choice == '가위') or (
                    user_choice == '보' and bot_choice == '바위'):
                result = "이겼습니다!"
            else:
                result = "졌습니다!"
            await context.bot.send_message(chat_id=user_id, text=f"봇: {bot_choice}\n결과: {result}")
        else:
            await context.bot.send_message(chat_id=user_id, text="가위, 바위, 보 중 하나를 입력하세요.")

    await context.bot.send_message(chat_id=user_id, text="종료를 입력하면 다시 기능을 선택할 수 있습니다.")


# 핸들러 설정
def main():
    application = Application.builder().token(API_KEY).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)

    application.add_handler(start_handler)
    application.add_handler(message_handler)

    # 봇 실행
    application.run_polling()


if __name__ == '__main__':
    main()
