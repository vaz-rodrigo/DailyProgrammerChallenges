# Python 2. Currently learning python...

from os.path import exists 

print "Hello, what's your name?"
name = raw_input('> ')
print "How old are you?"
age = raw_input('> ')
print "What's your reddit username?"
reddit_usr = raw_input('> ')

info = """So your name is %s,\n
you are %s years old\n
and your reddit username is %s. """ % (name, age, reddit_usr)

print info

def store_info():
	print "Do you want to store this information? Y/N"
	store = raw_input('> ')

	if store == 'N':
		print "Alright, see you later!"
	elif store == 'Y':
		print "Please, type the name of the file. Remember to add the extension (.txt)"
		file =  raw_input('> ')

		if not exists(file):
			print "File doesn't exist. Creating..."
			data = open(file, 'w+')

			print "Saving your info..."
			data.write(info)

			print "Done."
		else:
			data = open(file, 'w+')

			print "Saving your info..."
			data.write(info)

			print "Done."
	else:
		print "Type 'Y' for yes, 'N' for no."
		store_info()

store_info()