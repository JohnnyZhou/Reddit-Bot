import fileinput
import time
import praw
from praw.exceptions import RedditAPIException

message_body_1 = "how's it going? You seem like an ecommerce expert so I hope you don't mind me reaching out." \
                 """\n\nI'm a software developer looking """ \
                 "to help make store owners' life easier. Mind if I ask you a few questions " \
                 "around how you manage inventory and the most annoying problems you're facing there?"


def send_message():
    reddit = praw.Reddit(client_id='client_id',
                         client_secret='client_secret',
                         user_agent='Outreach Bot',
                         username='username',
                         password='password')

    ## read from file
    title = "Ecommerce Question"

    # file = open("potential_outreach.txt", 'w')
    count = 0
    sent = []
    with fileinput.FileInput(files=['potential_outreach.txt'], inplace=True) as f:
        for line in f:
            if count < 20:
                data = line.split(",", 2)
                if data and len(data) > 2 and data[1] == "n":
                    name = data[0]
                    message = "Hey {}, ".format(name) + message_body_1
                    line = line.replace(",n,", ",y,")

                    try:
                        reddit.redditor(name).message(title, message)
                        sent.append(name)
                    except RedditAPIException:
                        pass

                    count += 1
                    time.sleep(5)

            print(line.rstrip("\n"))

    for person in sent:
        print(person)


if __name__ == "__main__":
    send_message()
