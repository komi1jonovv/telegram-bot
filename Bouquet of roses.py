from aiogram import Bot, Dispatcher, executor, types


BOT_TOKEN = "7933453658:AAHkGQDm9XawsL7IHdUTdgBFO1eddON0MSM"


ADMIN_ID = 5321852973


keywords = ["buyurtma", "ilhom", "xarid", "yordam", "/start", "/help"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(content_types=types.ContentType.TEXT)
async def filter_message(message: types.Message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else "Username mavjud emas"


    text = message.text
    if text.startswith('/start'):

        text = text.split('@')[0]
        if message.chat.type == "supergroup":

            if '@' in text:
                text = text.split('@')[0]

    if any(keyword in text.lower() for keyword in keywords):
        try:
            await bot.send_message(
                chat_id=ADMIN_ID,
                text=(
                    f"Yangi xabar:\n"
                    f"👤 Kimdan: {first_name}\n"
                    f"🆔 ID: {user_id}\n"
                    f"📛 Username: {username}\n"
                    f"✉️ Xabar: {text}"
                )
            )
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")


if __name__ == '__main__':
    executor.start_polling(dp)