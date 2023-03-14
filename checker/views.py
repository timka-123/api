from os import environ

from django.http import JsonResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from requests import post
from dotenv import load_dotenv

from .models import License

load_dotenv()

base_url = f"https://api.telegram.org/bot{environ.get('TELEGRAM_TOKEN')}"


def check_license(request: HttpRequest):
    login = request.headers['login']
    token = request.headers['token']
    try:
        data = License.objects.get(login=login, token=token)
    except ObjectDoesNotExist:
        post(
            url=f"{base_url}/sendMessage",
            data={
                'chat_id': 1605007235,
                'text': f"""<strong>
❌ Новая попытка проверки лицензии!

Данные авторизации:
Login: <code>{login}</code>
Token: <code>{token}</code>
</strong>""",
                'parse_mode': 'HTML'
            }
        )
        return JsonResponse({
            'status': 'error',
            'message': 'Login or token invalid'
        })
    post(
        url=f"{base_url}/sendMessage",
        data={
            'chat_id': 1605007235,
            'text': f"""<strong>
✅ Новая попытка проверки лицензии!

Данные авторизации:
Login: <code>{login}</code>
Token: <code>{token}</code>
</strong>""",
                'parse_mode': 'HTML'
        }
    )
    return JsonResponse({
        'status': 'ok'
    })
