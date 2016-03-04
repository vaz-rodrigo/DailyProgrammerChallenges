# DailyProgrammerChallenges

This repo contains all of the challenges from [**r/dailyprogrammer**](http://reddit.com/r/dailyprogrammer) and also scripts used to pull challenges from the subreddit each week and to cleanup the directory of any posts that were pulled unnecessarily.

The [**post-challenges.py**](https://github.com/FreddieV4/DailyProgrammerChallenges/blob/master/post-challenges.py) script is ran via a cron job on a VPS at the end of each week, and then automatically pushes that week's challenges to this repository. **The script is pretty inefficient, but it gets the job done. If you see ways to improve it, feel free to submit a pull request!**

## Required Modules:
- praw
- subprocess
- re
- os
- pprint

**Runs on Python 3.x**


## Challenges & Solutions

See a missing challenge & missing selftext? Don't see a solution to a challenge? Submit a copy of the challenge as a directory and/or your own solution! Go ahead and fork this repo, upload your solutions to the directory for the specified challenge and submit a pull request.


-------------------------------------

This project was inspired by [**LewisJohnson**](https://github.com/LewisJohnson/dailyprogrammer), whom I collaborated with on a similar repository.
