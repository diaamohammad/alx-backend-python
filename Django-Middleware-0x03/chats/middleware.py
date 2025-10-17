# chats/middleware.py
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden, JsonResponse

# 1️⃣ Logging User Requests
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
        with open("requests.log", "a") as log_file:
            log_file.write(log_message)
        response = self.get_response(request)
        return response


# 2️⃣ Restrict Chat Access by Time
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # يمنع الدخول خارج الوقت المحدد (بين 6PM و 9PM)
        if current_hour < 18 or current_hour > 21:
            return HttpResponseForbidden("Access restricted during off hours.")
        return self.get_response(request)


# 3️⃣ Detect and Block Offensive Language (Rate Limiting)
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_messages = {}

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        now = datetime.now()

        if request.method == 'POST' and '/messages' in request.path:
            if ip not in self.ip_messages:
                self.ip_messages[ip] = []

            # نحذف الطلبات اللي عدت عليها أكتر من دقيقة
            self.ip_messages[ip] = [t for t in self.ip_messages[ip] if now - t < timedelta(minutes=1)]

            if len(self.ip_messages[ip]) >= 5:
                return JsonResponse({"error": "Rate limit exceeded. Try again later."}, status=429)

            self.ip_messages[ip].append(now)

        return self.get_response(request)


# 4️⃣ Enforce Chat User Role Permissions
class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        # يمنع المستخدمين غير admin أو moderator من دخول صفحات معينة
        if '/chats/' in request.path:
            if not user.is_authenticated or getattr(user, 'role', None) not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return self.get_response(request)
class RolepermissionMiddleware