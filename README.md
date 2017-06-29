# chosen-one
_It's like choosing straws for the 21st century_

I whipped this up one night, and thought I'd make it available here for
others to enjoy.

## Overview
This program will randomly and anonymously select a person from a list of "contacts".
It works great for games like Trouble in Terrorist Town, where the traitor is the 
only one who can know that he is the traitor.

Using a provided list of contacts (names & numbers), the program uses the twilio
SMS service to notify each person on the list. Everyone gets a message, but one 
person's message will indicate that they have been chosen for whatever purpose
you are using this program for.

## Contacts list
The contacts list is a plain text file with a very simple format: The contact
name, then their 11 digit number, delimited with a tilde (~), one per line. The
contacts names can contain spaces as well as other characters (except ~), but the 
numbers must not have dashes or spaces. The number must be the full 11-digit number
including the county code, +1 for the United States. Here's an example:

```
Capt. Jean-Luc Picard~+15552346789
```
(There's an example file in the repo)

## Setup
Just get a twilio account, and plunk in your information. It should just work...
Here's a link to the twilio docs if you need help:
https://www.twilio.com/docs/libraries/python

## Example use cases
### TTT (mentioned above)
Use this to anonymously choose a traitor and start the game

### You want to start a game of tag, and no one wants to be 'it'
Don't mess around with 'nose-goes' or 'bubble-gum'! Be a big kid
and use this to choose one person to be 'it'. It doesn't matter 
if others see...

### You need a ride somewhere, but don't know which relative to ask
Customize the message string, and let a computer decide!
