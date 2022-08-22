# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:10:26 2022

@author: edwar
"""

## HOMEWORK 3

#%%
## SETUP.
# Import packages.
import os
import importlib # Import files.
import tweepy
import time


# Reset directory to location of APIs in computer.
os.chdir('C:\\Users\\edwar\\Documents\\6. Academic\\APIs')

# Access Twitter API.
twitter = importlib.import_module('start_twitter')
# API object:
api = twitter.client
# Client object:
client = twitter.actualclient

# Reset directory to location of 'hw3_answers.py' file.
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW')


#%%
# Create @WUSTLPoliSci user object.
wps = api.get_user(screen_name = '@WUSTLPoliSci')
wps.id

# Follower count.
wps.followers_count # 847 (and growing!) :(

# Friend count.
wps.friends_count # 213

#%%
# Find list of @WUSTLPoliSci twitter followers.
## Look up followers using user id.
# Follower info: IDs, screen names, and usernames.
wps_followers_info = client.get_users_followers(id = 2752940851, max_results=1000)[0]
## Just follower IDs.
wps_follower_ids = wps.follower_ids()


len(wps_followers_info)
len(wps_follower_ids)


#%%

# Three kinds of Twitter Users:
##  Layman: Users with less than 100 followers.
##  Expert: Users with 100-1000 followers.
##  Celebrity: Users with more than 1000 followers.

# Using the Twitter API, and starting with the @WUSTLPoliSci twitter user, answer the following:
##  One degree of separation:
#%%
# TODO
##  Among the followers of @WUSTLPoliSci who is the most active?

# ANSWER:
##  User ID: 452877328
##  Username: TheNjoroge
##  Screen Name: Francis Wanjiku
##  Statuses Count: 171,051


## WORK:
# How do I measure user activity?
wps.statuses_count # Number of posted tweets.

# Create empty dictionary to store info
tfa = {}
# Create ticker to keep tracker of how many people are left.
ticker = 0
# For loop to go through all followers and count number of tweets.
for i in wps_followers_info:
    try:
        ticker += 1
        print(f"{ticker} of {len(wps_followers_info)}.")
        user = api.get_user(user_id = i.id)
        tfa[f"{i.username}, {i.id}"] = user.statuses_count
    except:
        time.sleep(15*60)
# Find follower with most tweets.
most_active_follower = max(tfa, key=tfa.get)
print(most_active_follower) # TheNjoroge, 452877328
# Find number of tweets.
tfa["TheNjoroge, 452877328"] #171,051 tweets!
# Find name associated with account:
for i in wps_followers_info:
    if i.id == 452877328:
        print(i.name)
    else:
        pass
# Francis Wanjiku.

del(user)
del(ticker)
del(i)
del(tfa)
del(most_active_follower)

#%%
# TODO
##  Among the followers of @WUSTLPoliSci who is the most popular, i.e. has the greatest number of followers?

# Answers:
##  User ID: 118794370
##  Username: mariapaularomo
##  Screen Name: María Paula Romo
##  Followers count: 357,055


# How do I measure followers?
wps.followers_count # Number of followers.

# Create empty dictionary to store info
folpop = {}
# Create ticker to keep tracker of how many people are left.
ticker = 0
# For loop to go through all followers and count number of tweets.


for i in wps_followers_info:
    try:    
        ticker += 1
        print(f"{ticker} of {len(wps_followers_info)}.")
        user = api.get_user(user_id = i.id)
        folpop[f"{i.username}, {i.id}, {i.name}"] = user.followers_count
    except:
        time.sleep(15*60)
# Find follower with most followers.
most_popular_follower = max(folpop, key=folpop.get)
print(most_popular_follower)
# Find number of followers.
folpop["mariapaularomo, 118794370, María Paula Romo"] 
# Find name associated with account:
for i in wps_followers_info:
    if i.id == 118794370:
        print(i.name)
    else:
        pass

del(i)
del(user)
del(folpop)
del(most_popular_follower)
del(ticker)

#%%
# TODO
##  Among the friends of @WUSTLPoliSci, i.e. the users she is following, who are the most active layman, expert and celebrity?

# Answers:
# Layman:
##  User ID: 764260766
##  Username: usmanfalalu1
##  Screen Name: usman falalu
##  Statuses Count: 1440
    
# Expert:
##  User ID: 1064533471
##  Username: prof_nokken
##  Screen Name: Tim.
##  Statuses Count: 20352

# Celebrity:
##  User ID: 807095
##  Username: nytimes
##  Screen Name: The New York Times
##  Statuses Count: 481487

    

# WORK:
# Find friends of @WUSTLPoliSci
wps_friends_info = client.get_users_following(id = 2752940851, max_results=1000)[0]
len(wps_friends_info) #213
# This matches our friend count.
wps.friends_count # 213

# Find follower count of friends of WUSTLPoliSci.
friendpop = {}
ticker = 0
for i in wps_friends_info:
    try:    
        ticker += 1
        print(f"{ticker} of {len(wps_friends_info)}.")
        user = api.get_user(user_id = i.id)
        friendpop[i.id] = user.followers_count
    except:
        time.sleep(15*60)

# Separate into subgroups based on follower count.
layfriends = []
expertfriends = []
celebfriends = []
# Separate into subgroups.
for key in friendpop:
    if friendpop[key] < 100:
        layfriends.append(key)
    elif friendpop[key] >= 100 and friendpop[key] < 1000:
        expertfriends.append(key)
    else:
        celebfriends.append(key)
##Laymen. < 100
len(layfriends)
##Experts. 100 - 1000
len(expertfriends)
## Celebrities. > 1000
len(celebfriends)
# Sums to right number.
len(layfriends) + len(expertfriends) + len(celebfriends)


del(i)
del(user)
del(ticker)


# Find most active friends in each group.
## Layfriends:
ticker = 0
layactivity = {}
for i in layfriends:
    try:
        ticker += 1
        print(f"{ticker} of {len(layfriends)}.")
        user = api.get_user(user_id = i)
        layactivity[user.id] = user.statuses_count
    except:
        time.sleep(15*60)

most_active_lay = max(layactivity, key=layactivity.get)
# Statuses: 1440
layactivity[most_active_lay] 
# name/username.
for i in wps_friends_info:
    if i.id == most_active_lay:
        print("Name: " + i.name + "," + "Username: " + i.username)
    else:
        pass

del(i)
del(user)
del(ticker)


# expertfriends.
ticker = 0
expertactivity = {}
for i in expertfriends:
    try:
        ticker += 1
        print(f"{ticker} of {len(expertfriends)}.")
        user = api.get_user(user_id = i)
        expertactivity[user.id] = user.statuses_count
    except:
        time.sleep(15*60)

most_active_expert = max(expertactivity, key=expertactivity.get)
# Statuses: 
expertactivity[most_active_expert] 
# name/username.
for i in wps_friends_info:
    if i.id == most_active_expert:
        print("Name: " + i.name + "," + "Username: " + i.username)
    else:
        pass

del(i)
del(user)
del(ticker)


# Celebrity Friend
ticker = 0
celebactivity = {}
for i in celebfriends:
    try:
        ticker += 1
        print(f"{ticker} of {len(celebfriends)}.")
        user = api.get_user(user_id = i)
        celebactivity[user.id] = user.statuses_count
    except:
        time.sleep(15*60)

most_active_celeb = max(celebactivity, key=celebactivity.get)
# Statuses: 
celebactivity[most_active_celeb] 
# name/username.
for i in wps_friends_info:
    if i.id == most_active_celeb:
        print("Name: " + i.name + "," + "Username: " + i.username)
    else:
        pass




del(i)
del(user)
del(ticker)


#%%
# TODO
##  Among the friends of @WUSTLPoliSci who is the most popular?

# ANSWER:
    ##  User ID: 813286
    ##  Username: BarackObama
    ##  Screen Name: Barack Obama
    ##  Follower Count: 132,573,396


most_popular_friend = max(friendpop, key=friendpop.get)
print(most_popular_friend)
# Find number of followers.
friendpop[813286] 
# Find name associated with account:
for i in wps_friends_info:
    if i.id == 813286:
        print(i.name + ", " + i.username)
    else:
        pass
    
    

##  Two degrees of separation: For the following two questions, limit your search of followers and friends to laymen and experts.
#%%
# TODO
## – Among the followers of @WUSTLPoliSci and their followers, who is the most active?


# 1. Get follower IDs.
wps_follower_ids = wps.follower_ids()
len(wps_follower_ids) #853
# This matches follower count.
wps.followers_count
 # 853

# Find follower count of followers of WUSTLPoliSci.
folpop = {}
ticker = 0
for i in wps_follower_ids:   
    ticker += 1
    print(f"{ticker} of {len(wps_follower_ids)}.")
    user = api.get_user(user_id = i)
    folpop[i] = user.followers_count#### FIX

# Separate into subgroups based on follower count.
layfollowers = []
expertfollowers = []
celebfollowers = []
# Separate into subgroups.
for key in folpop:
    if folpop[key] < 100:
        layfollowers.append(key)
    elif folpop[key] >= 100 and folpop[key] < 1000:
        expertfollowers.append(key)
    else:
        celebfollowers.append(key)

# Keep only layfollowers and celebfollowers. Drop celebfollowers.
wps_follower_ids_2 = []
for i in wps_follower_ids:
    if i in layfollowers:
        wps_follower_ids_2.append(i)
    if i in expertfollowers:
        wps_follower_ids_2.append(i)
    else:
        continue
    
len(wps_follower_ids) #853
len(wps_follower_ids_2) #646

wps_follower_ids = wps_follower_ids_2

del(i)
del(user)
del(ticker)
del(folpop)
del(layfollowers)
del(expertfollowers)
del(celebfollowers)
del(wps_follower_ids_2)
del(key)

# Ticker for WUSTL followers in first for-loop
ticker1 = 0
# Ticker for WUSTL followers in second for-loop.
ticker2_outer = 0
# ticker for followers of WUSTL followers in second for-loop.
ticker2_inner = 0
# Create empty dictionary 
ffp = {}

# FIRST FOR-LOOP: append just the WUSTL followers & status count.
for i in wps_follower_ids:
    ticker1 += 1
    print(f"FOR-LOOP 1: {ticker1} of {len(wps_follower_ids)} WUSTL followers.")
    user = api.get_user(user_id = i)
    ffp[i] = user.statuses_count
        
# Duplicate ticker.
dup_tick = 0

# SECOND FOR-LOOP: for each WUSTL follower, collect their followers and status counts.
## Create OUTER for-loop:      
for i in wps_follower_ids:
    # Update ticker2_outer (WUSTL followers).
    ticker2_outer += 1
    # Reset ticker2_inner to zero.
    ticker2_inner = 0
    # Print statement informing which WUSTL follower I'm on.
    print(f"{ticker2_outer} of {len(wps_follower_ids)} WUSTL followers.")
    # Create user object for WUSTL follower 'i'
    user_outer = api.get_user(user_id = i)
    # Gather list of WUSTL follower 'i' followers.
    follower_list = user_outer.follower_ids()
    # Create INNER for-loop:
    for j in follower_list:
        # Update ticker2_inner (followers of WUSTL followers).
        ticker2_inner += 1
        # Print statement on progress.
        print(f"WUSTL FOLLOWER: {ticker2_outer} of {len(wps_follower_ids)} \nFOLLOWER'S FOL: {ticker2_inner} of {len(follower_list)}")
        # Check if follower already in ID list. Skip if already included.
        if j in ffp.keys():
            # Print that one is duplicated.
            print(f"{ticker2_outer}:{ticker2_inner} is duplicate.")
            # Update duplicate ticker.
            dup_tick += 1
            continue
        # Create user object for follower of WUSTL follower.
        user_inner = api.get_user(user_id = j)
        # Add follower of WUSTL follower 'j' + status count to ID list.
        ffp[j] = user_inner.statuses_count
        
# Find user ID with most statuses.
most_active_follower_ID = max(ffp, key=ffp.get)
# Find number of followers.
most_active_follower_statcount = ffp[most_active_follower_ID] 
most_active_follower_user = api.get_user(user_id = most_active_follower_ID)
print("Status count: ", most_active_follower_statcount)
# Find screen name associated with ID.
print("Screen Name: ", most_active_follower_user.screen_name)
# Find user name associated with ID.
print("User Name: ", most_active_follower_user.name)
#Find ID of most active person.
print("User ID: ", most_active_follower_ID)

followerfollowerpop = ffp

del(ffp)
del(dup_tick)
del(follower_list)
del(i)
del(j)
del(ticker1)
del(ticker2_inner)
del(ticker2_outer)
del(user)
del(user_inner)
del(user_outer)



# TODO
## Among the friends of @WUSTLPoliSci and their friends, who is the most active?

# Command to get list of friends.
# api.get_friend_ids(user_id = 2752940851)


# Get list of non-celeb friends.
wps_friends_info = api.get_friend_ids(user_id = 2752940851)

# Find friend count of friends of WUSTLPoliSci.
friendpop = {}
ticker = 0
for i in wps_friends_info:
    ticker += 1
    print(f"{ticker} of {len(wps_friends_info)}.")
    user = api.get_user(user_id = i)
    friendpop[i] = user.followers_count
# Separate into subgroups based on friend count.
wps_friend_ids = []
# Separate into subgroups.
for key in friendpop:
    if friendpop[key] < 100:
        wps_friend_ids.append(key)
    elif friendpop[key] >= 100 and friendpop[key] < 1000:
        wps_friend_ids.append(key)
    else:
        continue

del(friendpop)
del(ticker)
del(i)
del(user)
del(key)
del(wps_friends_info)


# Ticker for WUSTL friend in first for-loop
ticker1 = 0
# Ticker for WUSTL friend in second for-loop.
ticker2_outer = 0
# ticker for friend of WUSTL friends in second for-loop.
ticker2_inner = 0
# Create empty dictionary 
friendfriendpop = {}

# FIRST FOR-LOOP: append just the WUSTL friends & status count.
for i in wps_friend_ids:
    ticker1 += 1
    print(f"FOR-LOOP 1: {ticker1} of {len(wps_friend_ids)} WUSTL friends.")
    user = api.get_user(user_id = i)
    friendfriendpop[i] = user.statuses_count
        
# Duplicate ticker.
dup_tick = 0

# SECOND FOR-LOOP: for each WUSTL friend, collect their followers and status counts.
## Create OUTER for-loop:      
for i in wps_friend_ids:
    # Update ticker2_outer (WUSTL friends).
    ticker2_outer += 1
    # Reset ticker2_inner to zero.
    ticker2_inner = 0
    # Print statement informing which WUSTL friend I'm on.
    print(f"{ticker2_outer} of {len(wps_friend_ids)} WUSTL friends.")
    # Create user object for WUSTL friend 'i'
    user_outer = api.get_user(user_id = i)
    # Gather list of WUSTL friend 'i' friends.
    friend_list = user_outer()
    # Create INNER for-loop:
    for j in friend_list:
        # Update ticker2_inner (friends of WUSTL friends).
        ticker2_inner += 1
        # Print statement on progress.
        print(f"WUSTL FRIEND: {ticker2_outer} of {len(wps_friend_ids)} \nFRIEND'S FREN: {ticker2_inner} of {len(friend_list)}")
        # Check if friend already in ID list. Skip if already included.
        if j in friendfriendpop.keys():
            # Print that one is duplicated.
            print(f"{ticker2_outer}:{ticker2_inner} is duplicate.")
            # Update duplicate ticker.
            dup_tick += 1
            continue
        # Create user object for friend of WUSTL friend.
        user_inner = api.get_user(user_id = j)
        # Add follower of WUSTL friend 'j' + status count to ID list.
        friendfriendpop[j] = user_inner.statuses_count
        
# Find user ID with most statuses.
most_active_friend_ID = max(friendfriendpop, key=friendfriendpop.get)
# Find info on the ID of most active friend
most_active_friend_statcount = friendfriendpop[most_active_friend_ID] 
most_active_friend_user = api.get_user(user_id = most_active_friend_ID)
print("Status count: ", most_active_friend_statcount)
# Find screen name associated with ID.
print("Screen Name: ", most_active_friend_user.screen_name)
# Find user name associated with ID.
print("User Name: ", most_active_friend_user.name)
#Find ID of most active person.
print("User ID: ", most_active_friend_ID)

del(dup_tick)
del(friend_list)
del(i)
del(j)
del(ticker1)
del(ticker2_inner)
del(ticker2_outer)
del(user)
del(user_inner)
del(user_outer)



