import threading
import asyncio
from bot import main as bot_main
import server

# Запускаем Flask в отдельном потоке
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    server.app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    asyncio.run(bot_main())
