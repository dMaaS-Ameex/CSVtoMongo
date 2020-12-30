# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:38:40 2020

@author: Rishi
"""

import pymongo
from pymongo import MongoClient
import json
import sharepy
import pandas as pd
import io



""" Input home URL here """
URL = "https://ameex.sharepoint.com"

"""   Input file url starting from '/sites' here, ending to url should be '.csv' """

FILE_URL = '/sites/I2D-Team/Shared%20Documents/DSG/4.%20Delivery/Client%20Delivery/RB/BakerySales.csv'

""" Input user email address """
SHAREPOINT_USER = 'rishabh.radhakrishnan@ameexusa.com'

""" Input Generated App-Password"""
SHAREPOINT_PASSWORD = 'fpdcgbjprdntfdfj'

s = sharepy.connect(URL, username=SHAREPOINT_USER, password=SHAREPOINT_PASSWORD)
r = s.get(URL+FILE_URL)
f = io.BytesIO(r.content)

"""Input MongoDB Database and Collection Name below """

dBName = 'sharepoint'
collectionName='bakery'
uri = 'mongodb+srv://Rishabh:25802580@cluster0.fzctt.mongodb.net/sharepoint?retryWrites=true&w=majority'
#use next line for local instance
#self.client = MongoClient("localhost", 27017, maxPoolSize=50)


#use next two lines for AWS IAM credentials (omit the previous line)

client = MongoClient(uri)


DB = client[dBName]
collection = DB[collectionName]
df = pd.read_csv(f, error_bad_lines=False)
data = df.to_dict('records')
collection.insert_many(data, ordered=False)
print("All the Data has been Exported to Mongo DB Server")




