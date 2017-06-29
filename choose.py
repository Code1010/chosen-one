"""

SMS Chosen One Version 2.0
by Cody Burrows

It's like anonymously picking straws, but for the 21st century.
Works great for games like Trouble in Terrorist Town.

Usage:
~$ python choose.py input_file

where input_file is a plain-text document containing
entries for contacts, one per line.

Name and number are separated with the '~' symbol so names
can contain spaces, if necessary. The number should be the person's full
11-digit number, appended to +A, where A is the country code. (1 in the
USA)

Here are some examples...
US Department of Labor~+18664872365
White House~+12024561111
Jenny~+15558675309

"""

from twilio.rest import TwilioRestClient # for the important suff
import random # randomness, duh
import collections # for storing name/number pairs in an ordered dict
import os # urandom
import sys

# get your own twilio account, and enter the info here
twilio_number = "+15555555555"
account_sid = "LOL1234lasagna"
auth_token = "shhdonttellanyone"

client = TwilioRestClient(account_sid, auth_token)

# The dictionary, or address book
contacts = collections.OrderedDict()

"""

This function does the hard work of parsing the data file, 
randomly choosing a person, and notifying all of the people on
the list appropriately.

"""
def main(fname:str):

    # Parse the file to get the numbers
    print('Parsing ' + fname)
    for line in open(fname):

        # pieces will split the string into name (pos 0) and number (pos 1)
        pieces = line.split("~")

        # adds each name/number pair to a dictionary
        contacts[pieces[0]] = pieces[1]
        print("Added " + pieces[0] + ", Number: " + pieces[1])


    print('Choosing one lucky person...')

    # change the seed if you like...seems random enough to me
    random.seed(os.urandom(566))

    # murderer because this was originally intended for TTT
    murderer = random.choice(list(contacts.keys()))

    print('Notifying contacts...')
    for person in contacts.keys():
        txt = ""
        if person == murderer:
            # unfortunately, sending a text with the word 'murder' in it is
            # bad, for obvious reasons.
            txt = person + ", you are the chosen one!"
        else:
            txt = person + ", you have not been chosen :("
        
        # gooey sms stuff!
        # sends an appropriate message to each contact on the list
        message = client.messages.create(to=contacts[person], 
                  from_=twilio_number,
                  body=txt)

    # celebrate!
    print('Notified contacts...Program finished successfully!')
    exit()


"""

Serves as the entry point for this program...see the docstring at the top
for more information...

Checks args, passes them on to main

"""
if __name__ == "__main__":
    print('[[[[[[[[SMS Chosen One V.2.0]]]]]]]]')
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: ~$ python choose.py input-file")
        exit()

