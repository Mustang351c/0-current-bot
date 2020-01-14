import praw
import config
import random
import os
import time
 
##defines the login and bot. runs at end of file.
def bot_login():
    print 'Logging in...'
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_se,
            user_agent = 'kemonomimi bot')
    print 'Logged in!'
 
    return r
 
def run_bot(r, comments_replied_to,
		bunnygirls = config.bunnygirls,
		catgirls = config.catgirls,
		doggirls = config.doggirls,
		foxgirls = config.foxgirls,
		horsegirls = config.horsegirls,
		wolfgirls = config.wolfgirls):
    # print comments_replied_to
    # print bunnygirls
    # print catgirls
    # print doggirls
    # print foxgirls
    # print horsegirls
    # print wolfgirls

##defines things for later. just wanted to keep the working part of the code cleaner.
    
    subreddits = r.subreddit('kemonomimicheerupbot+anime_irl+animemes+kemonomimi+nekomimi+kitsunemimi+ookamimi+usagimimi+moescape+gunime')

    exiled = r.subreddit('anime')

    trigger_phrases = ['im sad', 'im so sad', "i'm sad", "i'm so sad", 'i am sad', 'i am so sad', 'cheer me up', 'cheer him up', 'cheer her up', 'cheer them up']

    ignored_users = [r.user.me(), 'thiscatmightcheeryou', 'sneakpeekbot', '2400gbot']

    bunnygirl_reply = ('[Here](' + random.choice(bunnygirls) + ') is a '
                          'picture of a bunnygirl! Pyon! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a catgirl, doggirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    catgirl_reply = ('[Here](' + random.choice(catgirls) + ') is a '
                          'picture of a catgirl! Nya! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a bunnygirl, doggirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    doggirl_reply = ('[Here](' + random.choice(doggirls) + ') is a '
                          'picture of a doggirl! Wan Wan! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a bunnygirl, catgirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    foxgirl_reply = ('[Here](' + random.choice(foxgirls) + ') is a '
                          'picture of a foxgirl! Kon Kon! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a bunnygirl, catgirl, doggirl, horsegirl, or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    horsegirl_reply = ('[Here](' + random.choice(horsegirls) + ') is a '
                          'picture of a horsegirl! Hihin! hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a bunnygirl, catgirl, doggirl, foxgirl, or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    wolfgirl_reply = ('[Here](' + random.choice(wolfgirls) + ') is a '
                          'picture of a wolfgirl! Awoo! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Want an endless supply of kemonomimi girls? '
                          'We have them [here](https://discord.gg/GtETtcW)'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a bunnygirl, catgirl, doggirl, or foxgirl, or horsegirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

    replies = [bunnygirl_reply, catgirl_reply, doggirl_reply, foxgirl_reply, horsegirl_reply, wolfgirl_reply]

    all_reply = ('Here is a [bunnygirl](' + random.choice(bunnygirls) + 
                          '), a [catgirl](' + random.choice(catgirls) +
                          '), a [doggirl](' + random.choice(doggirls) +
                          '), a [foxgirl](' + random.choice(foxgirls) +
                          '), a [horsegirl](' + random.choice(horsegirls) + '), **AND** '
                          'a [wolfgirl](' + random.choice(wolfgirls) + ')!! '
                          'Hopefully this will cheer you up more!')

##checks inbox replies for trigger phrases

    # print 'searching replies...'

    for reply in r.inbox.comment_replies(limit=5):
        if reply.author not in ignored_users:

##various joke replies

            if ('loli' in reply.body.lower() and reply.id not in comments_replied_to):

                print 'LOLICON FOUND!!'

                reply.reply("LOLICE!!! I'd like to report a lolicon!!!")

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id + '\n')

            for lewd_trigger in ['lewd', 'ecchi']:
                if (lewd_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'Ecchi baka found'

                    reply.reply('E-Ecchi B-Ba-Baka!!')

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for all_trigger in ['all ', 'one of each', 'not enough']:
                if (all_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'all requested in reply ' + reply.id

                    reply.reply(all_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id + '\n')

##requests for specific mimis.

            for bunnygirl_trigger in ['bunnygirl', 'bunny girl', 'bunbun', 'bunny', 'bunnies', 'usagi', 'usamimi']:
                if (bunnygirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'bunnygirl requested in reply ' + reply.id

                    reply.reply(bunnygirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for catgirl_trigger in ['catgirl', 'cat girl', 'nya', 'neko']:
                if (catgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'catgirl requested in reply ' + reply.id

                    reply.reply(catgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for doggirl_trigger in ['doggirl', 'dog girl', 'inu', 'wanwan', 'wan wan']:
                if (doggirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'doggirl requested in reply ' + reply.id

                    reply.reply(doggirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for foxgirl_trigger in ['foxgirl', 'fox girl', 'kitsune', 'kon kon']:
                if (foxgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'foxgirl requested in reply ' + reply.id

                    reply.reply(foxgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for horsegirl_trigger in ['horsegirl', 'horse girl', 'uma', 'hinin']:
                if (horsegirl_trigger in reply.body.lower() and 'human' not in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'horsegirl requested in reply ' + reply.id

                    reply.reply(horsegirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for wolfgirl_trigger in ['wolfgirl', 'wolf girl', 'awoo', 'ookami']:
                if (wolfgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'wolfgirl requested in reply ' + reply.id

                    reply.reply(wolfgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

##goodbot/badbot replies.

            if ('good bot' in reply.body.lower() and reply.id not in comments_replied_to):

                #print 'Good bot found in reply ' + reply.id

                reply.reply('[Thank You! :)](https://i.imgur.com/P3GRavv.gifv)')

                print 'thanked reply ' + reply.id

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                    f.write(reply.id+ '\n')

            if ('bad bot' in reply.body.lower() and reply.id not in comments_replied_to):

                print 'TRASH WAIFU FOUND!!'

                reply.reply('[Your waifu](https://www.merriam-webster.com/dictionary/trash)')

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                    f.write(reply.id+ '\n')

##checks comments in above listed subreddit for triggers
 
    #print 'Searching last 25 comments...'

    for comment in subreddits.comments(limit=50):
        for trigger in (trigger_phrases):
             if (trigger in comment.body.lower()  and \
                comment.id not in comments_replied_to and \
                comment.author not in (ignored_users)):
 
                    #print 'Im sad found in comment' + comment.id

                    comment.reply(random.choice(replies))

                    print 'replied to comment ' + comment.id

                    comments_replied_to.append(comment.id)
         
                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(comment.id + '\n')

#checks inbox mentions for triggers

    #print 'searching mentions...'

    for mention in r.inbox.mentions(limit=5):
        for trigger in (trigger_phrases):
            if (trigger in mention.body.lower() and \
                mention.id not in comments_replied_to and \
                mention.author not in (ignored_users)):


                    mention.reply(random.choice(replies))

                    print 'Replied to mention ' + mention.id

                    comments_replied_to.append(mention.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(mention.id + '\n')
    
    #print 'Time for a cat-nap!...'

    time.sleep(60)

##reads file of comment ID's bot has replied to
def get_saved_comments():

    print 'reading comments_replied_to...'
 
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = filter(None, comments_replied_to)
 
    return comments_replied_to
 
##actually running the bot
if __name__ == '__main__':
 
    r = bot_login()
    comments_replied_to = get_saved_comments()
    
    print 'Running bot'
 
    while True:
        run_bot(r, comments_replied_to)