import tweepy as tw
import pandas as pd
import numpy as np
import json

#lendo o arquivo que contem os dados de autenticação
file_json = open('twitter_tokens.json','r')
parsed_json = json.load(file_json)

api_key = parsed_json['api_key']
api_key_secret = parsed_json['api_key_secret']
access_token = parsed_json['access_token']
access_token_secret = parsed_json['access_token_secret']

#pip install TwitterSearch
#Referencias
#https://pypi;org/project/TwiiterSearch/
#https://twittersearch.readthedocs.io/en/Latest/advanced_usage_tso.html

from TwitterSearch import *

try:
    ts = TwitterSearch(
        consumer_key = api_key,
        consumer_secret = api_key_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
    )

    tso = TwitterSearchOrder()
    tso.set_keywords(['ciência de dados', 'machine leraning'], or_operator = True)
    tso.set_language('pt')

    for tweet in ts.search_tweets_iterable(tso):
        print('created_at: ', tweet['created_at'], 'User_id', tweet['id_str'], 'Tweet: ',tweet['text'])
        

        created_at = tweet['created_at']
        user_id = tweet['id_str']
        texto = tweet['text']

        with open("tweet.json",'a+') as output:

            data = {"created_at":created_at,
                    "User_id":user_id,
                    "tweet":texto}
            #print(data)
            output.write("{}\n".format(json.dumps(data)))
except TwitterSearchException as e:
    print(e)


df = pd.read_json('tweet.json',lines = True)
df.head(10)