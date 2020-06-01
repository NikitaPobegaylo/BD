# This Python file uses the following encoding: utf-8
import random

import redis
import logging
import threading
import time

from pip._vendor.distlib.compat import raw_input


def check(messages, name, forWhom):

    thread = threading.Thread(target=Check, args=(messages, name, forWhom))
    thread.start()



def Check(message, name, forWhom):
    time.sleep(10)
    mes = message.split(" ")
    count = 0
    for word in mes:
        if isSpam(word):
            count += 1
    if count > 5:
        worker.base.zrem(name, message)
        worker.base.zadd(name, message, 3)
        worker.base.zincrby("spamers", name, 1)
    else:
        worker.base.zrem(name, message)
        worker.base.zadd(name, message, 2)
    worker.base.zadd(forWhom + '_get', message, 1.0)


def Spam(message):
    list = worker.base.lrange('spam', 0, -1)
    for item in list:
        if message == str(item):
            return True
    return False

def Users(name):
    list = worker.base.smembers("Users")
    for names in list:
        if name == names:
            return True
    return False
class Worker:
    base = redis.Redis()

def matchAdmin(name):
    list = worker.base.smembers("Administrators")
    for names in list:
        if name == names:
            return True
    return False

def GotMessages(name):
    messages = worker.base.zrange(name + '_get', 0, -1, withscores=True)
    for message in messages:
        print(message)


def showMessages(name):
    messages = worker.base.zrange(name, 0, -1, withscores=True)
    for message in messages:
        print(message)


def showOnline():
    print(worker.base.hgetall(online))

def Spamers():
    print(worker.base.zrange("spamers", 0, -1, withscores=True))

def emulate():
    i = 0
    while(i < 50):
        name1 = 'User'
        rand = random.uniform(0, 2)
        if int(rand) == 0:
            name1 = name1
        elif int(rand) == 1:
            name1 = name1 + '1'
        elif int(rand) == 2:
            name1 = name1 + '2'
        name2 = 'User'

        rand = random.uniform(0, 2)
        if int(rand) == 0:
            name2 = name2
        elif int(rand) == 1:
            name2 = name2 + '1'
        elif int(rand) == 2:
            name2 = name2 + '2'
        tag = tags[int(random.uniform(0, len(tags)))]

        worker.base.zadd(name1, 'someMessage ' + tag, 1.0)
        checkSpam('someMessage ' + tag, name1, name2)
        i = i + 1

worker = Worker()
worker.base.sadd("Administrators", "Lider")
worker.base.sadd("Users", "User")
worker.base.sadd("Users", "User1")
worker.base.sadd("Users", "User2")



online = "online"

tags = ["#institute", '#db', '#session', '#mark', 'action']
pubsub = worker.base.pubsub()
for tag in tags:
    worker.base.lpush('spam', tag)
list = worker.base.lrange('spam', 0, -1)
print(list)
print("Увійти як: 1 - user, 2 - admin")
if(raw_input()) == "1":
    print("Name")
    name = raw_input()
    if matchUsers(name):
       worker.base.hset(online, name, "true")
       print("Welcome")
       while True:
            print("Option: 1 - Message, 2 - Messages, "
                  "3 - Got messages\n, 4 - Sign, 5 - Publication, 6 - Escape")
            choice = int(input())
            if choice == 1:
                print("Message: \n")
                messageSend = raw_input()
                print("To: ")
                forWhom = raw_input()
                worker.base.zadd(name, messageSend, 1.0)
                checkSpam(messageSend, name, forWhom)
            if choice == 2:
                showMessages(name)
            if choice == 3:
                showGotMessages(name)
            if choice == 4:



                print("1 - sign, other - ")
                choice = int(input())
                if choice == 1:
                    print("Name: ")
                    pub = raw_input()
                    pubsub.subscribe(pub)
                else:
                    try:

                        print(pubsub.get_message()['data'])
                    except Exception:
                        print()


            if choice == 5:
                worker.base.publish(name
                                    , raw_input())
            if choice == 6:
                worker.base.hset(online, name, "false")
                break
else:
    print("Admin ")


    name = raw_input()
    if matchHead(name):
        print("Welcome")
        print("Option: 1 - user online, 2 -  спам, 3 - emultion")
        choice = int(raw_input())
        if choice == 1:
            showOnline()
        if choice == 2:
            showSpamers()
        if choice == 3:
            emulate()



