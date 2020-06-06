'''
song meaning: taking the time to find grattitude and satisfaction from even the simplest moments in your day
program: counts the number of words in the lyric, and the number of times a word repeats
'''

lyrics = '''
Slow down, you move too fast
You got to make the morning last
Just kicking down the cobblestones
Looking for fun and feeling groovy
Ba da-da da-da da-da, feeling groovy

Hello lamppost, what'cha knowing
I've come to watch your flowers growin'
Ain't you got no rhymes for me?
Doo-ait-n-doo-doo, feeling groovy
Ba da-da da-da da-da, feeling groovy

I got no deeds to do, no promises to keep
I'm dappled and drowsy and ready to sleep
Let the morning time drop all its petals on me
Life, I love you, all is groovy
'''

# print(lyrics)

groovylower = lyrics.lower()

# print(groovylower.split())

groovynocomma = groovylower.replace(',', '')
groovynoq = groovynocomma.replace('?', '')

print(groovynoq)

groovylist = groovynoq.split()

# print(len(groovylist))

'''
sample dict:

# remove all commas from lyric
string.replace(',', '')

# change lyric to all lower case
string.lower()

lyricdict = {
    "slow" : 1,
    "down" : 2,
    "you" : 4
    }
'''
lyricdict = {}

for word in groovylist:
    if word not in lyricdict:
        lyricdict[word] = 1
    else: 
        lyricdict[word] += 1        
print(lyricdict)

'''
print any word repeated at least 3x

commonwords = ()
for word in groovylist:
    if lyricdict[word] >= 3:
    commonwords.append(word)
print(commonwords)
'''

'''
# try 1

commonwords = ()

for word in groovylist:
    if lyricdict[word] >= 3:
        commonwords.append(word)
print(commonwords)
'''

skipwords = ['a', 'an', 'the', 'about', 'above', 'against', 'along', 'around', 'among', 'before', 'at', 'behind', 'beneath', 'below', 'beside', 'beyond', 'between', 'by', 'during', 'down', 'except', 'from', 'for', 'inside', 'in', 'into', 'near', 'like', 'of', 'on', 'off', 'to', 'since', 'toward', 'under', 'though', 'up', 'until', 'upon', 'within', 'with'] 

for word in lyricdict:
    if lyricdict[word] >= 3 and word not in skipwords:
        print(word)
