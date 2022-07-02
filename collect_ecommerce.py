#! usr/bin/env python3
import praw

import prawcore

from Person import Person


def init():
    reddit = praw.Reddit(client_id='client_id',
                         client_secret='client_secret',
                         user_agent='Outreach Scraper',
                         username='username',
                         password='password')

    subreddit = reddit.subreddit('ecommerce')

    count = 1
    people = []

    for submission in subreddit.top("day"):
        print("**** " + str(count))
        count += 1
        # grab list of names with comments
        redditor = submission.comments[0].author if len(submission.comments) > 0 else None
        if redditor is not None:
            # comments = get_last_messages(reddit, redditor)
            people.append(Person(str(redditor), ""))

    for person in people:
        save_to_file(person, "potential_outreach.txt")


def get_last_messages(reddit, redditor):
    comments = ""

    try:
        count = 1
        for comment in reddit.redditor(redditor.name).comments.new(limit=10):
            if comment.subreddit == "ecommerce":
                comments += "[{}]".format(count) + comment.body.replace("\n", " ").replace("\r", " ") + "\n"
                count += 1
    except prawcore.exceptions.NotFound:
        print("Something went wrong for {}".format(redditor))

    comments.rstrip("\n")
    return comments


# every day I run the script. Check with a date text file too.

def save_to_file(person, filename):
    if person.name in open(filename).read():
        print(person.name + " already exists")
        return False

    with open(filename, 'a') as out:
        out.write(person.to_string() + '\n')
        print(person.name + " saved")

    return True


if __name__ == "__main__":
    init()
