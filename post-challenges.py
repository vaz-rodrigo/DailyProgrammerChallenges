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


	for i in range(NUM_CHALLENGES):
		os.system('mkdir "{}"'.format(title_lst[i]))
		f = open('challenge_text.md', 'w')
		f.write(challenge_text[i])
		f.close()
		os.system('mv challenge_text.md "{}"'.format(title_lst[i]))


	#os.system("./send-data.sh")


if __name__ == '__main__':
	get_current_week()
