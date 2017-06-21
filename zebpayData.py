#! /usr/bin/python
import requests
import json
import csv
import time

csvfile=open('zebPayTradeVal.csv','wb')
#writer=csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)

while True:
	r=requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=INR")
	data=json.loads(r.content)
	csvfile.write(str(time.ctime())+','+str(data["buy"])+","+str(data["sell"])+"\n")
	print(str(time.ctime())+','+str(data["buy"])+","+str(data["sell"]))
	time.sleep(30)

