import logging


def get_logger() -> logging.Logger:
    """Функция настройки логирования и создание логгера"""

    # Настройка базовой конфигурации логирования
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования (INFO и выше)
        format='%(asctime)s - %(levelname)s - %(message)s'  # Формат вывода
    )

    # Создание логгера с именем текущего модуля
    logger = logging.getLogger(__name__)

    # Создание обработчика для записи логов в файл "app.log" с кодировкой UTF-8
    file_handler = logging.FileHandler('fastapi_app', encoding='utf-8')

    # Добавление обработчика к логгеру
    logger.addHandler(file_handler)

    # Возврат настроенного логгера
    return logger
