###############  TD API functions  ###############
import sys, os, time
sys.path.append('./tdameritrade')
sys.path.append('./data')
# sys.path.append('./tdameritrade')
import tdameritrade as td
import pandas as pd
import datetime
import json
## get stored token data
with open('token.json') as json_file:
    token = json.load(json_file)

conn = td.TDClient(api_key=token['api_key'], refresh_token=token['refresh_token'], access_token=token['access_token'], accountIds=token['accountIds'])

## update token data with refreshed access token

with open('token.json', 'w') as f:
    token['access_token'] = conn._access_token
    token['timestamp'] = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S') 
    json.dump(token, f, indent=4)

# read stock list in excel
equitylist_file = './EquityList.xlsx'
elist = pd.read_excel(equitylist_file)
# read stock list in csv
# equitylist_file = './data/Instrument.csv'
# elist = pd.read_csv(equitylist_file)

# equitylist_file = './epsactual_ticker_2018_2019.csv'
# elist = pd.read_csv(equitylist_file)

symbols = elist['Symbol']
data_dir_root = './data/Equity/'
runDate_t = datetime.datetime.now().strftime('%Y%m%d')
## data folders
data_dir_price = data_dir_root + 'HistPrices/'
if not os.path.exists(data_dir_price):
    os.makedirs(data_dir_price)

data_dir_fund = data_dir_root + 'Fundamentals/'
if not os.path.exists(data_dir_fund):
    os.makedirs(data_dir_fund)

data_dir_option = data_dir_root + 'Options/'
if not os.path.exists(data_dir_option):
    os.makedirs(data_dir_option)

## Fundamentals - All Symbols
df_fundametal = conn.fundamentalDF(symbols)
df_fundametal.to_csv(data_dir_fund + runDate_t + '_Fundamentals.csv', index=False)
## fetching all equity data
# x = [symbol for symbol in symbols if (not os.path.exists(data_dir_price + symbol + '_HistPrices.csv')) ]
for symbol in symbols:
    try:
        ## 1 - Historical Prices
        params = {'periodType': 'year',
                'period': 10,
                'frequencyType': 'daily',
                'frequency': 1,
                'needExtendedHoursData': 'true'
        }
        df_histprice = conn.historyDF(symbol, period=params['period'], periodType=params['periodType'], frequency=params['frequency'], frequencyType=params['frequencyType'])
        df_histprice.to_csv(data_dir_price + symbol + '_HistPrices.csv', index=False)
        # # 2 - Option Chain
        # params = {'contractType': 'CALL',
        #         'strikeCount': '5', 
        #         'includeQuotes': 'FALSE',
        #         'strategy': 'SINGLE',
        #         'fromDate': '2020-06-10',
        #         'toDate': '2020-06-11'
        # }
        # conn.options(symbol, contractType=params['contractType'], strikeCount=params['strikeCount'],fromDate=params['fromDate'], toDate=params['toDate'])
        ## all option chanin
        # if not os.path.exists(data_dir_option + runDate_t + '_' + symbol + '_Options.csv',):
        #     df_options = conn.optionsDF(symbol)
        #     df_options.to_csv(data_dir_option + runDate_t + '_' + symbol + '_Options.csv', index=False)
        # 3 - Fundamentals - by symbols
        # df_fundametal = conn.fundamentalDF(symbol)
        # df_fundametal = pd.DataFrame.from_records(data = df_fundametal.loc[0,'fundamental'], index=[0])
        # df_fundametal.to_csv(data_dir_fund + 'fundamentals.csv', index=False)
        # time.sleep(0.5)
    except Exception as e:
        print(e)
        print('missing quote for: '+ symbol)
        continue




# # ## 1. Search instrument
# # symbols = ['AAPL', 'GOOG']
# # conn.searchDF(symbols)

# # ## 2. Fundamentals
# # symbols = ['AAPL', 'GOOG']
# # conn.fundamental(symbols)
# # x = conn.fundamentalDF(symbols)
# # x['fundamental']

# # ## 3. Get Instrument by CUSIP
# # cusip = '88160R101'
# # conn.fundamental(cusip)
# # conn.fundamentalDF(cusip)

# # ## 4. Get Quotes by symbol
# # symbol = 'AAPL'
# # conn.quote(symbol)
# # conn.quoteDF(symbol)

# ## 5. Get Historical Price
# """"
# periodType: The type of period to show. Valid values are day, month, year, or ytd (year to date). Default is day
# period: Valid periods by periodType (defaults marked with an asterisk):
#         day: 1, 2, 3, 4, 5, 10*
#         month: 1*, 2, 3, 6
#         year: 1*, 2, 3, 5, 10, 15, 20
#         ytd: 1*
# frequencyType: The type of frequency with which a new candle is formed. Valid frequencyTypes by periodType (defaults marked with an asterisk):
#         day: minute*
#         month: daily, weekly*
#         year: daily, weekly, monthly*
#         ytd: daily, weekly*
# frequency: The number of the frequencyType to be included in each candle. Valid frequencies by frequencyType (defaults marked with an asterisk):
#         minute: 1*, 5, 10, 15, 30
#         daily: 1*
#         weekly: 1*
#         monthly: 1*
# endDate: End date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided. Default is previous trading day.
# startDate: Start date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided.
# needExtendedHoursData: true to return extended hours data, false for regular market hours only. Default is true

# """"






# ## 6. Get option chain for an optionable Symbol
# """"
# contractType: Can be CALL, PUT, or ALL. Default is ALL.
# strikeCount: The number of strikes to return above and below the at-the-money price.
# includeQuotes: Include quotes for options in the option chain. Can be TRUE or FALSE. Default is FALSE.
# strategy: Passing a value returns a Strategy Chain. Possible values are SINGLE, ANALYTICAL 
#         (allows use of the volatility, underlyingPrice, interestRate, and daysToExpiration params to calculate theoretical values), 
#         COVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY, CONDOR, DIAGONAL, COLLAR, or ROLL. Default is SINGLE.
# interval: Strike interval for spread strategy chains (see strategy param).
# strike: Provide a strike price to return options only at that strike price.
# range: Returns options for the given range. Possible values are:
#         ITM: In-the-money
#         NTM: Near-the-money
#         OTM: Out-of-the-money
#         SAK: Strikes Above Market
#         SBK: Strikes Below Market
#         SNK: Strikes Near Market
#         ALL: All Strikes
#         Default is ALL.
# fromDate: 'Only return expirations after this date. For strategies, expiration refers to the nearest term expiration in the strategy. 
#         Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.'
# toDate: 'Only return expirations before this date. For strategies, expiration refers to the nearest term expiration in the strategy. 
#         Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.'
# volatility: Volatility to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
# underlyingPrice: Underlying price to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
# interestRate: Interest rate to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
# daysToExpiration: Days to expiration to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
# expMonth: 'Return only options expiring in the specified month. Month is given in the three character format.
#             Example: JAN
#             Default is ALL.''
# optionType: 'Type of contracts to return. Possible values are:
#         S: Standard contracts
#         NS: Non-standard contracts
#         ALL: All contracts

#         Default is ALL.''
# """"
# symbol = 'SPY'
# params = {'contractType': 'CALL',
#         'strikeCount': '5', 
#         'includeQuotes': 'FALSE',
#         'strategy': 'SINGLE',
#         'fromDate': '2020-01-20',
#         'toDate': '2020-01-31'

# }
# conn.options('AAPL', contractType=params['contractType'], strikeCount=params['strikeCount'],fromDate=params['fromDate'], toDate=params['toDate'])
# conn.optionsDF('AAPL')

# ## 7. Movers
# index = '$DJI'  ## The index symbol to get movers from. Can be $COMPX, $DJI, or $SPX.X. Click to edit the value.
# direction = 'up'  ## up or down
# change_type='percent'  # percent or value
# conn.movers(index, direction=direction, change_type=change_type)
