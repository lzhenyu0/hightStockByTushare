from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse

import time
import tushare as ts

app = Flask(__name__)
api = Api(app)

stocks = {}

def getCurrentStock(code):
    df = ts.get_realtime_quotes(code)
    df[['code','name','price','time']]
    print(df.price[0])
    return {'stock':code, 'price':df.price[0], 'name': df.name[0], 'time': df.time[0]}


def getHistoryStock(code, date):
    t = time.strftime("%Y-%m-%d", time.localtime()) 
    q = code+t+date
    if (q in stocks):
        ck = stocks[q]
        return ck

    cur = ts.get_realtime_quotes(code)
    cur[['code','name','price','time']]
    df = ts.get_hist_data(code,start=date)
    high = cur.price[0]
    if (len(df['high']) > 0):
        high = max(x for x in df['high'])
    j = {'stock':code, 'price':cur.price[0], 'name': cur.name[0], 'time': cur.time[0], 'hight':high}
    t = time.strftime("%Y-%m-%d", time.localtime()) 
    q = code+t+date
    stocks[q] = j
    return j
    
    
class Current(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('s', type=str)

    def get(self):
        data = self.parser.parse_args()
        stock = data.get('s')
        return getCurrentStock(stock)


class Max(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('s', type=str)
        self.parser.add_argument('d', type=str)

    def get(self):
        data = self.parser.parse_args()
        stock = data.get('s')
        date = data.get('d')
        return getHistoryStock(stock, date)


api.add_resource(Current, '/current')
api.add_resource(Max, '/max')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)