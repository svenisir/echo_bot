import asyncio

from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers
from config_data.config import load_config, Config


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем данные конфигурации бота
    config: Config = load_config()

    # Создаём экземпляры класса бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Подключаем routers к root router 
    dp.include_router(router=user_handlers.router)
    dp.include_router(router=other_handlers.router)

    # Удаляем накопившиеся updates и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
