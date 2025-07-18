from yourapp.logging_formatter import CustomJsonFormatter

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': CustomJsonFormatter,
            'fmt': '%(timestamp)s %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
        # If you want to log to a file
        # 'file': {
        #     'class': 'logging.FileHandler',
        #     'formatter': 'json',
        #     'filename': 'myproject.log',
        # },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'http_logger': {  # Our custom logger
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}



MIDDLEWARE = [
    'yourapp.middleware.RequestResponseLoggingMiddleware',
    # ...other middleware
]
