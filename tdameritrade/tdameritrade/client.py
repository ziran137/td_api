import os
import requests
import pandas as pd
from datetime import datetime
import json
from tdameritrade.urls import ACCOUNTS, ACCOUNTS_POST_ACCESS, INSTRUMENTS, QUOTES, SEARCH, HISTORY, OPTIONCHAIN, MOVERS

class TDClient(object):
    ## The token endpoint returns an access token along with an optional refresh token.
    def refresh_access_token(self):
        return requests.post(ACCOUNTS_POST_ACCESS,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data = {'grant_type': 'refresh_token',
                        'refresh_token': self._refresh_token,
                        'access_type': 'offline ',
                        'code': '',
                        'client_id': self._api_key,
                        'redirect_uri': ''
                        }).json()

    def __init__(self, api_key=None, refresh_token=None, access_token=None, accountIds=None):
        self._api_key = api_key
        self._refresh_token = refresh_token
        self._access_token = self.refresh_access_token()['access_token']
        self._accountIds = accountIds or []
    
    ## authentication
    def _headers(self):
        return {'Authorization': 'Bearer ' + self._access_token}
    



    def accounts(self, positions=False, orders=False):
        ret = {}

        if positions or orders:
            fields = '?fields='
            if positions:
                fields += 'positions'
                if orders:
                    fields += ',orders'
            elif orders:
                fields += 'orders'
        else:
            fields = ''

        if self._accountIds:
            for acc in self._accountIds:
                resp = requests.get(ACCOUNTS + str(acc) + fields, headers=self._headers())
                if resp.status_code == 200:
                    ret[acc] = resp.json()
                else:
                    raise Exception(resp.text)
        else:
            resp = requests.get(ACCOUNTS + fields, headers=self._headers())
            if resp.status_code == 200:
                for account in resp.json():
                    ret[account['securitiesAccount']['accountId']] = account
            else:
                raise Exception(resp.text)
        return ret

    def accountsDF(self):
        return pd.io.json.json_normalize(self.accounts())
    
    ## Search or retrieve instrument data, including fundamental data.
    def search(self, symbol, projection='symbol-search'):
        return requests.get(SEARCH,
                            headers=self._headers(),
                            params={'symbol': symbol,
                                    'projection': projection}).json()
    ## in dataframe
    def searchDF(self, symbol, projection='symbol-search'):
        ret = []
        dat = self.search(symbol, projection)
        for symbol in dat:
            ret.append(dat[symbol])
        return pd.DataFrame(ret)

    def fundamental(self, symbol):
        return self.search(symbol, 'fundamental')

    def fundamentalDF(self, symbol):
        return self.searchDF(symbol, 'fundamental')
    
    ## Get an instrument by CUSIP
    def instrument(self, cusip):
        return requests.get(INSTRUMENTS + str(cusip),
                            headers=self._headers()).json()

    def instrumentDF(self, cusip):
        return pd.DataFrame(self.instrument(cusip))
    
    ## Get quote for one or more symbols
    def quote(self, symbols):
        return requests.get(QUOTES,
                            headers=self._headers(),
                            params={'symbol': symbols.upper()}).json()

    def quoteDF(self, symbol):
        x = self.quote(symbol)
        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(self, symbol, **kwargs):
        return requests.get(HISTORY % symbol,
                            headers=self._headers(),
                            params=kwargs).json()

    def historyDF(self, symbol, **kwargs):
        x = self.history(symbol, **kwargs)
        df = pd.DataFrame(x['candles'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        return df
    
    ## Get option chain for an optionable Symbol
    def options(self, symbol, **kwargs):
        return requests.get(OPTIONCHAIN,
                            headers=self._headers(),
                            params={'symbol': symbol.upper(), **kwargs}).json()

    def optionsDF(self, symbol):
        ret = []
        dat = self.options(symbol)
        for date in dat['callExpDateMap']:
            for strike in dat['callExpDateMap'][date]:
                ret.extend(dat['callExpDateMap'][date][strike])
        for date in dat['putExpDateMap']:
            for strike in dat['putExpDateMap'][date]:
                ret.extend(dat['putExpDateMap'][date][strike])

        df = pd.DataFrame(ret)
        for col in ('tradeTimeInLong', 'quoteTimeInLong', 'expirationDate', 'lastTradingDay'):
            df[col] = pd.to_datetime(df[col], unit='ms')
        return df

    def movers(self, index, direction='up', change_type='percent'):
        return requests.get(MOVERS % index,
                            headers=self._headers(),
                            params={'direction': direction,
                                    'change_type': change_type}).json()

    def orders(self, account_id, order):
        return requests.post(ACCOUNTS + account_id + "/orders",
                             headers=self._headers(),
                             json=order).json()
