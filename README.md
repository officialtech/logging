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


