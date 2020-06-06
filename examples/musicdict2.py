blues = {
        "BB_King" : 1967,
        "Muddy_Waters" : 1953
    }

swing = {
        "Duke_Ellington" : 1935
}

music = {
            "jazz" : [blues, swing, "chicago", "cool", "free", "bebop", "latin"],
            "theatre" : ["opera","musical"],
        }

print(type(music)) # dict
print(music)  # print music dict
# print(music(jazz)) # Error
# print(music[jazz]) # Error
# print(music[BB_King]) # Error
# print(music["BB_King"]) # Error
# print(music["jazz"]) # Print jazz values
# del music["theatre"]
# print(music)  # print music dict
print(list(music))
print("jazz" in music)
# print(blues in music) # Error
print(len(music)) # 1
print(len(blues)) # 2

print(music["jazz"])
for x in music:
    print(x)
print(music.keys())
print(music.values())
print(music.items())

print("+++++++++++++++++++++++++++++++++++++++++++++++++")
for (k, v) in music.items():
    print(k)
    print(v)
    #print("key is "+ k+". value is "+str(v))

'''
[ (k,v),(k,v)]
'''

