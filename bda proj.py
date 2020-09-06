import re
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
from pymongo import MongoClient
class TwitterClient(object):
    def __init__(self):
        consumer_key = 'zIRwata48Xlo2g71iVgGqYt3f'
        consumer_secret = 'K4qxeT2s0UyKqHHRN4C5GAdlDYj4ulm6bm8t1isdzhxeyiL38A'
        access_token = '1253991681743032320-cXwwylG0WIbOhgWyu1qq24GLGuiZV8'
        access_token_secret = 'eP0NmIwiWpASAXAfL8whSRWkmrmwK2zHvXnxRpBl3hkop'
        client=MongoClient()
        db=client['tweets_db']
        coll=db.coll
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            self.auth.set_access_token(access_token, access_token_secret)  
                        self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 

    def get_tweet_sentiment(self, tweet): 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        if analysis.sentiment.polarity > 0:
                        return 'positive'
        elif analysis.sentiment.polarity == 0: 
                        return 'neutral'
        else: 
            return 'negative'

        def get_tweets(self, query, count = 10):
                all_tweets=[]
                try:
                        api=tweepy.API(self.auth,timeout=15)
                        for tweet_object in tweepy.Cursor(api.search,q=query+"- filter:retweets",lang='en',result_type='recent').items(35):
                                tweet_dict['text']=tweet_object.text
                                tweet_dict['sentiment']=self.get_tweet_sentiment(tweet_object.text)
                                if tweet_object.retweet_count>1000:
                                        tweet_dict['sentiment']='positive'
                                if tweet_object.retweet_count>0:
                                        if tweet_dict not in all_tweets:
                                                all_tweets.append(tweet_dict)
                                else:
                                        all_tweets.append(tweet_dict)

                        return all_tweets

                except tweepy.TweepError as e:
                        # print error (if any) 
                        print("Error : " + str(e)) 
        def store_tweets(self):
            for t in self.tweet_dict:




def main(): 
        api = TwitterClient()
        tweets = api.get_tweets(query = 'Corona Virus')
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        neutral=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
        #print(neutral)
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
        p=len(ptweets)
        n=len(ntweets)
        a=len(tweets)
        print("Neutral tweets percentage: {} %".format(100*((a-p-n)/a)))
        #print("\n\nPositive tweets:") 
        for tweet in ptweets:
                print(tweet['text']) 

        #print("\n\nNegative tweets:") 
        #for tweet in ntweets: 
                #print(tweet['text']) 

if __name__ == "__main__": 
        main() 
