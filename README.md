# 🎮 PUBG Copilot — умный игровой ассистент

PUBG Copilot — это продвинутый Telegram‑бот, созданный для игроков PUBG Mobile.  
Он помогает с:
- анализом оружия  
- советами по картам  
- генерацией никнеймов  
- объяснением титулов  
- поиском тиммейтов  
- ИИ‑чатом на базе Google Gemini  

Бот работает быстро, стабильно и полностью оптимизирован под мобильную разработку.

---

## 🚀 Возможности

### 🧠 ИИ‑чат (Gemini)
- отвечает как Microsoft Copilot  
- даёт советы по PUBG  
- анализирует стиль игры  
- объясняет механики  

### 🔫 Оружие
- характеристики  
- лучшие обвесы  
- советы по использованию  

### 🗺 Карты
- лучшие места для лута  
- ротации  
- советы по позициям  

### 🏆 Титулы PUBG
- условия получения  
- скрытые требования  
- лайфхаки  

### 🎭 Генератор никнеймов
- агрессивные  
- аниме  
- PUBG‑стиль  
- минимализм  
- арабские  
- киберспорт  

### 🤝 Матчмейкинг
- заполнение профиля  
- очередь поиска  
- автоматический подбор тиммейтов  

---

## 📁 Структура проекта

```
pubg-copilot/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── bot/
│   ├── __init__.py
│   │
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py
│   │   ├── menu.py
│   │   ├── advice.py
│   │   ├── weapons.py
│   │   ├── maps.py
│   │   ├── ai_chat.py
│   │   ├── matchmaking.py
│   │   ├── nicknames.py
│   │   └── titles.py
│   │
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── main_menu.py
│   │   └── matchmaking_menu.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_engine.py
│   │   ├── pubg_logic.py
│   │   ├── titles_engine.py
│   │   └── nickname_engine.py
│   │
│   └── database/
│       ├── __init__.py
│       ├── db.py
│       ├── models.py
│       └── matchmaking.py
│
└── (локально, НЕ в GitHub)
    ├── .env
    └── database.db
```

---

## 🔧 Установка

### 1. Клонируй проект

```bash
git clone https://github.com/username/pubg-copilot.git
cd pubg-copilot
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Создай `.env` (НЕ пушить в GitHub!)

```
BOT_TOKEN=твой_токен_бота
GEMINI_API_KEY=твой_ключ_от_Google_AI_Studio
```

### 4. Запусти бота

```bash
python main.py
```

### 5. ОБЬЯЗАТЕЛЬНО УПОМЯНУТЬ НАШУ КОМПАНИЮ ЕСЛИ КОПИРУЕТЕ!!
---

## ☁️ Деплой на Koyeb

1. Залей проект на GitHub  
2. Создай сервис на Koyeb  
3. В разделе **Environment Variables** добавь:

```
BOT_TOKEN=...
GEMINI_API_KEY=...
```

4. Запусти деплой  
5. Бот работает 24/7


---

## 🛡 Безопасность

- `.env` всегда в `.gitignore`  
- ключи хранятся только в переменных окружения  
- база данных не пушится в GitHub  

---

## 📜 Лицензия

MIT — можно использовать, модифицировать и развивать.

---

## 💬 Автор

Разработано Компанией: IT_Company  — профессиональным Telegram‑бот девелопером и создателем PUBG Copilot Ecosystem.
