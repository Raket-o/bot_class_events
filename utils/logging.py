import logging
import logging.config
import sys
# from log_setup import dict_config


# logging.basicConfig(
#     # level=logging.DEBUG
#     level=logging.DEBUG
# )

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "{level: %(levelname)s | "
                      "logger: %(name)s | "
                      "time: %(asctime)s | "
                      "line №: %(lineno)s | "
                      "message: %(message)s}"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
        },
        # "file_info_utils": {
        #     "class": "logging.handlers.TimedRotatingFileHandler",
        #     "filename": "./logs/info.log",
        #     "when": "H",
        #     "interval": 10,
        #     "backupCount": 1,
        #     "level": "DEBUG",
        #     "encoding": "utf8",
        #     "formatter": "base"
        # },
        "file_errors_utils": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "./logs/err.log",
            "when": "H",
            "interval": 10,
            "backupCount": 1,
            "level": "ERROR",
            "encoding": "utf8",
            "formatter": "base"
        },
    },
    "loggers": {
        "logger_main": {
            "level": "DEBUG",
            "handlers": ["console", "file_errors_utils"]
        },
        "logger_main.logger_handler_high_low_price": {
            "level": "DEBUG",
            "handlers": ["console", "file_errors_utils"]
        },
        "logger_main.get_meta_data": {
            "level": "DEBUG",
            "handlers": ["console", "file_errors_utils"]
        }
    }
}



logging.config.dictConfig(dict_config)

logger_root = logging.getLogger('')
logger_root.setLevel(logging.DEBUG)

# logger = logging.getLogger("logger_bot")
