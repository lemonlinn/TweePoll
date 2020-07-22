import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import re
global stop_words
stop_words = set(stopwords.words('english'))
NRCdata = pd.read_table("C:/Users/swagj/Documents/Cool_Data/NRC-Sentiment-Emotion-Lexicons/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt",
	delimiter='\t')

class ReadyForSQL(object):
	def whichPrez(self, var):
		"""takes list of tweets and returns list of categories"""
		tmp = re.search('(.*@realdonaldtrump.*)', var.lower())
		tmp2 = re.search('(.*@joebiden.*)', var.lower())
		if tmp and tmp2:
			prez = "both"
		elif tmp:
			prez = 'trump'
		elif tmp2:
			prez = 'biden'
		elif not tmp and not tmp2:
			prez = 'no prez'
		return(prez)

	def kleenex(self, var):
		tmp = re.sub('(https://t.co/)\w*', ' ', var)
		tmp = re.sub('@.+?\s', ' ', tmp)
		tmp = re.sub('[^a-zA-Z]+', ' ', tmp)
		tmp = re.sub('^(RT)', ' ', tmp)
		tmp = tmp.lower()
		tmp = [word for word in tmp.split() if word not in stop_words]
		tmp = ' '.join(tmp)
		return(tmp)

	def NRCEmo(self, var):
		NRClist = str()
		pos = 0
		neg = 0
		anger = 0
		antic = 0
		disgust = 0
		fear = 0
		joy = 0
		sad = 0
		surprise = 0
		trust = 0
		neutral = 0

		for t in re.split(" ", var):
			if t in list(NRCdata.word[NRCdata.emotion == 'anger']):
				anger += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'positive']):
				pos += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'negative']):
				neg += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'anticipation']):
				antic += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'disgust']):
				disgust += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'fear']):
				fear += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'joy']):
				joy += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'sad']):
				sad += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'surprise']):
				surprise += 1
			elif t in list(NRCdata.word[NRCdata.emotion == 'trust']):
				trust += 1
			else:
				pass

		tmpdict = dict({'pos':pos,
			'neg':neg, 'anger':anger, 'antic':antic, 'neutral':neutral,
			'disgust':disgust, 'fear':fear, 'joy':joy,
			'sad':sad, 'surprise':surprise, 'trust':trust})

		if all(value == 0 for value in tmpdict.values()):
			NRClist = "neutral"
		else:
			inverse = [(value, key) for key, value in tmpdict.items()]
			winner = max(inverse)[1]
			NRClist = winner
		return(NRClist)


# if __name__ == '__main__':
	# test = ["keywords that will seem", "angry abolish slavery"]
	# test2 = ReadyForSQL().NRCEmo(test)
	# print(test2)
	# for i in test:
	# 	for t in re.split(" ", i):
	# 		if t in list(NRCdata.word[NRCdata.emotion == 'anger']):
	# 			print(True)
	# 		else:
	# 			print(t)
	# print(len(list(NRCdata.word[NRCdata.emotion == 'anger'])))
	# print(len(NRCdata.word))