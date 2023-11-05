# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:11:07 2023

@author: xtian
"""

from twilio.rest import Client

def make_phone_call():
    account_sid = 'AC78e0bb26bf1d0364d1b46271535f15e7'
    auth_token = 'd10407d42246d586f4eb268d8b651a3f'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>¡El entrenamiento ha finalizado!</Say></Response>',
        to='+51 986 295 558',    # Tu número de teléfono con código de país
        from_='+13203628612'  # Tu número de Twilio
    )

# Al final de tu script de entrenamiento:
# make_phone_call()


from twilio.rest import Client

def send_sms_notification():
    account_sid = 'AC78e0bb26bf1d0364d1b46271535f15e7'
    auth_token = 'd10407d42246d586f4eb268d8b651a3f'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="¡El entrenamiento ha finalizado!",
                        from_='+13203628612',  # Tu número de Twilio
                        to='+51 986 295 558'     # Tu número de teléfono
                    )

# Tu script de entrenamiento ...

# Al final del script:
# send_sms_notification()  # o send_whatsapp_notification() o make_phone_call()


from twilio.rest import Client

#Sincronizar con whatsapp: enviar whatsapp message to your whatsapp number +14155238886: "join sing-shine"
'''https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1'''

def send_whatsapp_notification():
    account_sid = 'AC78e0bb26bf1d0364d1b46271535f15e7'
    auth_token = 'd10407d42246d586f4eb268d8b651a3f'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="¡El entrenamiento ha finalizado!",
                        from_='whatsapp:+14155238886',  # Número de Twilio para WhatsApp
                        to='whatsapp:+51986295558'       # Tu número de WhatsApp
                    )

send_whatsapp_notification()