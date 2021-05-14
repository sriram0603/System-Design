'''
System Design overview for Movie Ticket Booking - Online
BMS - book my show app
the user should be connecting to theater's DB and its API.
how will the BMS know which seats are available and which are not?
instead of directly connecting to DB and reading its tables, we can connect through its API.
so there can be many API based on the work they do. one to search available seats, one to
lock the system, etc.,
why do we need a lock?
multiple people will try to book, so the API will lock the seat for a limited time 
and then it is released. 
features?
1) highly concurrent 90000-95000 reqsts per day 
2) responsive UI
3) multiple cities
4) Payments
5) Movie suggestions
6) comments and ratings
7) Movie Info
8) Send tickets by SMS and mail and whatsapp
the clients can be done from phone or tablet--> load balancer - in load balancer the 
request can be sure of round robin, consistent hashing, least connection and many other 
methods based on our requirements.
then the load balancer directs to a cache system called Varnish or CDN to reduce load on the 
server --> then to the app server which scales horizontally to handle lot of rqsts
(java, spring Boot,hibernate is used, but can also use python)
to support search system - dump all the data from app servers to Elatisearch where it has
distributed and RESTfuk search API's in the system.--> use a caching
---> we can actually both where we use rdbms beacuse of ACID properties, and also the 
data wont be growing much, and we will be needing NoSQL for the info about the movie and
its crew.  As there will be a lot of data for a RDBMS to handle, so go for Big DATA - NoSQL.
(to handle ratings,comments,reviews,crew)- can use Cassandra. RDBMS should shard data 
or use Master slave architecture. we can set the replication factor for the NoSQL DB to
save the copies of data. for making SMS, Email or whatsapp we have to use third party API.
as soon as the server completes booking, we can send message to a queue to send out 
the messages. use the hadoop for business intelligence, all the logs, user activity into 
hadoop and use Pig or hive to query. Also we can use kafka and dump into spark or storm 
to read the real time analysis.
working steps:
we can see the location using the GPS or ISP provider, and when he tries to book ticket,
the BMS server will ask theatre to lock for a time window. 
it uses Microservices architecture. 
uses RabbitMq for queue service.
all logs are sent to logstash                                           
DB schema tables MYSQL                           |---Movie
place--manytomany--theatre--manytomany--screen--OTO--manytomay--tier--MTM--seats,
ticket--MTM --seats, user--MTM--ticket.offer--OTO--seats,screen,Movie
For NoSQL - we need to do Data Modelling based on the number of queries and what queries.
		
'''


# declaring Enums constants and data types
from abc import ABC 
from enum import Enum
class BookingStatus(Enum):
    REQUESTED,CONFIRMED,CANCELLED = 1,2,3

class SeatType(Enum):
    REGULAR,PREMUIM, ACCESSIBLE = 1,2,3

class AccountStatus(Enum):
    ACTIVE,BLOCKED,UNKNOWN = 1,2,3

class PaymentStatus(Enum):
    UNPAID,DECLINED,CANCELLED,REFUNDED,COMPLETED = 1,2,3,4,5

class Adress:
    def __init__(self,street,city,state,zipcode,country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__country = country


class Account:
    def __init__(self,Id, password,status = AccountStatus.ACTIVE):
        self.__Id = Id
        self.__password = password
        self.__status = status
    
    def resetPassword(self):
        pass

# we are defining persons who are going to interact with out system 

class Person(ABC):
    def __init__(self,name,address,email,account):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account = account

class Customer(Person):
    def makeBooking(self,booking):
        pass
    def getBookings(self):
        pass


class Admin(Person):
    def add_movie(self,movie):
        pass
    def add_show(slef,show):
        pass
    def bloack_user(self):
        pass

class FrontDeskOfficer(Person):
    def create_booking(self,booking):
        pass

class Guest:
    def register_account(self):
        pass

#Shows and Movies: A movie can have many shows

from datetime import datetime

class Show:
    def __init__(self,id,played_at,movie,start_time,end_time):
        self.__show_id = id
        self.__created_on = datetime.today()
        self.__start_time = start_time
        self.__played_at = played_at
        self.__movie = movie



class Movie:
    def __init__(self,title,description,duration,langauge):
        self.__title = title
        self.__description =description
        self.__language = langauge
        self.__duration = duration
        self.__shows = []
    
    def get_shows(self):
        return self.__shows

