# logging
Complete Django logging solution that will produce logs in JSON formatting



## Install Requirements
```python
pip install python-json-logger
```

## Result
1. Now, every request and response will be logged to the console in JSON, like:
```json
{
  "timestamp": "2025-07-18T16:20:24.708Z",
  "levelname": "INFO",
  "name": "http_logger",
  "message": {
    "log_type": "request",
    "log_id": "bfc9f8f5-6a3d-4d0b-9b1c-...",
    "method": "GET",
    "path": "/api/example/",
    "headers": { ... },
    "user": "user@example.com"
  },
  "environment": "local-ras"
}
```

2. and for the response:
```json
{
  "timestamp": "2025-07-18T16:20:24.850Z",
  "levelname": "INFO",
  "name": "http_logger",
  "message": {
    "log_type": "response",
    "log_id": "bfc9f8f5-6a3d-4d0b-9b1c-...",
    "status_code": 200,
    "headers": { ... }
  },
  "environment": "local-ras"
}
```


## Log Integration with `Sentry`
- Open-source (you can self-host for free), also has a SaaS option.
- Specializes in error/exception tracking (not general log search, but great for stack traces, error context, alerting).
- Best for tracking exceptions, uncaught errors, performance monitoring.
- Not a full replacement for centralized search like ELK, but complements it.


#### How to integrate:
1. Install Sentry SDK:
```python
pip install sentry-sdk
```

2. Configure in `settings.py`:
```python
import sentry_sdk
sentry_sdk.init(
    dsn="your_sentry_dsn",  # get from your Sentry project
    traces_sample_rate=1.0,  # adjust as needed
    environment=os.getenv('DJANGO_ENV', 'local'),
)
```
- Sentry will auto-capture all unhandled Django errors/exceptions.
- You can also send custom logs/errors to Sentry.

