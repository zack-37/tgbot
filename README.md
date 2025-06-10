# 🤖 Telegram Bot Starter Template

## 🚀 Overview

This project is a simple lightweight template for a Telegram bot written in Python using the [python-telegram-bot](https://python-telegram-bot.org/) library.  
It is ready to run in Docker and easily configurable for your own logic. Also it doesnot spam requests it's procceding.

## 📁 Project Structure

```
tgbot
├── src
│   └── bot.py              # Main bot implementation
├── Dockerfile              # Dockerfile to build the bot image
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables example file
└── README.md               # Project documentation
```

## 🛠️ Requirements

- Docker
- Docker Compose

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Configure Environment Variables

Create a `.env` file, using `.env.example` file, in the project root with your Telegram bot token and allowed user IDs:

```
BOT_TOKEN=your_bot_token
ALLOWED_USERS=123456789,987654321
```

### 3️⃣ Build and Run the Bot

Use Docker Compose to build and start the bot:

```bash
docker-compose build && docker-compose up -d && docker-compose logs -f
```

### 4️⃣ Interact with the Bot

Open Telegram and send a message to your bot.  
By default, the bot responds to `/help` and any text message.

## 📝 Customization

- Add your logic to `src/bot.py`.
- Update dependencies in `requirements.txt` as needed.

## 🧹 Useful Commands

- 🛑 **Stop the bot:**  
  `docker-compose down`

- 🔄 **Rebuild after changes big changes:**  
  `docker-compose up --build`

- 🔄 **Rebuild after changes small adjustments inside src/bot.py:**  
  `docker-compose restart`

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ for Telegram bot developers!
