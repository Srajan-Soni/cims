
from random import randrange
from twilio.rest import Client

import requests

from home.models import City

import json

def reCaptchaTest(request):
    grecapresp = request.POST.get('g-recaptcha-response')
    secretkey = '6Lc1r9waAAAAAHqwW1Exk7eo4SwCU8qYjnh3Ak1X'

    url = 'https://www.google.com/recaptcha/api/siteverify'

    postparams = {'secret': secretkey, 'response': grecapresp}

    resp = requests.post(url, data=postparams)

    respdict = json.loads(resp.text)

    return respdict['success']


def prepareCityList():
    cities = City.objects.all()
    
    cityList = []
    for city in cities:
        cityList.append((city.id, city.city+' ('+city.state.state+')'))

    return cityList

def collectAllCities():
    cities = City.objects.all()
    cityList = []
    for city in cities:
        #city = City(id=city.id, city.city+' ('+city.state.state+')'))
        cityList.append(city)

    return cityList

def sendOTP(request):
    contact = request.GET.get('contact')
    otp = randrange(1111,9999)
    print(otp, '++++++++++++++++++++ #################')
    request.session['otp'] = otp
    
    account_sid = 'AC301e7476bc36ad87fb2ce645b2131daf'
    auth_token = '7eb25be5046d507b9c63c9e5a661260d'
    client = Client(account_sid, auth_token)
     
    
    message = client.messages \
                    .create(
                        body="Welcome to ISRDC. Your OTP: "+str(otp),
                        from_='+16502036946',
                        to='+91'+contact
                    )

    return message.status