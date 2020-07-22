import tweepy
from textwrap import TextWrapper
import pandas as pd
import config
import TweePoll_NLP_single
import json

MLObj = TweePoll_NLP_single.ReadyForSQL()

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api=None):
		super(MyStreamListener, self).__init__()
		self.num_tweets = 0
		self.auth = tweepy.auth.OAuthHandler(config.ckey, config.csecret)
		self.auth.set_access_token(config.atoken, config.asecret)
		self.api = tweepy.API(self.auth)
		#self.printDF = None

	def on_status(self, status):
		# status_wrapper = TextWrapper(width=140, initial_indent='', subsequent_indent='')
		# try:
		# 	if hasattr(status, "retweeted_status"):  # Check if Retweet
		# 		try:
		# 			tweet = status_wrapper.fill(status.retweeted_status.extended_tweet["full_text"].encode('utf-8'))
		# 		except AttributeError:
		# 			tweet = status_wrapper.fill(status.retweeted_status.text.encode('utf-8'))
		# 	else:
		# 		try:
		# 			tweet = status_wrapper.fill(status.extended_tweet["full_text"].encode('utf-8'))
		# 		except AttributeError:
		# 			tweet = status_wrapper.fill(status.text.encode('utf-8'))

		try:
			if hasattr(status, "retweeted_status"):  # Check if Retweet
				try:
					tweet = status.retweeted_status.extended_tweet["full_text"]
				except AttributeError:
					tweet = status.retweeted_status.text
			else:
				try:
					tweet = status.extended_tweet["full_text"]
				except AttributeError:
					tweet = status.text

			user = status.author.screen_name
			time = str(status.created_at)
			prez = MLObj.whichPrez(tweet)
			clean = MLObj.kleenex(tweet)
			NRCemo = MLObj.NRCEmo(clean)

			global printDF
			printDF = json.dumps({"tweet":tweet, "clean":clean,
				"prez":prez, "NRCEmo":NRCemo, "time":time, "username":user})

			#print(printDF)
			#yield(printDF)
			#return(printDF)
			
			#sets upper bound of tweets to grab (low for testing purposes)
			#self.num_tweets += 1
			#if self.num_tweets < 1:
				#return(True)
			#else:
				#return(False)
			return(False)
			
		except Exception as e:
			print(e)
			pass

	def main(self, regexTrump, RegexBiden):
		tweepoll = MyStreamListener()
		stream = tweepy.Stream(auth=self.api.auth, listener=tweepoll, is_async = True)
		stream.filter(track = [regexTrump, RegexBiden])
		return(printDF)


if __name__ == '__main__':
	x = MyStreamListener().main("covid @realDonaldTrump", "covid @JoeBiden")
	print(x)