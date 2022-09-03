# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:33:54 2022

@author: edwar
"""

# 3._twitter_search.py


#%% Libraries/packages to import.
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
from datetime import datetime
import dateutil.parser
import unicodedata
#To add wait time between requests
import time
import sys
import time as pytime
from time import sleep
if sys.version_info[0] >= 3:
    from datetime import timezone
#!pip install osometweet
from osometweet.utils import pause_until

#%% Preliminary/Setup
# Set WD
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\Final_Project\\Data+Methodology')


#%% Import meps twitter screen name data.
meps = pd.read_csv("meps_twitter.csv")

#%% Twitter access setup.

#### 1. Save 'Bearer Token' to environment variable from twitter API file.

#### 2. Create an auth() function to retreive token from environment.
def auth():
    return os.getenv('TOKEN')

#### 3. Create headers - i.e., create function that takes bearer token, passed 
####    it for authorization, then returns headers that will be used to access the API.
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


#%% Create URL creation function.

#### 4. Create URL.
def create_url(keyword, start_date, end_date, max_results = 500):
    # 'search_url' is the link of the endpoint we want to access.
    # In this case, we use 'full-archive search endpoint' which is only available to academic researchers.
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id',
                    'tweet.fields': 'id,text,author_id,created_at,lang,public_metrics,in_reply_to_user_id',
                    'user.fields': 'id,name,username,public_metrics',
                    # IMPORTANT - next_token overcomes maximum search results limit.
                    'next_token': {}}
    return (search_url, query_params)


#%% Create connect to endpoint function.

#### 6. Connect to Endpoint.
####    Create a function that will put all of this together and connect to the endpoint.
####    The function below will send the “GET” request and if everything is correct (response code 200), it will return the response in “JSON” format.
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    # Twitter returns (in the header of the request object) how many requests you have left. 
    # Lets use this to our advantage
    remaining_requests = int(response.headers["x-rate-limit-remaining"])
    
    # If that number is one, we get the reset-time and wait until then, plus 15 seconds (your welcome Twitter).
    # The regular 429 exception is caught below as well, however, we want to program defensively, where possible.
    if remaining_requests == 1:
        buffer_wait_time = 15
        resume_time = datetime.fromtimestamp( int(response.headers["x-rate-limit-reset"]) + buffer_wait_time )
        print(f"Waiting on Twitter.\n\tResume Time: {resume_time}")
        pause_until(resume_time)  ## Link to this code in above answer
    
    # We still may get some weird errors from Twitter.
    # We only care about the time dependent errors (i.e. errors that Twitter wants us to wait for).
    # Most of these errors can be solved simply by waiting a little while and pinging Twitter again - so that's what we do.
    if response.status_code != 200:

        # Too many requests error
        if response.status_code == 429:
            buffer_wait_time = 15
            resume_time = datetime.fromtimestamp( int(response.headers["x-rate-limit-reset"]) + buffer_wait_time )
            print(f"Waiting on Twitter.\n\tResume Time: {resume_time}")
            pause_until(resume_time)  ## Link to this code in above answer

        # Twitter internal server error
        elif response.status_code == 500:
            # Twitter needs a break, so we wait 30 seconds
            resume_time = datetime.now().timestamp() + 30
            print(f"Waiting on Twitter.\n\tResume Time: {resume_time}")
            pause_until(resume_time)  ## Link to this code in above answer

        # Twitter service unavailable error
        elif response.status_code == 503:
            # Twitter needs a break, so we wait 30 seconds
            resume_time = datetime.now().timestamp() + 30
            print(f"Waiting on Twitter.\n\tResume Time: {resume_time}")
            pause_until(resume_time)  ## Link to this code in above answer

        # If we get this far, we've done something wrong and should exit
        else:
            Exception("Request returned an error: {} {}".format(response.status_code, response.text))

    # Each time we get a 200 response, lets exit the function and return the response.json
    if response.ok:
        return response.json()


#%% Pre-for loop setup.

# Create list of column names for creation of dataframe.
json_columns = ['user_id',
     'screen_name',
     'twitter_handle',
     'followers_count',
     'following_count',
     'tweet_count',
     'tweet_id',
     'tweet_timedate',
     'tweet_language',
     'tweet_text',
     'tweet_reply_count',
     'tweet_like_count',
     'tweet_quote_count',
     'tweet_totengagement',
     'mep_name',
     'mep_country',
     'mep_europarty',
     'mep_EPid'
     ]
# Create empty list of lists to collect data for mep 'i' in.
json_list = [ [] for _ in range(18)]
# Create empty DataFrame object to fill with tweet data.
tweet_data = pd.DataFrame(columns = json_columns)
# Counters to keep track of progress.
mep_counter = 0
tweet_counter = 0
maxResultsLimitHit = 0
token_counter = 0
total_tweets_collected = 0


#%% Create test subset of meps. Use 1st 3 meps.
#test_meps = meps.iloc[0:5]


#%% For-loop through all meps in the data, using screen name.

for i in range(0, len(meps)):
    tweet_counter = 0
    mep_counter += 1
    print(f"{mep_counter} of {len(meps['screen_name2'])} MEPS.")
#### 7. Define terms I want to use. 
    bearer_token = auth()
    headers = create_headers(bearer_token)
    keyword = f"from:{meps['screen_name2'][i]} -is:reply -is:retweet" 
    start_time = "2020-01-01T21:32:01.000Z"
    end_time = "2022-09-01T21:32:11.428Z"
    max_results = 500
    
#### Create 'while' loop to cycle through next_token pages.
    flag = True
    next_token = None
    current_token = 0
    
    # Check if flag is true.
    while flag:
        # Create url.
        url = create_url(keyword, start_time, end_time, max_results)
        # connect to endpoint.
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response["meta"]["result_count"]
        
        # If next_token exists (i.e., more tweets).
        if 'next_token' in json_response['meta']:
            # Save token for next call.
            next_token = json_response['meta']['next_token']
            # Add to token_counter, shows how many times I did this.
            token_counter += 1
            if result_count is not None and result_count > 0 and next_token is not None:
                current_token += 1
                # Add tweet info to list in this case.
                for j in range(0, json_response['meta']['result_count']):
                    tweet_counter += 1
                    total_tweets_collected += 1
                    if tweet_counter == 500:
                        maxResultsLimitHit += 1
                    print(f"MEPs: {mep_counter} of {len(meps['screen_name2'])}\nTWEETS: {tweet_counter} of {json_response['meta']['result_count']}\nCurrent Token: {current_token}\nTotal Tweets Collected: {total_tweets_collected}")
                    ##### ADD USER INFO (Recycles for each tweet/row).
                    # user_id.
                    json_list[0].append(json_response['includes']["users"][0]["id"])
                    # screen_name
                    json_list[1].append(json_response['includes']["users"][0]["username"])
                    # twitter_handle
                    json_list[2].append(json_response['includes']["users"][0]["name"])
                    # followers_count
                    json_list[3].append(json_response['includes']["users"][0]["public_metrics"]["followers_count"])
                    # following_count
                    json_list[4].append(json_response['includes']["users"][0]["public_metrics"]["following_count"])
                    # tweet_count
                    json_list[5].append(json_response['includes']["users"][0]["public_metrics"]["tweet_count"])
                    ##### ADD TWEET INFO (unique fr each tweet/row).
                    # tweet_id.
                    json_list[6].append(json_response["data"][j]["id"])
                    # tweet_timedate.
                    json_list[7].append(json_response["data"][j]["created_at"])
                    # tweet_language.
                    json_list[8].append(json_response["data"][j]["lang"])
                    # tweet_text.
                    json_list[9].append(json_response["data"][j]["text"])
                    # tweet_reply_count.
                    json_list[10].append(json_response["data"][j]["public_metrics"]["reply_count"])
                    # tweet_like_count.
                    json_list[11].append(json_response["data"][j]["public_metrics"]["like_count"])
                    # tweet_quote_count.
                    json_list[12].append(json_response["data"][j]["public_metrics"]["quote_count"])
                    # tweet_totengagement.
                    json_list[13].append(json_response["data"][j]["public_metrics"]["reply_count"] + json_response["data"][j]["public_metrics"]["like_count"] + json_response["data"][j]["public_metrics"]["quote_count"])
                    ##### ADD MEP INFO.
                    # mep_name.
                    json_list[14].append(meps["NAME"][i])
                    # mep_country.
                    json_list[15].append(meps["NATIONALITY"][i])
                    # mep_europarty.
                    json_list[16].append(meps["GROUP"][i])
                    # mep_EPid.
                    json_list[17].append(meps["EP id"][i])
                # Sleep to avoid limit.
                time.sleep(1)
                
        # If NO 'next_token' EXISTS.
        else:
            if result_count is not None and result_count > 0:
                current_token += 1
                # Add tweet info to list in this case.
                for j in range(0, json_response['meta']['result_count']):
                    tweet_counter += 1
                    total_tweets_collected += 1
                    if tweet_counter == 500:
                        maxResultsLimitHit += 1
                    print(f"MEPs: {mep_counter} of {len(meps['screen_name2'])}\nTWEETS: {tweet_counter} of {json_response['meta']['result_count']}\nCurrent Token: {current_token}\nTotal Tweets Collected: {total_tweets_collected}")
                    ##### ADD USER INFO (Recycles for each tweet/row).
                    # user_id.
                    json_list[0].append(json_response['includes']["users"][0]["id"])
                    # screen_name
                    json_list[1].append(json_response['includes']["users"][0]["username"])
                    # twitter_handle
                    json_list[2].append(json_response['includes']["users"][0]["name"])
                    # followers_count
                    json_list[3].append(json_response['includes']["users"][0]["public_metrics"]["followers_count"])
                    # following_count
                    json_list[4].append(json_response['includes']["users"][0]["public_metrics"]["following_count"])
                    # tweet_count
                    json_list[5].append(json_response['includes']["users"][0]["public_metrics"]["tweet_count"])
                    ##### ADD TWEET INFO (unique fr each tweet/row).
                    # tweet_id.
                    json_list[6].append(json_response["data"][j]["id"])
                    # tweet_timedate.
                    json_list[7].append(json_response["data"][j]["created_at"])
                    # tweet_language.
                    json_list[8].append(json_response["data"][j]["lang"])
                    # tweet_text.
                    json_list[9].append(json_response["data"][j]["text"])
                    # tweet_reply_count.
                    json_list[10].append(json_response["data"][j]["public_metrics"]["reply_count"])
                    # tweet_like_count.
                    json_list[11].append(json_response["data"][j]["public_metrics"]["like_count"])
                    # tweet_quote_count.
                    json_list[12].append(json_response["data"][j]["public_metrics"]["quote_count"])
                    # tweet_totengagement.
                    json_list[13].append(json_response["data"][j]["public_metrics"]["reply_count"] + json_response["data"][j]["public_metrics"]["like_count"] + json_response["data"][j]["public_metrics"]["quote_count"])
                    ##### ADD MEP INFO.
                    # mep_name.
                    json_list[14].append(meps["NAME"][i])
                    # mep_country.
                    json_list[15].append(meps["NATIONALITY"][i])
                    # mep_europarty.
                    json_list[16].append(meps["GROUP"][i])
                    # mep_EPid.
                    json_list[17].append(meps["EP id"][i])
                # Sleep to avoid limit.
                time.sleep(1)
                
            #Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        
## Create dataframe.
df = pd.DataFrame(zip(
        json_list[0],
        json_list[1],
        json_list[2],
        json_list[3],
        json_list[4],
        json_list[5],
        json_list[6],
        json_list[7],
        json_list[8],
        json_list[9],
        json_list[10],
        json_list[11],
        json_list[12],
        json_list[13],
        json_list[14],
        json_list[15],
        json_list[16],
        json_list[17]),
        columns = json_columns)

# Export to csv
df.to_csv("tweet_data.csv")
