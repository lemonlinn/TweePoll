import tweepy
from textwrap import TextWrapper
import config

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		#print(status.text)
		status_wrapper = TextWrapper(width=140, initial_indent='', subsequent_indent='')
		try:
			my_dict = dict()
			my_dict['body'] = status_wrapper.fill(status.text)
			my_dict['isRetweet'] = status.retweeted
			my_dict['userLanguage'] = status.user.lang
			my_dict['urls'] = status.entities['urls']
			my_dict['place'] = status.place
			my_dict['followerCount'] = status.user.followers_count
			my_dict['screenName'] = status.author.screen_name
			my_dict['friendCount'] = status.user.friends_count
			my_dict['createdAt'] = status.created_at
			my_dict['messageId'] = status.id
			print(my_dict)
			
		except:
			pass

if __name__ == '__main__':
	search = "protest"
	auth = tweepy.auth.OAuthHandler(config.ckey, config.csecret)
	auth.set_access_token(config.atoken, config.asecret)
	api = tweepy.API(auth)

	tweepoll = MyStreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=tweepoll)
	stream.filter(track = [search])