# Problem Outline:
# Given the duration of a car ride in seconds, rideDuration and a list representing the duration of songs (assuming in seconds as well):
# return a list pair [1, 2] of two song ids (their indicies in songDurations) whose COMBINED runtime is 30 seconds less than the ride duration
# There are always at least 2 songs availible and cannot pick same song twice
# if there are multiple pairs with the same total time pick the pair with the LONGEST SONG
# if two songs have the same duration select the option with the LOWEST INDEX
# if no such pair exists return [-1, -1]

def findSongs(rideDuration, songDurations):
    # init dictionary with song complement as a key and the song's index as a value
    # ex {complementDur: [1, 2]}
    complements = {}
    
    # init list to hold possible song pair information to draw from and eventually return
    # ex - [{pair: [1, 2], longestSong: 35}]
    possiblePairs = []
    
    # loop through songDurations
    for i, song in enumerate(songDurations):
        # calculate complementary song length complement = (rideDuration - 30) - song
        complementDur = rideDuration - 30 - song
        # build the dictionary
        # if complementDur exists in complementDict
        if complementDur in complements:
            # add i to complements[complementDur]
            complements[complementDur].append(i)
        # otherwise add it
        else:
            complements[complementDur] = [i]

        # find if current song has a complement in the dictionary that isn't itself
        if song in complements:
            # loop through j, complement complements[song]
            for complement in complements[song]:
                if complement == i:
                    continue
                else:
                    # add it to possible pairs
                    possiblePairs.append({"pair": [complement, i], "longestSong": max(complement, songDurations[i])})
            
    # if possible pairs list has a length
    if possiblePairs:
        def longest(pair):
            return pair["longestSong"]
        # sort by longest song
        possiblePairs.sort(key=longest)
            
        # return the pair
        return possiblePairs[-1]["pair"]
    else: 
        return [-1, -1]

# print(findSongs(90, [5, 30, 30, 55,])) # [0, 3]
# print(findSongs(90, [1,10,25,35,60,25])) # [2,3]
# print(findSongs(90, [2, 12])) # [-1, -1]
print(findSongs(135, [250,5,100,180,40,120,10])) #[1,2]
