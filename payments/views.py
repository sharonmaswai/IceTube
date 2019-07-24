from django.shortcuts import render
from pympesa import Pympesa
import pympesa

# Create your views here.

response = pympesa.oauth_generate_token(
   '''DRq4b3D5tNWw4Q3uUUiYQLCgabKNlZir,bDnSilPbQIidgcrM
).json() '''
"access_token"=response.get("x0Bng5LDe75F6G8grgm1AwSwOdJ3")

mpesa_client.lipa_na_mpesa_online_payment(
    BusinessShortCode="600000",
    Password="xxxxx_yyyy_zzz",
    TransactionType="CustomerPayBillOnline",
    Amount="100",
    PartyA="254708374149",
    PartyB="600000",
    PhoneNumber="254708374149",
    CallBackURL="https://your-app/callback",
    AccountReference="ref-001",
    TransactionDesc="desc-001"
    )