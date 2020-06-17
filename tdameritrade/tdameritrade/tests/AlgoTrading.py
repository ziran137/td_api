import requests

endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format('GOOG')

payload = {'apikey': URLENCODED_Consumer_Key,
            'periodType': 'minute',
            'frequency': 1,
            'period':2,
            'endDate':'155615824000',
            'startDate':'1554535854000',
            'needExtendedHoursData':'true'
            }
content = requests.get(url=endpoint, params=payload)
data=content.json()


URLENCODED_REDIRECT_URI = 'http%3A%2F%2Flocalhost'
URLENCODED_Consumer_Key = 'HYCCBHZVNLQNFY4N9BB0GUUJYWOMZVWM'

'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={}&client_id={}%40AMER.OAUTHAP'.format(URLENCODED_REDIRECT_URI, URLENCODED_Consumer_Key)





###############  test functions  ###############
import tdameritrade as td
import pandas as pd
token={
  "access_token": "as+I4Am/9jXgvNQZdQUTjjv14e1IMk6LwuI/RT6WVaoHt2FXVetix6Faw7pyMZYoGICqh5Vec0rwsck57TQ8/trzR9E2sf06fW+NheCeELWldW1yJaTklTMntkmhiOrXSU+2lb4Tco2I13zfhnnGSc4s6WlpqaqrRth3WMqAh0a1FZlCKNnLeJiaid089+Zm8t9WJ13syGp0QvbDTkKFbOWaU1FhQXs9/gz6lSrxTudiPkiLWyZmSyNtQWzRU3TldI4jYWjfrUxBzTjxaRxtZp1MfrkVmJPVI5IOkcNeD/yVdRuUULg2Wwoo2wru8lhI3ncXrglDOp1keOV3prn1nShWtqllPDSosFMcUEZXvsSsicOEAgKNyiCWbaHqjM5SoMlyAzEFeqYBgx3lNtvdt0RkaOCtJfxVRkKvZQOy2kq3v23R+aHnvXeBQ7Ve8eQAge/DTp1ExdVqbtW1SKduF/tq92gD/fvHqFWSwx7vDVgP3paoj64CmOo1/vQCLbyucOKQDgLwu3KoBnnabdJBU4otTRcD8yKAx83fpq7zSHDcbAkpa100MQuG4LYrgoVi/JHHvlP0pkRWfyFDazgom5gI8/yrOwlg1cC3cwPLdvz+UYbKu3NzZ9LTWIloV7XR4nFBZ4RTYUNuK2WmLxopddSu/VegBIqsPc/JoWxpQ3UQzx8VzU/Qi9NzWaqyubpaCYRzQmeuNGruzR5gjDt4xo9WOIFhZNVPmb+YpErLZq+X3m9bbNJomWOwnAGBfZTELZbAfQYq1Xx4uZxuOHPj6ATDe3qVFotioEt6zhho5RyPF+t4VzLuWwurzlEij40aeLkCMF7D4C5+w/y9L4U52tl7yCJ+xEm04N+T/RtZ9xrWaM9dVvqnH1M3e+ptCj/r0RPu1JQo3EqUOUMjvTCNuXvrdBySDEZImhXFCacGyHQBsLTn72FeOTAvxDD86v2Q9wZPpOOyG83iUsIpGojEuG3nF4fLp8TX8v8rdHqmTar9dO/i5wyIUALLIMEGht1w/P70JI4OY1qf6A6NDEqLwBQtS6soOIex857qI7K5iTSiOQZsqtDZMOKC4+ktRXleefgj3/BMBkL0sYmDr1f9T1zf9+pce/ndJ+lK+prT+4Bd5j65FX8/Fg==212FD3x19z9sWBHDJACbC00B75E",
  "refresh_token": "TBYollq7DQfWrx91AsKm3d+MG5ENpP00LDmdTGwE/iOQ69hEn4X9A8c1yfUiVujZrTUnaUpNJJW5BpCLHZV5BQS6SLziplEOXuViXYU+VgC9GEC58YqhWeXl9IatFXKOqd2K7fYoJbkKLOcp14M45WNC7pwr2pwE3mRyaJYYSipcArTZ3ULNNsoQb5Lcfm0yanyYafIwrAzYf4JM9MhxiTp4YtYgaMRF8YuHpP7oReOUcgfjLB4cX2TYPQXtG7NT2frjJGZ/v3V5OWi9b5pratWiNIW5eOGEswj2n0Xub7VHOXuiYbBn1dsj342ZiK3r3NxifH07ce29XK8B/dQaA7jsB/zXM/rzBsXQf90tOCjL3Bozgc58TWsLP8jc9FlStsax2dHBKKU5I8SVtmS0BPORR0xfXki2iNdjcg9sbx6GbTp6qBf2312itfx100MQuG4LYrgoVi/JHHvlhn5AWowPg/YMBH7QyaB84FkL1J16BrmffNTwDK/NDoYSXZMndvhyMEMmhQqazLSxwP7MOZuGR5e6/E7nqvwRFKumJcf5WGZVAMYrp1RzA4j/jzn+DLWeEMC2lPUt4/kI2jKKrBVnAgmYjvEUeuOPOyOD9YhfDsAeka80FmdZHfeJpbeLuY2yX9/VLGklHNHF/Nys+25/1RSvg46Z8vGo17+6kImFLNnYPjL+4HDal6sITObYjh/Bei1+7jzo6NLwRGpYopb2jeq5bahaKBYLEfWyGgOHRx1xZRO5XwYC2HoPNx5oK4AcCfChuO+0doGzQD5uvGHrPODEXib/Zo4CbqXhaKVCILExyL/95uWjM/RofZUu4hb9A+3yDG2ROk7WmKbNkoA5lQnQBscoLeAgJ03FI3Y8huPJooc6dJPFlnTagJeZGAy2GPsYFls=212FD3x19z9sWBHDJACbC00B75E",
  "scope": "PlaceTrades AccountAccess MoveMoney",
  "expires_in": 1800,
  "refresh_token_expires_in": 7776000,
  "token_type": "Bearer"
}
token['accountIds'] = ['ziran1206']


c = td.TDClient(access_token=token['access_token'], accountIds=token['accountIds'])
## 1. Search instrument
symbols = ['AAPL', 'GOOG']
c.search(symbols)
c.searchDF(symbols)

## 2. Fundamentals
symbols = ['AAPL', 'GOOG']
c.fundamental(symbols)
x = c.fundamentalDF(symbols)
x['fundamental']

## 3. Get Instrument by CUSIP
cusip = '88160R101'
c.fundamental(cusip)
c.fundamentalDF(cusip)

## 4. Get Quotes by symbol
symbol = 'AAPL'
c.quote(symbol)
c.quoteDF(symbol)

## 5. Get Historical Price
""""
periodType: The type of period to show. Valid values are day, month, year, or ytd (year to date). Default is day
period: Valid periods by periodType (defaults marked with an asterisk):
        day: 1, 2, 3, 4, 5, 10*
        month: 1*, 2, 3, 6
        year: 1*, 2, 3, 5, 10, 15, 20
        ytd: 1*
frequencyType: The type of frequency with which a new candle is formed. Valid frequencyTypes by periodType (defaults marked with an asterisk):
        day: minute*
        month: daily, weekly*
        year: daily, weekly, monthly*
        ytd: daily, weekly*
frequency: The number of the frequencyType to be included in each candle. Valid frequencies by frequencyType (defaults marked with an asterisk):
        minute: 1*, 5, 10, 15, 30
        daily: 1*
        weekly: 1*
        monthly: 1*
endDate: End date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided. Default is previous trading day.
startDate: Start date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided.
needExtendedHoursData: true to return extended hours data, false for regular market hours only. Default is true

""""
symbol = 'SPY'
params = {'period': 10,
        'periodType': 'year', 
        'frequency': 1,
        'frequencyType': 'daily',
        'needExtendedHoursData': 'true'
}
        

c.history(symbol, period=params['period'], periodType=params['periodType'], frequency=params['frequency'], frequencyType=params['frequencyType'])
c.historyDF(symbol, period=params['period'], periodType=params['periodType'], frequency=params['frequency'], frequencyType=params['frequencyType'])

## 6. Get option chain for an optionable Symbol
""""
contractType: Can be CALL, PUT, or ALL. Default is ALL.
strikeCount: The number of strikes to return above and below the at-the-money price.
includeQuotes: Include quotes for options in the option chain. Can be TRUE or FALSE. Default is FALSE.
strategy: Passing a value returns a Strategy Chain. Possible values are SINGLE, ANALYTICAL 
        (allows use of the volatility, underlyingPrice, interestRate, and daysToExpiration params to calculate theoretical values), 
        COVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY, CONDOR, DIAGONAL, COLLAR, or ROLL. Default is SINGLE.
interval: Strike interval for spread strategy chains (see strategy param).
strike: Provide a strike price to return options only at that strike price.
range: Returns options for the given range. Possible values are:
        ITM: In-the-money
        NTM: Near-the-money
        OTM: Out-of-the-money
        SAK: Strikes Above Market
        SBK: Strikes Below Market
        SNK: Strikes Near Market
        ALL: All Strikes
        Default is ALL.
fromDate: 'Only return expirations after this date. For strategies, expiration refers to the nearest term expiration in the strategy. 
        Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.'
toDate: 'Only return expirations before this date. For strategies, expiration refers to the nearest term expiration in the strategy. 
        Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.'
volatility: Volatility to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
underlyingPrice: Underlying price to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
interestRate: Interest rate to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
daysToExpiration: Days to expiration to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
expMonth: 'Return only options expiring in the specified month. Month is given in the three character format.
            Example: JAN
            Default is ALL.''
optionType: 'Type of contracts to return. Possible values are:
        S: Standard contracts
        NS: Non-standard contracts
        ALL: All contracts

        Default is ALL.''
""""
symbol = 'SPY'
params = {'contractType': 'CALL',
        'strikeCount': '5', 
        'includeQuotes': 'FALSE',
        'strategy': 'SINGLE',
        'fromDate': '2020-01-20',
        'toDate': '2020-01-31'

}
c.options('AAPL', contractType=params['contractType'], strikeCount=params['strikeCount'],fromDate=params['fromDate'], toDate=params['toDate'])
c.optionsDF('AAPL')

## 7. Movers
index = '$DJI'  ## The index symbol to get movers from. Can be $COMPX, $DJI, or $SPX.X. Click to edit the value.
direction = 'up'  ## up or down
change_type='percent'  # percent or value
c.movers(index, direction=direction, change_type=change_type)
