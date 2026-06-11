# 🌤️ Weather Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge&logo=openweathermap&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

Telegram-бот для получения актуальной погоды в любом городе мира 🌍

</div>

---

## ✨ Возможности

- 🌡️ Температура и ощущаемая температура
- 💧 Влажность воздуха
- 💨 Скорость и направление ветра
- 👁️ Видимость
- 🌍 Поддержка любого города мира
- 🇷🇺 Описание погоды на русском языке
- ⌨️ Удобная клавиатура с кнопками

---

## 📸 Демо

```
👋 Привет, Леонид!
Я помогу узнать погоду в любом городе мира 🌍

> Ташкент

☀️ Погода в Tashkent, UZ

🌡️ Температура: 32°C (ощущается как 30°C)
💧 Влажность: 25%
💨 Ветер: 3 м/с, направление СВ
👁️ Видимость: 10 км
📋 Описание: Ясно
```

---

## 🛠️ Технологии

| Технология | Назначение |
|------------|-----------|
| Python 3.11+ | Язык программирования |
| aiogram 3.x | Фреймворк для Telegram Bot API |
| aiohttp | Асинхронные HTTP-запросы |
| OpenWeatherMap API | Данные о погоде |
| python-dotenv | Управление переменными окружения |

---

## 🚀 Запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/xmiroxxx142/weather-bot.git
cd weather-bot
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Создать файл `.env`

```bash
cp .env.example .env
```

Заполни `.env`:

```env
BOT_TOKEN=твой_токен_от_BotFather
WEATHER_API_KEY=твой_ключ_от_openweathermap.org
```

**Где взять ключи:**
- `BOT_TOKEN` → [@BotFather](https://t.me/BotFather) в Telegram
- `WEATHER_API_KEY` → [openweathermap.org](https://openweathermap.org/api) (бесплатно)

### 4. Запустить

```bash
python bot.py
```

---

## 📁 Структура проекта

```
weather-bot/
├── bot.py            # Основной файл бота
├── requirements.txt  # Зависимости
├── .env.example      # Пример конфига
├── .env              # Конфиг (не в git!)
├── .gitignore
└── README.md
```

---

## 👨‍💻 Автор

**Леонид** — [@xmiroxxx142](https://github.com/xmiroxxx142)

---

## 📄 Лицензия

MIT
