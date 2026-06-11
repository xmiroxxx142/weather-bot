import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌤️ Погода по городу")],
        [KeyboardButton(text="ℹ️ О боте")],
    ],
    resize_keyboard=True
)

WEATHER_EMOJIS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "Haze": "🌫️",
}

def wind_direction(degrees: int) -> str:
    dirs = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    return dirs[round(degrees / 45) % 8]

async def get_weather(city: str) -> dict | None:
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ru",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_URL, params=params) as resp:
            if resp.status == 200:
                return await resp.json()
            return None

def format_weather(data: dict) -> str:
    city = data["name"]
    country = data["sys"]["country"]
    temp = round(data["main"]["temp"])
    feels = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].capitalize()
    condition = data["weather"][0]["main"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"].get("deg", 0)
    visibility = data.get("visibility", 0) // 1000

    emoji = WEATHER_EMOJIS.get(condition, "🌡️")

    return (
        f"{emoji} <b>Погода в {city}, {country}</b>\n\n"
        f"🌡️ Температура: <b>{temp}°C</b> (ощущается как {feels}°C)\n"
        f"💧 Влажность: <b>{humidity}%</b>\n"
        f"💨 Ветер: <b>{wind_speed} м/с</b>, направление {wind_direction(wind_deg)}\n"
        f"👁️ Видимость: <b>{visibility} км</b>\n"
        f"📋 Описание: {description}"
    )

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, <b>{message.from_user.first_name}</b>!\n\n"
        "Я помогу узнать погоду в любом городе мира 🌍\n"
        "Просто введи название города или нажми кнопку ниже.",
        parse_mode="HTML",
        reply_markup=main_keyboard
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📖 <b>Как пользоваться ботом:</b>\n\n"
        "• Напиши название города на любом языке\n"
        "• Или нажми кнопку <b>🌤️ Погода по городу</b>\n\n"
        "Примеры: <code>Ташкент</code>, <code>Moscow</code>, <code>London</code>",
        parse_mode="HTML"
    )

@dp.message(F.text == "ℹ️ О боте")
async def about(message: Message):
    await message.answer(
        "🤖 <b>Weather Bot</b>\n\n"
        "Показывает актуальную погоду по всему миру.\n\n"
        "⚙️ <b>Технологии:</b>\n"
        "• Python 3.11+\n"
        "• aiogram 3.x\n"
        "• OpenWeatherMap API\n"
        "• aiohttp\n\n"
        "👨‍💻 Автор: @xmiroxxx142\n"
        "📦 GitHub: github.com/xmiroxxx142/weather-bot",
        parse_mode="HTML"
    )

@dp.message(F.text == "🌤️ Погода по городу")
async def ask_city(message: Message):
    await message.answer("Введи название города 🏙️")

@dp.message()
async def handle_city(message: Message):
    city = message.text.strip()
    if len(city) < 2:
        await message.answer("Введи корректное название города.")
        return

    await message.answer("⏳ Ищу погоду...")

    data = await get_weather(city)
    if data:
        await message.answer(format_weather(data), parse_mode="HTML")
    else:
        await message.answer(
            f"❌ Город <b>{city}</b> не найден.\n"
            "Проверь название и попробуй ещё раз.",
            parse_mode="HTML"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
