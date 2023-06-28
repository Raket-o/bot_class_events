# import logging
# import sys
# import string
# import requests
#
#
# # class CustomCalcHandler(logging.Handler):
# #
# #     def __init__(self, file_name, mode='a'):
# #         super().__init__()
# #         self.file_name = file_name
# #         self.mode = mode
# #
# #     def emit(self, record: logging.LogRecord) -> None:
# #         message = self.format(record)
# #         if record.levelno == 40:
# #             with open('./logs/calc_error.log', mode=self.mode) as file:
# #                 file.write(message + '\n')
# #         elif record.levelno == 10:
# #             with open('./logs/calc_debug.log', mode=self.mode) as file:
# #                 file.write(message + '\n')
#
#
# dict_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "base": {
#             "format": "{level: %(levelname)s | "
#                       "logger: %(name)s | "
#                       "time: %(asctime)s | "
#                       "line №: %(lineno)s | "
#                       "message: %(message)s}"
#         }
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "level": "DEBUG",
#             "formatter": "base",
#             "stream": sys.stdout
#         },
#         "file_info_utils": {
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "filename": "./logs/utils.log",
#             "when": "H",
#             "interval": 10,
#             "backupCount": 1,
#             "level": "INFO",
#             "encoding": "utf8",
#             "formatter": "base"
#         },
#         "file_debug_utils": {
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "filename": "./logs/utils.log",
#             "when": "H",
#             "interval": 10,
#             "backupCount": 1,
#             "level": "ERROR",
#             "encoding": "utf8",
#             "formatter": "base"
#         },
#     },
#     "loggers": {
#         "logger_bot": {
#             "level": "DEBUG",
#             "handlers": ["console", "file_info_utils", "file_debug_utils"]
#         }
#     }
# }





import logging
import sys
import string
import requests


class CustomHttpHandler(logging.Handler):
    def __init__(self, url: str, method: str = "POST"):
        self.url = url
        self.method = method
        super().__init__()

    def emit(self, record):
        _logEntry = {'time': f'{record.asctime}',
                    'line': f'{record.lineno}',
                    'logLevel': f'{record.levelname}',
                    'message': f'{record.message}'}

        try:
            if self.method == "POST":
                post_req = requests.post(self.url, data=_logEntry)
                # print('POST code=', post_req.status_code, 'POST TEXT=', post_req.text)
            elif self.method == "GET":
                get_req = requests.get(self.url, params=_logEntry)
                # print('GET code=', get_req.status_code, 'GET TEXT=', get_req.text)
        except requests.exceptions.ConnectionError:
            print('The server is unavailable')



class CustomCalcHandler(logging.Handler):

    def __init__(self, file_name, mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        if record.levelno == 40:
            with open('./logs/calc_error.log', mode=self.mode) as file:
                file.write(message + '\n')
        elif record.levelno == 10:
            with open('./logs/calc_debug.log', mode=self.mode) as file:
                file.write(message + '\n')


class ACIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        return not any(symb not in string.printable for symb in record.msg)


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
        "file": {
            "()": CustomCalcHandler,
            "level": "DEBUG",
            "formatter": "base",
            "file_name": "*.log",
            "mode": "a"
        },
        "file_info_utils": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "./logs/utils.log",
            "when": "H",
            "interval": 10,
            "backupCount": 1,
            "level": "INFO",
            "encoding": "utf8",
            "formatter": "base"
        },

        "http_post": {
            "()": CustomHttpHandler,
            "url": "http://127.0.0.1:5000/log",
            "method": "POST",
        },
        "http_get": {
            "()": CustomHttpHandler,
            "url": "http://127.0.0.1:5000/log",
            "method": "GET",
        },

    },
    "filters": {
        "myfilterACII": {
            "()": ACIIFilter,
        }
    },
    "loggers": {
        "logger_app": {
            "level": "DEBUG",
            "handlers": ["console", "file", 'http_post', "http_get"],
            "filters": ['myfilterACII'],
        },
        "logger_app.logger_unils": {
            "level": "INFO",
            "handlers": ['file_info_utils'],
            "filters": ['myfilterACII'],
        }
    },
}
