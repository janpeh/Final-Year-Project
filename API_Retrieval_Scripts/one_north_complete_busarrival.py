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

class NewBusArrival_11361(Document):
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

class NewBusArrival_11369(Document):
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

class NewBusArrival_11191(Document):
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

class NewBusArrival_18021(Document):
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

class NewBusArrival_18029(Document):
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

class NewBusArrival_18049(Document):
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

class NewBusArrival_18061(Document):
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

class NewBusArrival_18069(Document):
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

class NewBusArrival_18079(Document):
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

class NewBusArrival_18081(Document):
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

class NewBusArrival_18089(Document):
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

class NewBusArrival_18099(Document):
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

class NewBusArrival_18109(Document):
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

class NewBusArrival_18141(Document):
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

class NewBusArrival_18149(Document):
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

class NewBusArrival_18171(Document):
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

class NewBusArrival_18179(Document):
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

class NewBusArrival_18181(Document):
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

class NewBusArrival_18189(Document):
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

class NewBusArrival_18191(Document):
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

class NewBusArrival_18199(Document):
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

class NewBusArrival_18201(Document):
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

class NewBusArrival_18211(Document):
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

            # BUS ARRIVAL TIMINGS (23 Stops) | BUS FREQUENCY (source: Datamall) #Every data should be stored throughout the day

            #1 Bus Stop #11361 – BUONA VISTA STN EXIT C #bus 14 74 91 92 92M 95 191 196 198 200 
            api_11361 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=11361', headers=headers, verify=False)
            bus_arrivals_11361 = api_11361.json()['Services']
        
            if bus_arrivals_11361 != []: # if it is not empty, it proceeds
                print('#1 bus_arrivals_11361 is Operational')
                for busnumber_dict1 in bus_arrivals_11361:
                    if (busnumber_dict1['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict1['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_11361(
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
                        print(' #1 Successfully Stored to NewBusArrival_11361 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict1['ServiceNo']))
                    else:
                        NewBusArrival_11361(
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
                        print(' #1 Successfully Stored to NewBusArrival_11361 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict1['ServiceNo']))
            else:
                print('#1 bus_arrivals_11361 is NO LONGER operational')

            #2 Bus Stop #11369 – BUONA VISTA STN EXIT D #bus 14 74 91 92 92M 95 191 196 198 200
            api_11369 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=11369', headers=headers, verify=False)
            bus_arrivals_11369= api_11369.json()['Services']
            
            if bus_arrivals_11369 != []: #is not empty
                print('#2 bus_arrivals_11369 is Operational')
                for busnumber_dict2 in bus_arrivals_11369:
                    if (busnumber_dict2['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict2['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_11369(
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
                        print(' #2 Successfully Stored to NewBusArrival_11369 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict2['ServiceNo']))
                    else:
                        NewBusArrival_11369(
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
                        print(' #2 Successfully Stored to NewBusArrival_11369 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict2['ServiceNo']))
                    
            else:
                print('#2 bus_arrivals_11369 is NO LONGER operational')

            #3 Bus Stop #11191 – BUONA VISTA STN #bus 100 105 106 147 185
            api_11191 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=11191', headers=headers, verify=False)
            bus_arrivals_11191 = api_11191.json()['Services']
            
            if bus_arrivals_11191!= []: # if it is not empty, it proceeds
                print('#3 bus_arrivals_11191 is Operational')
                for busnumber_dict3 in bus_arrivals_11191:
                    if (busnumber_dict3['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict3['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_11191(
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
                        print(' #3 Successfully Stored to NewBusArrival_11191- B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict3['ServiceNo']))
                    else:
                        NewBusArrival_11191(
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
                        print(' #3 Successfully Stored to NewBusArrival_11191 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict3['ServiceNo']))
            else:
                print('#3 bus_arrivals_11191 is NO LONGER operational')

            #4 Bus Stop #18021 – OPP GEMPLUS #bus 91
            api_18021 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18021', headers=headers, verify=False)
            bus_arrivals_18021 = api_18021.json()['Services']
            
            if bus_arrivals_18021 != []:
                print('#4 bus_arrivals_18021 is Operational')
                for busnumber_dict4 in bus_arrivals_18021:
                    if (busnumber_dict4['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict4['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18021(
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
                        print(' #4 Successfully Stored to NewBusArrival_18021 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict4['ServiceNo']))
                    else:
                        NewBusArrival_18021(
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
                        print(' #4 Successfully Stored to NewBusArrival_18021 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict4['ServiceNo']))
            else:
                print('#4 bus_arrivals_18021 is NO LONGER operational')

            #5 Bus Stop #18029 - TEMPCO MFG #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18029
            api_18029 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18029', headers=headers, verify=False)
            bus_arrivals_18029 = api_18029.json()['Services']
            
            if bus_arrivals_18029 != []:
                print('#5 bus_arrivals_18029 is Operational')
                for busnumber_dict5 in bus_arrivals_18029:
                    if (busnumber_dict5['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict5['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18029(
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
                        print(' #5 Successfully Stored to NewBusArrival_18029 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict5['ServiceNo']))
                    else:
                        NewBusArrival_18029(
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
                        print(' #5 Successfully Stored to NewBusArrival_18029 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict5['ServiceNo']))
            else:
                print('#5 bus_arrivals_18029 is NO LONGER operational')
            
            #6 Bus Stop #18049 - OPP SCIENCE PK #bus 14 166 197 33 33A 97 97e 963 963e
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18049
            api_18049 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18049', headers=headers, verify=False)
            bus_arrivals_18049 = api_18049.json()['Services']

            if bus_arrivals_18049 != []:
                print('#6 bus_arrivals_18049 is Operational')
                for busnumber_dict6 in bus_arrivals_18049:
                    if (busnumber_dict6['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict6['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18049(
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
                        print(' #6 Successfully Stored to NewBusArrival_18049 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict6['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18049(
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
                        print(' #6 Successfully Stored to NewBusArrival_18049 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict6['ServiceNo']))
            else:
                print('#6 bus_arrivals_18049 is NO LONGER operational')

            #7 Bus Stop #18061 - BLK 71 #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18061
            api_18061 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18061', headers=headers, verify=False)
            bus_arrivals_18061 = api_18061.json()['Services']

            if bus_arrivals_18061 != []:
                print('#7 bus_arrivals_18061 is Operational')
                for busnumber_dict7 in bus_arrivals_18061:
                    if (busnumber_dict7['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict7['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18061(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict7['ServiceNo'],
                            operator = busnumber_dict7['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict7['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict7['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict7['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict7['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict7['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict7['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict7['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict7['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict7['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict7['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict7['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict7['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict7['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict7['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict7['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict7['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict7['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict7['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #7 Successfully Stored to NewBusArrival_18061 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict7['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18061(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict7['ServiceNo'],
                            operator = busnumber_dict7['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict7['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict7['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict7['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict7['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict7['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict7['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict7['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict7['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict7['NextBus']['VisitNumber'],
                        ).save()
                        print(' #7 Successfully Stored to NewBusArrival_18061 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict7['ServiceNo']))
            else:
                print('#7 bus_arrivals_18061 is NO LONGER operational')


            #8 Bus Stop #18069 - OPP BLK 71 #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18069
            api_18069 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18069', headers=headers, verify=False)
            bus_arrivals_18069 = api_18069.json()['Services']

            if bus_arrivals_18069 != []:
                print('#8 bus_arrivals_18069 is Operational')
                for busnumber_dict8 in bus_arrivals_18069:
                    if (busnumber_dict8['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict8['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18069(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict8['ServiceNo'],
                            operator = busnumber_dict8['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict8['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict8['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict8['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict8['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict8['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict8['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict8['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict8['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict8['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict8['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict8['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict8['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict8['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict8['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict8['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict8['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict8['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict8['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #8 Successfully Stored to NewBusArrival_18069 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict8['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18069(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict8['ServiceNo'],
                            operator = busnumber_dict8['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict8['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict8['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict8['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict8['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict8['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict8['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict8['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict8['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict8['NextBus']['VisitNumber'],
                        ).save()
                        print(' #8 Successfully Stored to NewBusArrival_18069 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict8['ServiceNo']))
            else:
                print('#8 bus_arrivals_18069 is NO LONGER operational')

            
            #9 Bus Stop #18079 - Opp Nuh #bus 197 198 97 963 963e
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18079
            api_18079 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18079', headers=headers, verify=False)
            bus_arrivals_18079 = api_18079.json()['Services']

            if bus_arrivals_18079 != []:
                print('#9 bus_arrivals_18079 is Operational')
                for busnumber_dict9 in bus_arrivals_18079:
                    if (busnumber_dict9['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict9['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18079(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict9['ServiceNo'],
                            operator = busnumber_dict9['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict9['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict9['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict9['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict9['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict9['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict9['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict9['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict9['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict9['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict9['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict9['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict9['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict9['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict9['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict9['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict9['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict9['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict9['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #9 Successfully Stored to NewBusArrival_18079 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict9['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18079(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict9['ServiceNo'],
                            operator = busnumber_dict9['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict9['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict9['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict9['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict9['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict9['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict9['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict9['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict9['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict9['NextBus']['VisitNumber'],
                        ).save()
                        print(' #9 Successfully Stored to NewBusArrival_18079 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict9['ServiceNo']))
            else:
                print('#9 bus_arrivals_18079 is NO LONGER operational')


            #10 Bus Stop #18081 - BLK 55 #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18081
            api_18081 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18081', headers=headers, verify=False)
            bus_arrivals_18081 = api_18081.json()['Services']

            if bus_arrivals_18081 != []:
                print('#10 bus_arrivals_18081 is Operational')
                for busnumber_dict10 in bus_arrivals_18081:
                    if (busnumber_dict10['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict10['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18081(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict10['ServiceNo'],
                            operator = busnumber_dict10['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict10['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict10['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict10['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict10['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict10['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict10['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict10['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict10['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict10['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict10['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict10['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict10['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict10['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict10['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict10['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict10['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict10['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict10['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #10 Successfully Stored to NewBusArrival_18081 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict10['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18081(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict10['ServiceNo'],
                            operator = busnumber_dict10['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict10['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict10['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict10['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict10['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict10['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict10['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict10['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict10['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict10['NextBus']['VisitNumber'],
                        ).save()
                        print(' #10 Successfully Stored to NewBusArrival_18081 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict10['ServiceNo']))
            else:
                print('#10 bus_arrivals_18081 is NO LONGER operational')

            
            #11 Bus Stop #18089 - S'PORE POST #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18089
            api_18089 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18089', headers=headers, verify=False)
            bus_arrivals_18089 = api_18089.json()['Services']

            if bus_arrivals_18089 != []:
                print('#11 bus_arrivals_18089 is Operational')
                for busnumber_dict11 in bus_arrivals_18089:
                    if (busnumber_dict11['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict11['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18089(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict11['ServiceNo'],
                            operator = busnumber_dict11['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict11['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict11['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict11['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict11['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict11['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict11['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict11['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict11['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict11['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict11['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict11['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict11['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict11['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict11['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict11['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict11['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict11['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict11['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #11 Successfully Stored to NewBusArrival_18089 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict11['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18089(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict11['ServiceNo'],
                            operator = busnumber_dict11['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict11['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict11['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict11['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict11['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict11['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict11['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict11['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict11['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict11['NextBus']['VisitNumber'],
                        ).save()
                        print(' #11 Successfully Stored to NewBusArrival_18089- B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict11['ServiceNo']))
            else:
                print('#11 bus_arrivals_18089 is NO LONGER operational')


            #12 Bus Stop #18099 - AYER RAJAH BUS PK #bus 91
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18099
            api_18099 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18099', headers=headers, verify=False)
            bus_arrivals_18099 = api_18099.json()['Services']

            if bus_arrivals_18099!= []:
                print('#12 bus_arrivals_18099 is Operational')
                for busnumber_dict12 in bus_arrivals_18099:
                    if (busnumber_dict12['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict12['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18099(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict12['ServiceNo'],
                            operator = busnumber_dict12['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict12['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict12['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict12['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict12['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict12['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict12['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict12['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict12['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict12['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict12['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict12['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict12['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict12['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict12['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict12['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict12['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict12['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict12['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #12 Successfully Stored to NewBusArrival_18099 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict12['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18099(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict12['ServiceNo'],
                            operator = busnumber_dict12['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict12['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict12['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict12['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict12['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict12['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict12['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict12['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict12['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict12['NextBus']['VisitNumber'],
                        ).save()
                        print(' #12 Successfully Stored to NewBusArrival_18099 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict12['ServiceNo']))
            else:
                print('#12 bus_arrivals_18099 is NO LONGER operational')


            #13 Bus Stop #18109 - OPP PSB SCIENCE PK BLDG #bus 14 166 197 33 33A 97 963 963e
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18109
            api_18109 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18109', headers=headers, verify=False)
            bus_arrivals_18109 = api_18109.json()['Services']

            if bus_arrivals_18109 != []:
                print('#13 bus_arrivals_18109 is Operational')
                for busnumber_dict13 in bus_arrivals_18109:
                    if (busnumber_dict13['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict13['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18109(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict13['ServiceNo'],
                            operator = busnumber_dict13['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict13['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict13['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict13['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict13['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict13['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict13['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict13['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict13['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict13['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict13['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict13['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict13['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict13['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict13['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict13['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict13['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict13['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict13['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #13 Successfully Stored to NewBusArrival_18109 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict13['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18109(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict13['ServiceNo'],
                            operator = busnumber_dict13['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict13['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict13['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict13['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict13['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict13['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict13['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict13['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict13['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict13['NextBus']['VisitNumber'],
                        ).save()
                        print(' #13 Successfully Stored to NewBusArrival_18109 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict13['ServiceNo']))
            else:
                print('#13 bus_arrivals_18109 is NO LONGER operational')


            #14 Bus Stop #18141 - AFT ANGLO-CHINESE JC #bus 14 191 196 198 200 74 91 92 92A 92M 95 95B
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18141
            api_18141 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18141', headers=headers, verify=False)
            bus_arrivals_18141 = api_18141.json()['Services']

            if bus_arrivals_18141 != []:
                print('#14 bus_arrivals_18141 is Operational')
                for busnumber_dict14 in bus_arrivals_18141:
                    if (busnumber_dict14['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict14['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18141(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict14['ServiceNo'],
                            operator = busnumber_dict14['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict14['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict14['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict14['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict14['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict14['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict14['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict14['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict14['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict14['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict14['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict14['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict14['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict14['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict14['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict14['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict14['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict14['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict14['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #14 Successfully Stored to NewBusArrival_18141 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict14['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18141(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict14['ServiceNo'],
                            operator = busnumber_dict14['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict14['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict14['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict14['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict14['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict14['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict14['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict14['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict14['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict14['NextBus']['VisitNumber'],
                        ).save()
                        print(' #14 Successfully Stored to NewBusArrival_18141 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict14['ServiceNo']))
            else:
                print('#14 bus_arrivals_18141 is NO LONGER operational')


            
            #15 Bus Stop #18149 - ESSEC BUSINESS SCH #bus 14 191 196 198 200 200A 74 91 92 92A 92B 92M 95
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18149
            api_18149 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18149', headers=headers, verify=False)
            bus_arrivals_18149 = api_18149.json()['Services']

            if bus_arrivals_18149 != []:
                print('#15 bus_arrivals_18149 is Operational')
                for busnumber_dict15 in bus_arrivals_18149:
                    if (busnumber_dict15['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict15['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18149(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict15['ServiceNo'],
                            operator = busnumber_dict15['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict15['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict15['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict15['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict15['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict15['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict15['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict15['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict15['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict15['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict15['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict15['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict15['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict15['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict15['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict15['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict15['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict15['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict15['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #15 Successfully Stored to NewBusArrival_18149 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict15['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18149(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict15['ServiceNo'],
                            operator = busnumber_dict15['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict15['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict15['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict15['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict15['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict15['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict15['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict15['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict15['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict15['NextBus']['VisitNumber'],
                        ).save()
                        print(' #15 Successfully Stored to NewBusArrival_18149 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict15['ServiceNo']))
            else:
                print('#15 bus_arrivals_18149 is NO LONGER operational')


            #16 Bus Stop #18171 - BEF WEYHILL CL #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18171
            api_18171 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18171', headers=headers, verify=False)
            bus_arrivals_18171 = api_18171.json()['Services']

            if bus_arrivals_18171 != []:
                print('#16 bus_arrivals_18171 is Operational')
                for busnumber_dict16 in bus_arrivals_18171:
                    if (busnumber_dict16['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict16['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18171(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict16['ServiceNo'],
                            operator = busnumber_dict16['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict16['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict16['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict16['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict16['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict16['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict16['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict16['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict16['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict16['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict16['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict16['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict16['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict16['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict16['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict16['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict16['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict16['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict16['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #16 Successfully Stored to NewBusArrival_18171 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict16['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18171(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict16['ServiceNo'],
                            operator = busnumber_dict16['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict16['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict16['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict16['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict16['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict16['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict16['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict16['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict16['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict16['NextBus']['VisitNumber'],
                        ).save()
                        print(' #16 Successfully Stored to NewBusArrival_18171 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict16['ServiceNo']))
            else:
                print('#16 bus_arrivals_18171 is NO LONGER operational')


            #17 Bus Stop #18179 - OPP WEYHILL CL #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18179
            api_18179 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18179', headers=headers, verify=False)
            bus_arrivals_18179 = api_18179.json()['Services']

            if bus_arrivals_18179 != []:
                print('#17 bus_arrivals_18179 is Operational')
                for busnumber_dict17 in bus_arrivals_18179:
                    if (busnumber_dict17['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict17['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18179(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict17['ServiceNo'],
                            operator = busnumber_dict17['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict17['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict17['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict17['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict17['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict17['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict17['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict17['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict17['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict17['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict17['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict17['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict17['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict17['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict17['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict17['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict17['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict17['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict17['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #17 Successfully Stored to NewBusArrival_18179 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict17['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18179(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict17['ServiceNo'],
                            operator = busnumber_dict17['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict17['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict17['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict17['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict17['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict17['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict17['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict17['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict17['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict17['NextBus']['VisitNumber'],
                        ).save()
                        print(' #17 Successfully Stored to NewBusArrival_18179 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict17['ServiceNo']))
            else:
                print('#17 bus_arrivals_18179 is NO LONGER operational')


            
            #18 Bus Stop #18181 - OPP RAEBURN PK #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18181
            api_18181 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18181', headers=headers, verify=False)
            bus_arrivals_18181 = api_18181.json()['Services']

            if bus_arrivals_18181 != []:
                print('#18 bus_arrivals_18181 is Operational')
                for busnumber_dict18 in bus_arrivals_18181:
                    if (busnumber_dict18['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict18['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18181(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict18['ServiceNo'],
                            operator = busnumber_dict18['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict18['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict18['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict18['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict18['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict18['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict18['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict18['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict18['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict18['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict18['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict18['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict18['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict18['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict18['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict18['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict18['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict18['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict18['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #18 Successfully Stored to NewBusArrival_18181 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict18['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18181(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict18['ServiceNo'],
                            operator = busnumber_dict18['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict18['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict18['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict18['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict18['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict18['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict18['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict18['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict18['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict18['NextBus']['VisitNumber'],
                        ).save()
                        print(' #18 Successfully Stored to NewBusArrival_18181 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict18['ServiceNo']))
            else:
                print('#18 bus_arrivals_18181 is NO LONGER operational')


            #19 Bus Stop #18189 - RAEBURN PK SCH #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18189
            api_18189 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18189', headers=headers, verify=False)
            bus_arrivals_18189 = api_18189.json()['Services']

            if bus_arrivals_18189 != []:
                print('#19 bus_arrivals_18189 is Operational')
                for busnumber_dict19 in bus_arrivals_18189:
                    if (busnumber_dict19['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict19['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18189(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict19['ServiceNo'],
                            operator = busnumber_dict19['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict19['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict19['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict19['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict19['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict19['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict19['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict19['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict19['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict19['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict19['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict19['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict19['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict19['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict19['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict19['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict19['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict19['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict19['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #19 Successfully Stored to NewBusArrival_18189 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict19['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18189(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict19['ServiceNo'],
                            operator = busnumber_dict19['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict19['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict19['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict19['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict19['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict19['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict19['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict19['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict19['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict19['NextBus']['VisitNumber'],
                        ).save()
                        print(' #19 Successfully Stored to NewBusArrival_18189 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict19['ServiceNo']))
            else:
                print('#19 bus_arrivals_18189 is NO LONGER operational')


            #20 Bus Stop #18191 - BEF WHITCHURCH RD #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18191
            api_18191= requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18191', headers=headers, verify=False)
            bus_arrivals_18191 = api_18191.json()['Services']

            if bus_arrivals_18191 != []:
                print('#20 bus_arrivals_18191 is Operational')
                for busnumber_dict20 in bus_arrivals_18191:
                    if (busnumber_dict20['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict20['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18191(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict20['ServiceNo'],
                            operator = busnumber_dict20['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict20['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict20['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict20['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict20['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict20['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict20['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict20['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict20['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict20['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict20['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict20['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict20['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict20['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict20['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict20['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict20['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict20['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict20['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #20 Successfully Stored to NewBusArrival_18191 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict20['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18191(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict20['ServiceNo'],
                            operator = busnumber_dict20['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict20['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict20['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict20['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict20['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict20['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict20['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict20['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict20['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict20['NextBus']['VisitNumber'],
                        ).save()
                        print(' #20 Successfully Stored to NewBusArrival_18191 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict20['ServiceNo']))
            else:
                print('#20 bus_arrivals_18191 is NO LONGER operational')


            #21 Bus Stop #18199 - AFT WHITCHURCH RD #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18199
            api_18199 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18199', headers=headers, verify=False)
            bus_arrivals_18199 = api_18199.json()['Services']

            if bus_arrivals_18199 != []:
                print('#21 bus_arrivals_18199 is Operational')
                for busnumber_dict21 in bus_arrivals_18199:
                    if (busnumber_dict21['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict21['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18199(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict21['ServiceNo'],
                            operator = busnumber_dict21['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict21['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict21['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict21['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict21['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict21['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict21['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict21['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict21['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict21['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict21['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict21['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict21['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict21['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict21['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict21['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict21['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict21['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict21['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #21 Successfully Stored to NewBusArrival_18199 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict21['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18199(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict21['ServiceNo'],
                            operator = busnumber_dict21['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict21['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict21['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict21['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict21['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict21['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict21['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict21['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict21['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict21['NextBus']['VisitNumber'],
                        ).save()
                        print(' #21 Successfully Stored to NewBusArrival_18199 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict21['ServiceNo']))
            else:
                print('#21 bus_arrivals_18199 is NO LONGER operational')


            #22 Bus Stop #18201 - MEDIA CAMPUS #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18201
            api_18201 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18201', headers=headers, verify=False)
            bus_arrivals_18201 = api_18201.json()['Services']

            if bus_arrivals_18201 != []:
                print('#22 bus_arrivals_18201 is Operational')
                for busnumber_dict22 in bus_arrivals_18201:
                    if (busnumber_dict22['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict22['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18201(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict22['ServiceNo'],
                            operator = busnumber_dict22['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict22['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict22['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict22['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict22['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict22['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict22['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict22['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict22['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict22['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict22['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict22['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict22['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict22['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict22['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict22['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict22['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict22['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict22['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #22 Successfully Stored to NewBusArrival_18201 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict22['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18201(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict22['ServiceNo'],
                            operator = busnumber_dict22['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict22['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict22['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict22['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict22['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict22['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict22['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict22['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict22['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict22['NextBus']['VisitNumber'],
                        ).save()
                        print(' #22 Successfully Stored to NewBusArrival_18201 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict22['ServiceNo']))
            else:
                print('#22 bus_arrivals_18201 is NO LONGER operational')


            #23 Bus Stop #18211 - BEF JLN HANG JEBAT #bus 191
            # Bus Info Link: https://businterchange.net/sgbus/stops/busstop.php?stop=18211
            api_18211 = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=18211', headers=headers, verify=False)
            bus_arrivals_18211 = api_18211.json()['Services']

            if bus_arrivals_18211 != []:
                print('#23 bus_arrivals_18211 is Operational')
                for busnumber_dict23 in bus_arrivals_18211:
                    if (busnumber_dict23['NextBus2']['EstimatedArrival'] != "") and (busnumber_dict23['NextBus2']['EstimatedArrival'] != None): #means have
                        NewBusArrival_18211(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict23['ServiceNo'],
                            operator = busnumber_dict23['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict23['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict23['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict23['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict23['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict23['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict23['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict23['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict23['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict23['NextBus']['VisitNumber'],

                            # SECOND NEXT BUS DETAILS
                            second_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict23['NextBus2']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            second_next_bus_load = busnumber_dict23['NextBus2']['Load'],
                            second_next_bus_feature = busnumber_dict23['NextBus2']['Feature'],
                            second_next_bus_the_type = busnumber_dict23['NextBus2']['Type'],

                            second_bus_latitude = busnumber_dict23['NextBus2']['Latitude'],
                            second_bus_longitude = busnumber_dict23['NextBus2']['Longitude'],
                            
                            second_next_bus_origin_code = busnumber_dict23['NextBus2']['OriginCode'],
                            second_next_bus_destination_code = busnumber_dict23['NextBus2']['DestinationCode'],
                            second_next_bus_visit_number = busnumber_dict23['NextBus2']['VisitNumber'],
                        ).save()
                        print(' #23 Successfully Stored to NewBusArrival_18211 - B1B2 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict23['ServiceNo']))

                    else:
                        # msg_text = 'Bus Arrival Error'
                        # send_msg(chat_id, msg_text)

                        NewBusArrival_18211(
                            date_time = datetime.datetime.now(),
                            date = str(datetime.datetime.now().date()),
                            time = str(datetime.datetime.now().time()),
                            bus_number = busnumber_dict23['ServiceNo'],
                            operator = busnumber_dict23['Operator'],

                            # FIRST NEXT BUS DETAILS
                            first_next_bus_estimated_arrival = datetime.datetime.strptime(busnumber_dict23['NextBus']['EstimatedArrival'], '%Y-%m-%dT%H:%M:%S%z'),
                            first_next_bus_load = busnumber_dict23['NextBus']['Load'],
                            first_next_bus_feature = busnumber_dict23['NextBus']['Feature'], 
                            first_next_bus_the_type = busnumber_dict23['NextBus']['Type'],

                            first_bus_latitude = busnumber_dict23['NextBus']['Latitude'],
                            first_bus_longitude = busnumber_dict23['NextBus']['Longitude'],

                            first_next_bus_origin_code = busnumber_dict23['NextBus']['OriginCode'], 
                            first_next_bus_destination_code = busnumber_dict23['NextBus']['DestinationCode'],
                            first_next_bus_visit_number = busnumber_dict23['NextBus']['VisitNumber'],
                        ).save()
                        print(' #23 Successfully Stored to NewBusArrival_18211 - B1 '+ str(datetime.datetime.now()) + ' ' + str(busnumber_dict23['ServiceNo']))
            else:
                print('#23 bus_arrivals_18211 is NO LONGER operational')


        except Exception as ErrorMessage:
            print('ERROR MESSAGE: ', ErrorMessage)
            msg_text = 'Bus Arrival Error'
            send_msg(chat_id, msg_text)

        finally:
            time.sleep(60) # 1 minute pause