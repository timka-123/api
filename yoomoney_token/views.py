from os import environ

from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from dotenv import load_dotenv
from requests import post

# Create your views here.

load_dotenv()


def create_temp_token(request: HttpRequest):
    page = post(f"https://yoomoney.ru/oauth/authorize?client_id={environ.get('YOOMONEY_CLIENT_ID')}&response_type=code&redirect_uri=https://core.timka.space/yoomoney/callback/&scope=payment+account-info+operation-history+operation-details+payment-shop+payment-p2p+money-source")
    if page.status_code == 302:
        return redirect(page.json()['location'])
    return HttpResponse("<h1>Allow access to YooMoney</h1>")


def callback(request: HttpRequest, code: str):
    page = post(f"https://yoomoney.ru/oauth/token?code={code}&client_id={environ.get('YOOMONEY_CLIENT_ID')}&grant_type=authorization_code&redirect_uri=https://core.timka.space/yoomoney/success")
    try:
        return HttpResponse(f"<h1>{page.json()['error']}</h1>")
    except KeyError:
        return HttpResponse(f"<h1>{page.json()['access_token']}</h1>")
