charcount = 0
with open('Datastream.txt') as ds:
    datastream = str.strip(ds.readline())
    while True:
        char1 = datastream[charcount]
        char2 = datastream[charcount + 1]
        char3 = datastream[charcount + 2]
        char4 = datastream[charcount + 3]
        char5 = datastream[charcount + 4]
        char6 = datastream[charcount + 5]
        char7 = datastream[charcount + 6]
        char8 = datastream[charcount + 7]
        char9 = datastream[charcount + 8]
        char10 = datastream[charcount + 9]
        char11 = datastream[charcount + 10]
        char12 = datastream[charcount + 11]
        char13 = datastream[charcount + 12]
        char14 = datastream[charcount + 13]
        if len({char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14}) == 14:
            print(str(charcount+14))
            break
        else:
            charcount += 1
