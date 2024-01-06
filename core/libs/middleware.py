import logging
import time
from datetime import datetime
logger = logging.getLogger(__name__)

class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response_ms = duration * 1000
        # response_data = response.data
        response_data = getattr(response, "data", "")
        user = str(getattr(request, 'user', ''))
        method = str(getattr(request, 'method', '')).upper()
        status_code = str(getattr(response, 'status_code', ''))
        request_path = str(getattr(request, 'path', ''))
        now = datetime.strftime(datetime.now(), "%Y-%m-%d %HH:%MM:%SS")
        # request_data = str(getattr(request, 'data', 'aefasdf'))
        # import ipdb; ipdb.set_trace()
        # request_data = request.body or None
        logger.info({
                        # "message": "*****SLOW RESPONSE****",
                        "timestamp": now,
                        "path": request_path,
                        "response_time": str(response_ms) + " ms",
                        "method": method,
                        "user": user,
                        "status_code": status_code,
                        "response_data": response_data
                        # "request_data": request_data
                        })
        return response