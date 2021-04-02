import requests
import json
from mongoengine import *
import time
import pytz
import datetime
from datetime import datetime

########## DATABASE START ##########
DB_URL = ""
connect(host=DB_URL)
print("Connected to Database")

class UpdatedTaxiAvailability_2nd(Document):
    datetime = ComplexDateTimeField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)
    longitute = FloatField(required=True)
    latitute = FloatField(required=True)

## DATABASE END ##########

## TELEGRAM BOT ##########
chat_id =  # Tele ID of the Receiver 
api_token = '1471285291:AAG8BC7qpgJoDcVpy5nTcgDOEaX4sfOoxCU'
base_url = 'https://api.telegram.org/bot{}/'.format(api_token)

sendMsg_url = base_url + 'sendMessage'

def send_msg(chat_id, msg_text):
	params = {'chat_id':chat_id, 'text':msg_text}
	r = requests.post(sendMsg_url,params=params)
	return None

## TELEGRAM BOT END##########

while True:
    if __name__ == "__main__":

        try:
            #Authentication parameters
            headers = {'AccountKey' : '', 'accept' : 'application/json'}

            # TAXI AVAILABILITY | TAXI COORDINATES - by Time and Date (source: Data.Gov)
            api_taxi_availability = requests.get('https://api.data.gov.sg/v1/transport/taxi-availability')
            all_taxi_coordinates_list = api_taxi_availability.json()['features'][0]['geometry']['coordinates']
            # print(all_taxi_coordinates_list)
            print('Successfully Retrieved')

            # SAVE TO DB
            for taxi in all_taxi_coordinates_list:
                UpdatedTaxiAvailability_2nd(
                    datetime = datetime.now(),
                    date = str(datetime.now().date()),
                    time = str(datetime.now().time()),
                    longitute = taxi[0],
                    latitute = taxi[1],
                ).save()

            print('Successfully Saved to Taxi Availability Database')
            print(datetime.now())

        except Exception as ErrorMessage:
            print('ERROR MESSAGE: ', ErrorMessage)
            msg_text = 'Taxi Availability Error'
            send_msg(chat_id, msg_text)
            
        finally:
            time.sleep(300) # 5 minute pause