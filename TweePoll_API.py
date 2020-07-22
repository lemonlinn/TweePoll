import tweepy
from textwrap import TextWrapper
import pandas as pd
import config
#import TweePoll_NLP
import TweePoll_NLP_single
import json

global tweet, user, time
#tweet = []
#user = []
#time = []
tweet = str()
user = str()
time = str()
MLObj = TweePoll_NLP_single.ReadyForSQL()


class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api=None):
		super(MyStreamListener, self).__init__()
		self.num_tweets = 0
		self.auth = tweepy.auth.OAuthHandler(config.ckey, config.csecret)
		self.auth.set_access_token(config.atoken, config.asecret)
		self.api = tweepy.API(self.auth)

	def on_status(self, status):
		status_wrapper = TextWrapper(width=140, initial_indent='', subsequent_indent='')
		try:
			#my_dict = dict()
			#my_dict['body'] = status_wrapper.fill(status.text)
			#my_dict['isRetweet'] = status.retweeted
			#my_dict['userLanguage'] = status.user.lang
			#my_dict['urls'] = status.entities['urls']
			#my_dict['place'] = status.place
			#my_dict['followerCount'] = status.user.followers_count
			#my_dict['screenName'] = status.author.screen_name
			#my_dict['friendCount'] = status.user.friends_count
			#my_dict['createdAt'] = status.created_at
			#my_dict['messageId'] = status.id

			if hasattr(status, "retweeted_status"):  # Check if Retweet
				try:
					#tweet.append(status_wrapper.fill(status.retweeted_status.extended_tweet["full_text"]))
					tweet = status_wrapper.fill(status.retweeted_status.extended_tweet["full_text"])
				except AttributeError:
					#tweet.append(status_wrapper.fill(status.retweeted_status.text))
					tweet = status_wrapper.fill(status.retweeted_status.text)
			else:
				try:
					#tweet.append(status_wrapper.fill(status.extended_tweet["full_text"]))
					tweet = status_wrapper.fill(status.extended_tweet["full_text"])
				except AttributeError:
					#tweet.append(status_wrapper.fill(status.text))
					tweet = status_wrapper.fill(status.text)

			#tweet.append(status_wrapper.fill(status.text))
			#user.append(status.author.screen_name)
			#time.append(str(status.created_at))
			user = status.author.screen_name
			time = str(status.created_at)
			prez = MLObj.whichPrez(tweet)
			clean = MLObj.kleenex(tweet)
			NRCemo = MLObj.NRCEmo(clean)

			printDF = json.dumps({"tweet":tweet, "clean":clean,
				"prez":prez, "NRCEmo":NRCemo, "time":time, "username":user})
			print(printDF)
			#yield printDF

			#sets upper bound of tweets to grab (low for testing purposes)
			self.num_tweets += 1
			if self.num_tweets < 10:
			#if len(tweet) < 10:
				return(True)
			else:
				return(False)
			
		except:
			pass

	def main(self, regexTrump, RegexBiden):
		#auth = tweepy.auth.OAuthHandler(config.ckey, config.csecret)
		#auth.set_access_token(config.atoken, config.asecret)
		#api = tweepy.API(auth)

		tweepoll = MyStreamListener()
		stream = tweepy.Stream(auth=self.api.auth, listener=tweepoll, is_async = True)
		stream.filter(track = [regexTrump, RegexBiden])

		#MLObj = TweePoll_NLP.ReadyForSQL()
		#prez = MLObj.whichPrez(tweet)
		#clean = MLObj.kleenex(tweet)
		#NRCemo = MLObj.NRCEmo(clean)

		#printDF = json.dumps({"tweet":tweet, "clean":clean,
			#"prez":prez, "NRCEmo":NRCemo, "time":time, "username":user})
		
		#printDF = json.dumps(({"tweet": tweet, "time":time, "UN":user}))
		#return(clean[-1])
		#return(printDF)
		#print(clean)
		#print(printDF)
		#yield(printDF)


if __name__ == '__main__':
	# MyStreamListener().main(regex="protest")
	# print(test)
	# output = MyStreamListener().main(regexTrump = "protest @realDonaldTrump",
	# 	RegexBiden = "protest @JoeBiden")
	# print(output)
	MyStreamListener().main("covid @realDonaldTrump", "covid @JoeBiden")