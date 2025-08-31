import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command 

# --- настройки ---
API_TOKEN = "8119552777:AAFNDZI9L_otshwsFWYJICDUKBT8HJ1Idi0"   # вставь токен из @BotFather
ADMIN_ID = 1032077865       # твой user_id из @userinfobot

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привітик, сонечко 💞  Ми дуже раді, що ти завітав і чекаємо на твої повідомлення 💋")
# ------------------ ТЕКСТ ------------------
@dp.message(F.text)
async def forward_text(message: types.Message):
    # 1️⃣ пересылаем админу
    await bot.send_message(
        ADMIN_ID,
        f"Сообщение от @{message.from_user.username or message.from_user.id}:\n{message.text}"
    )
    # 2️⃣ авто-ответ пользователю
    await message.answer("Дякуємо, що поділився з нами! Ми цінуємо твою відкритість та будемо чекати на наступні фото🥵💅 ")

# ------------------ ФОТО ------------------
@dp.message(F.photo)
async def forward_photo(message: types.Message):
    photo = message.photo[-1].file_id
    caption = message.caption if message.caption else ""
    # 1️⃣ пересылаем админу
    await bot.send_photo(
        ADMIN_ID,
        photo,
        caption=f"Фото от @{message.from_user.username or message.from_user.id}:\n{caption}"
    )
    # 2️⃣ авто-ответ пользователю
    await message.answer("Дякуємо, що поділився з нами! Ми цінуємо твою відкритість та будемо чекати на наступні фото🥵💅 ")

# ------------------ запуск бота ------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



