from pythonjsonlogger import jsonlogger
import datetime
import os

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['timestamp'] = datetime.datetime.utcnow().isoformat() + 'Z'
        log_record['environment'] = os.getenv('DJANGO_ENV', 'local-ras')  # or customize
        # Add more custom fields as needed
