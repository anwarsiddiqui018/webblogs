import requests
import pandas as pd
from datetime import datetime, timedelta
import datetime, calendar
from io import StringIO

pd.set_option('display.width',1500)
pd.set_option('display.max_columns',225)
pd.set_option('display.max_rows',225)

volatilityList = []
expiry = '30APR2020'
print("Running Stock Volatility Sheet for Expiry: {}".format(expiry))
####################################################################### UPDATE HERE #####################
D = '20022020'

# dateList=['03042020','07042020','08042020','09042020','13042020']
dateList =[]
holidaylist = ['21022020','10032020','02042020','05042020','06042020','10042020','14042020', '01052020','25052020','02102020','16112020','30112020','25122020']

#######################################################################

class DeliveryPercentage:
    def __init__(self):
        pass
    def fetchEquity(self,date):
        try:
            url = "https://www1.nseindia.com/archives/equities/mto/MTO_" + date + ".DAT"
            # print(url)
            r = requests.get(url, headers={'User-Agent': 'PostmannRuntime/7.21.0'})
            # print(r.text)
            csvdata = r.text.partition('<N>')[2]
            df = pd.read_csv(StringIO(csvdata))
            return df
        except:
            print("Data Not Available for the Mentioned DATE")


    def calculateVolatility(self):
        date1 = datetime.date.today()
        dateList = DeliveryPercentage().getDateList(date1)
        df0 = DeliveryPercentage().fetchEquity(dateList[0])
        df1 = DeliveryPercentage().fetchEquity(dateList[1])
        df2 = DeliveryPercentage().fetchEquity(dateList[2])
        df3 = DeliveryPercentage().fetchEquity(dateList[3])
        df4 = DeliveryPercentage().fetchEquity(dateList[4])
        df7 = df3[df3['Sr No'].isin(['SBIN','TECHM','PVR','BEL','PEL','SBIN']) & df3['Name of Security'].str.contains('EQ')]
        # print(df7.nlargest(5, ['% of Deliverable Quantity to Traded Quantity']))

        return df0,df1,df2,df3

    def filterEquity(self,df, TICKER):
        df = df[df['Sr No'].str.contains(TICKER) & df['Name of Security'].str.contains('EQ')]
        # df1 = df[df['Sr No'].str.contains('A') & df['Name of Security'].str.contains('EQ')]
        # df1.head()
        # df = df[df['Name of Security'].str.contains(symbol) & df['Quantity Traded'].str.contains('EQ')]
        # print(df)
        # print('D*********', df['% of Deliverable Quantity to Traded Quantity'])
        return df.iloc[0]['% of Deliverable Quantity to Traded Quantity']

    def getDateList(self,date1):
        numberofDays = 0
        print("ff :{},{}".format(date1.weekday(),date1))
        if (date1.weekday() == 5 or date1.weekday() == 6 or date1.strftime('%d%m%Y') in holidaylist):
            numberofDays = 6
        else:
            numberofDays = 5
            dateList.append(date1.strftime('%d%m%Y'))
        for i in range(1, numberofDays):
            if (date1.weekday() == 5):
                date_N_days_ago = date1 - timedelta(days=1)
            elif (date1.weekday() == 6):
                date_N_days_ago = date1 - timedelta(days=2)
            elif (date1.strftime('%d%m%Y') in holidaylist):
                date_N_days_ago = date1 - timedelta(days=1)
            else:
                date_N_days_ago = date1 - timedelta(days=1)
        # print('date_N_days_ago:', date_N_days_ago)

            if (date_N_days_ago.weekday() == 5):
                date_N_days_ago = date_N_days_ago - timedelta(days=1)
            if (date_N_days_ago.weekday() == 6):
                date_N_days_ago = date_N_days_ago - timedelta(days=2)
            if (date_N_days_ago.strftime('%d%m%Y') in holidaylist):
                date_N_days_ago = date_N_days_ago - timedelta(days=1)

            dateList.append(date_N_days_ago.strftime('%d%m%Y'))
            date1 = date_N_days_ago
        # print(sorted(dateList))
        # print (list(reversed(dateList)))
        return list(reversed(dateList))

TICKER = 'ASHOKLEY'
myclass = DeliveryPercentage()
df0,df1,df2,df3 = myclass.calculateVolatility()
print(TICKER)
print(myclass.filterEquity(df0,TICKER))
print(myclass.filterEquity(df1,TICKER))
print(myclass.filterEquity(df2,TICKER))
print(myclass.filterEquity(df3,TICKER))
