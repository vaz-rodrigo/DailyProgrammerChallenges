# -*- coding: utf-8 -*-
import re
import os
import praw
from pprint import pprint

NUM_CHALLENGES = 3


def get_current_week():
	""" Gets 3 challenges, easy, intermediate, hard
	for the current week from r/dailyprogrammer
	and stores the challenge text in directories
	named after the challenge titles
	"""

	r = praw.Reddit(user_agent="dailyprogrammer-challenges")
	sub = r.get_subreddit("dailyprogrammer")

	chals = sub.get_top_from_week()
	_chals = sub.get_top_from_week()
	
	# get challenge titles & selftext
	challenge_titles = [str(x.title) for x in chals]
	del challenge_titles[0]
	challenge_text = [str(x.selftext) for x in _chals]
	del challenge_text[0]

	# cleanup titles for directory names
	title_lst = []
	for title in challenge_titles:
		t = re.sub(r'\[([0-9\-]+)\]', '', title)
		title_lst.append(t.lstrip())
	pprint(title_lst)

	# name directories after challenges
	# add challenge selftext to directories
	for i in range(NUM_CHALLENGES):
		os.system('mkdir "{}"'.format(title_lst[i]))
		f = open('challenge_text.md', 'w')
		f.write(challenge_text[i])
		f.close()
		os.system('mv challenge_text.md "{}"'.format(title_lst[i]))


	#os.system("./send-data.sh")


def get_all_submissions():
	""" Gets all submissions from the entire dailyprogrammer
	subreddit and stores their titles and selftexts 
	in order to initialize the repository
	"""
	
	r = praw.Reddit(user_agent="dailyprogrammer-all")
	sub = r.search("Challenge #", subreddit="dailyprogrammer", sort="hot", limit=1000, period='all')	
	_sub = r.search("Challenge #", subreddit="dailyprogrammer", sort="hot", limit=1000, period='all')

	#posts = sorted([re.sub(r'\[([A-Z0-9\-\/]+)\]', '', str(x.title)).lstrip() for x in sub])
	
	#_posts = posts.copy()

	# get challenge titles & selftext
	challenge_titles = [catch(str(x.title)) for x in sub] #if 'EASYeasy' in x or 'INTERMEDIATEintermediate' in x or 'HARDhard' in x]
	#del challenge_titles[0]
	challenge_text = [catch(str(x.selftext)) for x in _sub]
	#del challenge_text[0]

	# cleanup titles for directory names
	title_lst = []
	for title in challenge_titles:
		t = re.sub(r'\[([0-9\-\/\PSA\Meta]+)\]', '', title)
		title_lst.append(t.lstrip())
	print("\nTITLES length", len(title_lst))
	print("\n")
	#pprint(title_lst)

	# name directories after challenges
	# add challenge selftext to directories
	for i in range(NUM_CHALLENGES):
		os.system('mkdir "{}"'.format(title_lst[i]))
		f = open('challenge_text.md', 'w')
		f.write(challenge_text[i])
		f.close()
		os.system('mv challenge_text.md "{}"'.format(title_lst[i]))


def catch(data):
	
	try:
		print(data)
		return data
	except UnicodeEncodeError as e:	
		print("\n\n\nYOU'VE HIT THE CATCH!!\n")
		return 'trash'


if __name__ == '__main__':
	get_all_submissions()











