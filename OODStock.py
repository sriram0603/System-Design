#Requirements
'''
-->buy and sell stocks
-->market orders, stop loss, limit order, stop limit
-->Notification from the system
-->multiple watchlist for the stocks
-->view all the stocks he owns
-->stock lot - different volumes of same stock on diff day
-->tax statements yearly or quarterly
-->deposit - cash, wire transfer
'''
'''
USE CASES
customer - register, login , logout,add stocks to watchlist, create watchlist, 
        buy stock--inclusive--->search-->or sell stock, deposit, view his orders, 
        requesting for tax
admin - block/unblock customers
system - notifications, FETCH STOCKS FROM STOCK EXCHANGE API
'''
'''
    stockInventory---stocks, Account, order,notifications,watchlist,payment,admin,customer,
    <<Search>>,stock Exchange API
'''
#constants and enums required
from enum import Enum
class Returnstats(Enum):
    FAILED = 1
    SUCCESS = 2
    INSUFFICIENTFUNDS = 3

class Ordertype(Enum):
    OPEN = 1
    PARTIALLYFILLED = 2
    FILLED = 3
    CANCELLED = 4

