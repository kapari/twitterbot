import tweepy # for tweeting
import secrets # shhhh
import wikipedia # to parse data from wikipedia
import datetime # to get date; actual wiki page has more info than "on this day"
import random

def get_date():
    """ returns today's date as string, e.g. 'January 01' """
    today = datetime.date.today() # ex 2015-10-31
    return today.strftime("%B %d")

def get_event():
    """ returns a string 140 characters or less of a random Events item """
    this_day = wikipedia.page(get_date())
    events = this_day.section("Events") # unicode
    # split unicode into list items
    lines = events.split('\n')
    # get random item in list
    item_index = random.randrange(len(lines))
    event_text = lines[item_index]
    # tweet the whole sentence if it's short enough
    if len(event_text) <= 140:
        return event_text
    # otherwise just print the first 137 characters plus "..." = 140
    else:
        return event_text[0:137] + "..."

def tweet(message):
    """ Send tweet """
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)
    auth.secure = True
    # print("Posting message {}".format(message))
    api.update_status(status=message)

tweet(get_event())
