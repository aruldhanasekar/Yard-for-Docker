import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
    ]
)


def get_logger(name):
    return logging.getLogger(name)


