import logging


def get_logger() -> logging.Logger:
    """Функция настройки логирования и создание логгера"""

    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования (INFO и выше)
        format='%(asctime)s - %(levelname)s - %(message)s'  # Формат вывода
    )
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    return logger
