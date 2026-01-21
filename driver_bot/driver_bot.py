import requests
from aiogram import Bot, Dispatcher, types, F
import asyncio

BOT_TOKEN = "DRIVER_BOT_TOKEN"
SERVER_URL = "https://YOUR_RENDER_URL"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Salom! Siz haydovchisiz. /orders bilan buyurtmalarni ko'ring.")

@dp.message(F.text == "/orders")
async def orders(message: types.Message):
    response = requests.get(f"{SERVER_URL}/get_orders").json()
    if not response:
        await message.answer("Hozircha buyurtmalar yo'q.")
        return
    for o in response:
        await message.answer(f"Order ID: {o['id']}\nUser: {o['user_name']}\nQabul qilish uchun /take_{o['id']} bosing.")

@dp.message(F.text.startswith("/take_"))
async def take_order(message: types.Message):
    order_id = message.text.split("_")[1]
    requests.post(f"{SERVER_URL}/order_taken", json={"id": order_id})
    await message.answer(f"Buyurtma {order_id} sizga berildi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
