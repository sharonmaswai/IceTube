# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import *
from decouple import config
from datetime import datetime
cl = MpesaClient()

def index(request):

	return HttpResponse('Welcome to the home of daraja APIs')

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)

def stk_push_success(request):
	phone_number = config('LNM_PHONE_NUMBER')
	amount = '1'
	account_reference = 'ABC001'
	transaction_desc = 'Description'
	callback_url = 'https://darajambili.herokuapp.com/express-payment'
	r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0724869317'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response.text)

def stk_push_callback(request):
        data = request.body
        # You can do whatever you want with the notification received from MPESA here.