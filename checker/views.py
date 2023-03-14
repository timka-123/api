from django.http import JsonResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from requests import post

from .models import License


base_url = f"https://api.telegram.org/bot6295880776:AAFuTGL9lTKaHjO3NapkWwWllTwSxvENPCo"


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
