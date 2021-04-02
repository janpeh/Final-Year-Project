import requests
import json
from mongoengine import *
from datetime import datetime
import pytz
import time
import datetime

########## DATABASE START ##########
DB_URL = ""
connect(host=DB_URL)
print("Connected to Database")

class NewBusArrival_18051_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()

class NewBusArrival_18059_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()

class NewBusArrival_18159_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()

class NewBusArrival_18151_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()

class NewBusArrival_18121_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()

class NewBusArrival_18129_2nd(Document):
    date_time = ComplexDateTimeField(required=True) #of the data being stored
    date = StringField(required=True)
    time = StringField(required=True)
    bus_number = StringField(required=True)
    operator = StringField(required=True)

    #First Next Bus Details
    first_next_bus_estimated_arrival = ComplexDateTimeField(required=True) #'2020-12-23T14:36:44+08:00'
    first_next_bus_load = StringField(required=True) #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    first_next_bus_feature = StringField(required=True) #Indicate if bus is wheel-chair accessible - WAB, else blank
    first_next_bus_the_type = StringField(required=True) #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    first_next_bus_origin_code = IntField(required=True) #Reference code of the first bus stop where this bus started its service 
    first_next_bus_destination_code = IntField(required=True) #Reference code of the last bus stop where this bus will terminate its service 
    first_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    first_bus_latitude = FloatField(required=True)
    first_bus_longitude = FloatField(required=True)

    #Second Next Bus Details
    second_next_bus_estimated_arrival = ComplexDateTimeField()
    second_next_bus_load = StringField() #SEA-Seats Available, SDA-Standing Available, LSD-Limited Standing
    second_next_bus_feature = StringField() #Indicate if bus is wheel-chair accessible - WAB, else blank
    second_next_bus_the_type = StringField() #SD-Single Deck, DD-Double-Deck, BD-Bendy
    
    second_next_bus_origin_code = IntField() #Reference code of the first bus stop where this bus started its service 
    second_next_bus_destination_code = IntField() #Reference code of the last bus stop where this bus will terminate its service 
    second_next_bus_visit_number = IntField() #Ordinal value of the nth visit of this vehicle at this bus stop; 1=1st visit, 2=2nd visit 

    second_bus_latitude = FloatField()
    second_bus_longitude = FloatField()
## TELEGRAM BOT ##########
chat_id =  # Tele ID of the Receiver
api_token = ''
base_url = 'https://api.telegram.org/bot{}/'.format(api_token)

sendMsg_url = base_url + 'sendMessage'

def send_msg(chat_id, msg_text):
	params = {'chat_id':chat_id, 'text':msg_text}
	r = requests.post(sendMsg_url,params=params)
	return None

## TELEGRAM BOT END ##########

while True:
    if __name__ == "__main__":
        try:

            #Authentication parameters
            headers = {'AccountKey' : '', 'accept' : 'application/json'}

            # BUS ARRIVAL TIMINGS (6 Stops) | BUS FREQUENCY (source: Datamall) #Every data should be stored throughout the day

            #1 Bus Stop #18051 – Ayer Rajah Ave (one-north Stn) #bus 91
            api_18051 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18051', headers=headers, verify=False)
            bus_arrivals_18051 = api_18051.json()['Services']
        
            if bus_arrivals_18051 != []: # if it is not empty, it proceeds
                print('#1 bus_arrivals_18051 is Operational')
                for busnumber_dict1 in bus_arrivals_18051:
                    if (busnumber_dict1['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict1['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18051_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict1['ServiceNo'],
                            operator = busnumber_dict1['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict1['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict1['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict1['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict1['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict1['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict1['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict1['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict1['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict1['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict1['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict1['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict1['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict1['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict1['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict1['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict1['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict1['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict1['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #1 Successfully Stored to NewBusArrival_18051_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict1['ServiceNo']))
                    else:
                        NewBusArrival_18051_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict1['ServiceNo'],
                            operator = busnumber_dict1['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict1['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict1['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict1['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict1['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict1['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict1['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict1['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict1['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict1['NextBus']['VisitNumber'],
                        ).save()
                        print(' #1 Successfully Stored to NewBusArrival_18051_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict1['ServiceNo']))
            else:
                print('#1 bus_arrivals_18051 is NO LONGER operational')

            #2 Bus Stop #18059 – Ayer Rajah Ave (Opp one-north Stn) #bus 91
            api_18059 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18059', headers=headers, verify=False)
            bus_arrivals_18059 = api_18059.json()['Services']
            
            if bus_arrivals_18059 != []: #is not empty
                print('#2 bus_arrivals_18059 is Operational')
                for busnumber_dict2 in bus_arrivals_18059:
                    if (busnumber_dict2['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict2['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18059_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict2['ServiceNo'],
                            operator = busnumber_dict2['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict2['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict2['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict2['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict2['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict2['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict2['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict2['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict2['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict2['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict2['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict2['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict2['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict2['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict2['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict2['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict2['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict2['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict2['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #2 Successfully Stored to NewBusArrival_18059_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict2['ServiceNo']))
                    else:
                        NewBusArrival_18059_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict2['ServiceNo'],
                            operator = busnumber_dict2['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict2['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict2['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict2['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict2['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict2['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict2['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict2['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict2['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict2['NextBus']['VisitNumber'],
                        ).save()
                        print(' #2 Successfully Stored to NewBusArrival_18059_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict2['ServiceNo']))
                    
            else:
                print('#2 bus_arrivals_18059 is NO LONGER operational')

            #3 Bus Stop #18159 – Portsdown Rd (one-north Stn/Galaxis) #bus 191
            api_18159 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18159', headers=headers, verify=False)
            bus_arrivals_18159 = api_18159.json()['Services']
            
            if bus_arrivals_18159 != []: # if it is not empty, it proceeds
                print('#3 bus_arrivals_18159 is Operational')
                for busnumber_dict3 in bus_arrivals_18159:
                    if (busnumber_dict3['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict3['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18159_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict3['ServiceNo'],
                            operator = busnumber_dict3['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict3['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict3['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict3['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict3['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict3['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict3['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict3['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict3['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict3['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict3['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict3['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict3['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict3['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict3['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict3['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict3['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict3['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict3['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #3 Successfully Stored to NewBusArrival_18159_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict3['ServiceNo']))
                    else:
                        NewBusArrival_18159_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict3['ServiceNo'],
                            operator = busnumber_dict3['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict3['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict3['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict3['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict3['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict3['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict3['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict3['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict3['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict3['NextBus']['VisitNumber'],
                        ).save()
                        print(' #3 Successfully Stored to NewBusArrival_18159_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict3['ServiceNo']))
            else:
                print('#3 bus_arrivals_18159 is NO LONGER operational')

            #4 Bus Stop #18151 – Portsdown Rd (Opp one-north Stn/Galaxis) #bus 191
            api_18151 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18151', headers=headers, verify=False)
            bus_arrivals_18151 = api_18151.json()['Services']
            
            if bus_arrivals_18151 != []:
                print('#4 bus_arrivals_18151 is Operational')
                for busnumber_dict4 in bus_arrivals_18151:
                    if (busnumber_dict4['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict4['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18151_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict4['ServiceNo'],
                            operator = busnumber_dict4['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict4['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict4['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict4['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict4['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict4['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict4['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict4['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict4['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict4['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict4['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict4['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict4['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict4['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict4['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict4['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict4['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict4['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict4['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #4 Successfully Stored to NewBusArrival_18151_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict4['ServiceNo']))
                    else:
                        NewBusArrival_18151_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict4['ServiceNo'],
                            operator = busnumber_dict4['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict4['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict4['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict4['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict4['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict4['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict4['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict4['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict4['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict4['NextBus']['VisitNumber'],
                        )#.save()
                        print(' #4 Successfully Stored to NewBusArrival_18151_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict4['ServiceNo']))
            else:
                print('#4 bus_arrivals_18151 is NO LONGER operational')

            #5 Bus Stop #18121 - Buona Vista Flyover (Opp Ayer Rajah Ind Est) #bus 14., 33., 92., 92A., 95., 95B, 166., 198., 200.
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18121
            api_18121 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18121', headers=headers, verify=False)
            bus_arrivals_18121 = api_18121.json()['Services']
            
            if bus_arrivals_18121 != []:
                print('#5 bus_arrivals_18121 is Operational')
                for busnumber_dict5 in bus_arrivals_18121:
                    if (busnumber_dict5['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict5['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18121_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict5['ServiceNo'],
                            operator = busnumber_dict5['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict5['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict5['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict5['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict5['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict5['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict5['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict5['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict5['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict5['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict5['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict5['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict5['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict5['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict5['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict5['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict5['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict5['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict5['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #5 Successfully Stored to NewBusArrival_18121_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict5['ServiceNo']))
                    else:
                        NewBusArrival_18121_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict5['ServiceNo'],
                            operator = busnumber_dict5['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict5['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict5['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict5['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict5['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict5['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict5['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict5['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict5['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict5['NextBus']['VisitNumber'],
                        ).save()
                        print(' #5 Successfully Stored to NewBusArrival_18121_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict5['ServiceNo']))
            else:
                print('#5 bus_arrivals_18121 is NO LONGER operational')
            
            #6 Bus Stop #18129 - Buona Vista Flyover (Ayer Rajah Ind Est) #bus 14, 33, 33A, 92, 92A, 92B, 95, 166, 198, 200, 200A
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18129
            api_18129 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18129', headers=headers, verify=False)
            bus_arrivals_18129 = api_18129.json()['Services']

            if bus_arrivals_18129 != []:
                print('#6 bus_arrivals_18129 is Operational')
                for busnumber_dict6 in bus_arrivals_18129:
                    if (busnumber_dict6['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict6['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18129_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict6['ServiceNo'],
                            operator = busnumber_dict6['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict6['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict6['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict6['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict6['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict6['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict6['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict6['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict6['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict6['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict6['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict6['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict6['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict6['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict6['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict6['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict6['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict6['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict6['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #6 Successfully Stored to NewBusArrival_18129_2nd - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict6['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18129_2nd(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict6['ServiceNo'],
                            operator = busnumber_dict6['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict6['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict6['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict6['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict6['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict6['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict6['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict6['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict6['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict6['NextBus']['VisitNumber'],
                        ).save()
                        print(' #6 Successfully Stored to NewBusArrival_18129_2nd - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict6['ServiceNo']))
            else:
                print('#6 bus_arrivals_18129 is NO LONGER operational')

        except Exception as ErrorMessage:
            print('ERROR MESSAGE: ', ErrorMessage)
            msg_text = 'Bus Arrival Error'
            send_msg(chat_id, msg_text)

        finally:
            time.sleep(60) # 1 minute pause