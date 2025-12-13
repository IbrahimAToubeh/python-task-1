import datetime

class AuditMixin:
    def log_action(self, action, details):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {action}: {details}")
