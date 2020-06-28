import requests
from twilio.rest import Client

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "af8414c813mshfa68b005eced6a6p1d6a6fjsn16bfa57b4c34"
}

response = requests.request("GET", url, headers=headers).json()

result = []


def display_all():
    global result
    for each in response['countries_stat']:
        if each['country_name'].lower() == 'india':
            del each['region']
            result = str(each)

    return result


account_sid = "<Your account-sid>"
auth_token = "<Your auth_token>"
client = Client(account_sid, auth_token)


def func():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=display_all(),
        to='whatsapp:+919717423241')

    return message



