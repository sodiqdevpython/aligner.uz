from .models import APIToken

def get_least_used_token():
    token = APIToken.objects.filter(is_active=True).order_by("usage_count").first()
    return token