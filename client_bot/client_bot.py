import requests
from aiogram import Bot, Dispatcher, types, F
import asyncio

BOT_TOKEN = "CLIENT_BOT_TOKEN"
SERVER_URL = "https://YOUR_RENDER_URL"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Salom! Taksi chaqirish uchun /order bosing.")

@dp.message(F.text == "/order")
async def order(message: types.Message):
    order_data = {
        "id": str(message.from_user.id),
        "user_name": message.from_user.full_name
    }
    requests.post(f"{SERVER_URL}/new_order", json=order_data)
    await message.answer("Sizning buyurtmangiz qabul qilindi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
