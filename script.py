import requests
from twilio.rest import Client
from os import environ

account_sid =  environ['acct_key']#ACd8bdbb137ca4f402879f6a995f66eeb2 # replace this with yours
auth_token =  environ['auth_key']#20f570d963775e3168dd9d48170c3ba9 # replace this with yours
client = Client(account_sid, auth_token)

def send_message(message):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to='whatsapp:+919717423241'
    )
    return message

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "af8414c813mshfa68b005eced6a6p1d6a6fjsn16bfa57b4c34"
}

response = requests.request("GET", url, headers=headers).json()


def display_all():
    for each in response['countries_stat']:
        del each['region']
        print('\n')
        print('#######################################')
        print('\n')
        for key in each:
            print(key.upper(), ' : ', each[key])


