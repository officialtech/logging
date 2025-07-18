import logging
import uuid
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('http_logger')

class RequestResponseLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._log_id = str(uuid.uuid4())
        logger.info({
            "log_type": "request",
            "log_id": request._log_id,
            "method": request.method,
            "path": request.get_full_path(),
            "headers": dict(request.headers),
            "user": str(request.user) if hasattr(request, 'user') and request.user.is_authenticated else None,
        })

    def process_response(self, request, response):
        log_id = getattr(request, '_log_id', None)
        logger.info({
            "log_type": "response",
            "log_id": log_id,
            "status_code": response.status_code,
            "headers": dict(response.items()),
        })
        return response


