import tweepy
import time

CONSUMER_KEY = 'bnMFVYAWM2GS1I9gvntxaaqFX'
CONSUMER_SECRET = '51pMacJarXxDRzuUtyoSkIVWaaudQg1oWc04vRlh6kJcq6lbxg'
ACCESS_KEY = '1153294143491379200-7AF1AR1INCIQaQEblgqoRwYj2BY6lb'
ACCESS_SECRET = 'h3OTCaHhpUULRzhuPZIAi86wRYjsMgQMmqiA9EpwGqYm0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
latestId = 1

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = f_read.read().strip()
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)


while True:
    print("Finding Tweets")
    try:
        while True:
            for tweet in tweepy.Cursor(api.search, q='%23100DaysOfCode').items(1):
                if ('RT @' not in tweet.text):
                    if tweet.id != last_seen_id:
                        last_seen_id = tweet.id
                        store_last_seen_id(last_seen_id, FILE_NAME)
                        print(str(tweet.id) + " - " + tweet.text)
                        print("Retweeting tweet")
                        api.retweet(tweet.id)
                        time.sleep(20)
    except Exception as e:
        print(e)
