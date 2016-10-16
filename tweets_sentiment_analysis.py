#import dependencies
import tweepy
from textblob import TextBlob
import csv

#authenticate
consumer_key = "" #Consumer Key Here
consumer_secret = "" #Consumer Secret Here

access_token = "" #Access Token Here
access_token_secret = "" #Access Token Secret Here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('Nepal')


with open('sentiment_results.csv', 'w') as csvfile:
	writer=csv.writer(csvfile, delimiter='\t',lineterminator='\n',)
	for tweet in public_tweets:
		tweet_message = tweet.text
		analysis = TextBlob(tweet_message)
		tweet_message = tweet_message.replace(",", "")	#Remove all commas else formating error occurs if any tweet contains a comma
		tweet_message = tweet_message.encode("utf-8")	#to support unicode characters in case a tweet contains one
		if(analysis.sentiment.polarity > 0):
			sentiment = "Positive"
		else:
			sentiment = "Negative"
		writer.writerow([tweet_message, sentiment])