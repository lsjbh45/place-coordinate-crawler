import logging


class Logger():
    def __init__(self):
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
             '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        file_handler = logging.FileHandler('log.txt', encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)
