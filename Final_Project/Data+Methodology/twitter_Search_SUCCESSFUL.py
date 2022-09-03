# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:37:03 2022

@author: edwar
"""

# Twitter Search SUCCESSFUL.


#%% Libraries/packages to import.
import importlib
import os
import tweepy
import time
import traceback
import csv
import pandas as pd

#%% Set up twitter stuff.

# Reset directory to location of APIs in computer.
os.chdir('C:\\Users\\edwar\\Documents\\6. Academic\\APIs')
# Access Twitter API.
twitter = importlib.import_module('start_twitter')

api = twitter.client
Api = twitter.Client
limit = api.rate_limit_status()
# 1. Save 'Bearer Token' to environment variable from twitter API file.
Client = tweepy.Client(os.environ["TOKEN"], wait_on_rate_limit=True)

#%% Set Working Directory
# Set WD
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\Final_Project\\Data+Methodology')


#%% Import meps twitter screen name data.
meps = pd.read_csv("meps_twitter.csv")

#%% Create/access preliminary variables.

# Twitter handles.
mep_handles = meps["screen_name2"].values.tolist()
# Column names.
names = ['user_id', 'screen_name', 'twitter_handle',
     'follower_count','following_count','tweet_count','tweet_id',
     'tweet_timedate','tweet_language','tweet_text','tweet_retweet_count','tweet_reply_count',
     'tweet_like_count','tweet_quote_count','tweet_totengagement',
     'mep_name','mep_country','mep_europarty','mep_EPid']

# Create empty list of lists to collect data for mep 'i' in.
#json_list = [ [] for _ in range(19)]
# Second mysterious list.
#tw = []

# Ticker variables.
#mep_counter = 0
#total_tweets_collected = 0

testhandles = mep_handles[0:5]



#%% Rune for-loop (Raduan copy)

# Set location to save all these files.
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\Final_Project\\Data+Methodology\\individual_mep_csv_files')

mep_count = 0
mep_total = len(mep_handles)
tweet_total = 0
mep_failures = 0

for handle in mep_handles:
#for handle in testhandles:
    try:
        mep_count += 1
        fname = str(handle) + '.csv'    
        with open(fname, "w", encoding = "utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = names)
            writer.writeheader()
            tw = []
            result = {}
            for tweet in tweepy.Paginator(Client.search_all_tweets,
                                          query = f'from:{handle} -is:reply -is:retweet',
                                          end_time = "2022-09-01T21:32:11.428Z",
                                          start_time = "2020-01-01T21:32:01.000Z",
                                          max_results = 500,
                                          expansions = "author_id",
                                          tweet_fields = 'id,text,author_id,created_at,lang,public_metrics,in_reply_to_user_id',
                                          user_fields = "id,name,username,public_metrics"):
                tw.append(tweet)
                time.sleep(1)
                for i in tw:
                    if i[0] is None:
                        pass
                    else:
                        try:
                            for j in i[0]:
                                tweet_total += 1
                                result = {}
                                # user_id.
                                result["user_id"] = i[1]["users"][0].id
                                # screen_name.
                                result["screen_name"] = i[1]["users"][0].username
                                # twitter_handle.
                                result["twitter_handle"] = i[1]["users"][0].name
                                # follower_count.
                                result["follower_count"] = i[1]["users"][0]["public_metrics"]["followers_count"]
                                # following_count.
                                result["following_count"] = i[1]["users"][0]["public_metrics"]["following_count"]
                                # tweet_count.
                                result["tweet_count"] = i[1]["users"][0]["public_metrics"]["tweet_count"]
                                ##### ADD TWEET INFO (unique fr each tweet/row).
                                # tweet_id.
                                result["tweet_id"] = j.id
                                # tweet_timedate.
                                result["tweet_timedate"] = j.data["created_at"]
                                # tweet_language.
                                result["tweet_language"] = j.lang
                                # tweet_text.
                                result["tweet_text"] = j.text
                                # tweet_retweet_count.
                                result["tweet_retweet_count"] = j.data["public_metrics"]["retweet_count"]
                                # tweet_reply_count.
                                result["tweet_reply_count"] = j.data["public_metrics"]["reply_count"]
                                # tweet_like_count.
                                result["tweet_like_count"] = j.data["public_metrics"]["like_count"]
                                # tweet_quote_count.
                                result["tweet_quote_count"] = j.data["public_metrics"]["quote_count"]
                                # tweet_totengagement.
                                result["tweet_totengagement"] = j.data["public_metrics"]["retweet_count"] + j.data["public_metrics"]["reply_count"] + j.data["public_metrics"]["like_count"] + j.data["public_metrics"]["quote_count"]
                                ##### ADD MEP INFO.
                                # mep_name.
                                result["mep_name"] = meps.loc[meps["screen_name2"] == handle, "NAME"].iloc[0]
                                # mep_country.
                                result["mep_country"] = meps.loc[meps["screen_name2"] == handle, "NATIONALITY"].iloc[0]
                                # mep_europarty.
                                result["mep_europarty"] = meps.loc[meps["screen_name2"] == handle, "GROUP"].iloc[0]
                                # mep_EPid.
                                result["mep_EPid"] = meps.loc[meps["screen_name2"] == handle, "EP id"].iloc[0]
                                writer.writerow(result)
                        except Exception:
                            pass
        print(f"Finished MEP {mep_count} of {mep_total} MEPs.\nTweets collected: {tweet_total}.\nFailed MEPs: {mep_failures}.\n")
    except Exception:
        mep_count += 1
        mep_failures += 1
        pass


#%% Add together function
df_list = []
for handle in mep_handles:
    fname = str(handle) + '.csv' 
    df_list.append(pd.read_csv(fname))
    
bigdataset = pd.concat(df_list)
print(len(bigdataset))

bigdataset = bigdataset.drop_duplicates(subset = "tweet_id", keep = "first")
bigdataset = bigdataset.sort_values("tweet_id", ascending = False)
print(len(bigdataset))

#%% Save to csv.

# Set higher working directory.
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\Final_Project\\Data+Methodology')

# Convert to csv.
bigdataset.to_csv("mep_tweet_data.csv")

