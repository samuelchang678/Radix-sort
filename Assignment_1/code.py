"""
@author: Samuel Chang Chew Leong
@since: 15/8/2019
@modified: 23/582019
"""

import math


def countingSort(my_list, target):
    """
    this function performs counting sort for alphabets
    pre_condition: list is not empty
    post_condition: none
    param: list, position of string
    return: sorted list
    time_complexity = best case = worst case  because every steps require one step only which is O(TM), T is total words
                      and M is the length of longest word
    """
    count = [0 for i in range(26)]
    position = [0 for i in range(26)]
    output = [0 for i in range(len(my_list))]
    if len(my_list) > 1:
        for i in range(len(my_list)):
            count[ord(my_list[i][0][target]) - 97] += 1
    position[0] = 0
    for i in range(1, len(position)):
        position[i] = position[i - 1] + count[i - 1]
    for i in range(len(my_list)):
        key = my_list[i][0]
        pos=0
        index = ord(my_list[i][0][target]) - 97
        if count[index] != 0:
            pos = position[index]
        position[index] += 1
        output[pos] = my_list[i]

    return output


def radixSortNumbers(array):
    """
    this function performs counting sort for ids of the songs
    pre_condition: list is not empty
    post_condition: none
    param: list
    return: sorted list
    time_complexity = best case = worst case  because every steps require one step only which is O(TN), T is total words
                      and N is the largest number
    """
    maxLen = -1
    for number in array:
        numLen = int(math.log10(int(number[1])+1)) + 1
        if numLen > maxLen:
            maxLen = numLen
    buckets = [[] for i in range(0, 10)]
    for digit in range(0, maxLen):
        for number in array:
            x=int(number[1])+1
            buckets[int(x/ 10**digit % 10)].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array


def longestWord(my_list):
    """
    this function return the length of the longest string
    pre_condition: list is not empty
    post_condition: none
    param: list
    return: length of longest string
    time_complexity = best case = worst case  because every steps require one step only which is O(T), T is total words
    """
    my_max = 0
    # find the maximum element
    for k in range( len(my_list)):
        (lyric, id) = my_list[k]
        if len(lyric) > len(my_list[my_max][0]):
            my_max = k
    max_length = len(my_list[my_max][0])
    return max_length

def BinarySearch(array, l, r, x):
    """
    this function performs binary search
    pre_condition: list is not empty
    post_condition: none
    param: list, position of string
    return: sorted list
    time_complexity = best case O(1) where the x is in the middle
                      worst case is O(log U) where U is the number of elements(lines)
    """
    if r >= l:
        mid = l + (r - l) // 2
        if array[mid][0] == x:
            return array[mid][1]
        elif array[mid][0] > x:
            return BinarySearch(array, l, mid - 1, x)
        else:
            return BinarySearch(array, mid + 1, r, x)
    else:
        return "Not found"

def process(filename):
    """
    this function takes in a file and sort the lyrics alphabetically
    pre_condition: file is not empty
    post_condition: none
    param: file that contain songs
    return: file with sorted lyrics
    time_complexity = best case = worst case  because every steps require one step only which is O(TM), T is total words
                      and M is the length of the longest word
    """
    x = open(filename, "r")
    words_from_songs=[]
    for line in x:
        array =line.split(":")
        songid= array[0]
        lyrics=array[1]
        lyrics=lyrics.replace("\n", "")
        lyrics=lyrics.split(" ")
        for i in range(len(lyrics)):
            words_from_songs.append((lyrics[i],songid))
    words_from_songs=radixSortNumbers(words_from_songs)
    max1 = longestWord(words_from_songs)
    counting = []
    for _ in range(max1+1):
        counting.append([])
    for k in range(len(words_from_songs)-1,0,-1):
        counting[len(words_from_songs[k][0])].append(words_from_songs[k])
    new_list = []
    # for i in range(len(counting)-1,0,-1):
    #     for k in range(len(counting[i])):
    #         new_list.insert(0,counting[i][k])
    # for i in range(len(counting) - 1, 0, -1):
    #     new_list = countingSort(new_list, i - 1)

    for i in range(len(counting)-1,0,-1):
        for k in range(len(counting[i])):
            new_list.insert(0,counting[i][k])
        new_list = countingSort(new_list,i-1)
    y = open("sorted_words.txt","w")
    for i in range(len(new_list)):
        y.write(str(new_list[i][0])+":"+str(new_list[i][1]+"\n"))


def collate(filename):
    """
    this function removes repeated words and concatenate the ids together
    pre_condition: file is not empty
    post_condition: none
    param: list
    return: sorted list with replicated lyrics removed
    time_complexity = best case = worst case  because every steps require one step only which is O(TM), T is total words
                      and M is the length of the longest word
    """
    x=open(filename,"r")
    total_words=[]
    for line in x:
        line=line.strip("\n")
        line=line.split(":")
        if len(total_words)<1:
            total_words.append(line)
        else:
            x= len(total_words)
            if line[0] == total_words[x-1][0]:
                if int(line[1]) > int(total_words[x-1][len(total_words[x-1])-1]):
                    total_words[x-1].append(line[1])
            else:
                total_words.append(line)
    y = open("collated_ids.txt", "w")
    # for i in range(len(total_words)):
    #     if len(total_words[i])<3:
    #         total_words[i]=":".join(total_words[i])+"\n"
    #     else:
    #         id=" ".join(total_words[i][1:])
    #         total_words[i]=total_words[i][0]+":"+id+"\n"
    # y.writelines(total_words)
    for i in range(len(total_words)):
        id=""
        for j in range(1,len(total_words[i])):
            id=id +total_words[i][j] +" "
        y.write(str(total_words[i][0]) + ":" +str(id) + "\n")

def lookup(collated_file,query_file):
    """
    this function takes query words in and return ids of the word match with the query word
    pre_condition: file is not empty
    post_condition: none
    param: lyricsfile and queryfile
    return: sorted list with replicated lyrics removed
    time_complexity = best case = worst case  because every steps require one step only which is O(q x MlogU+P) ,
                      where P is the total number of IDs in the query file and U number of lines in lyrcisfile
                      M is the number of query words and logU the time for binary search
    """
    x=open(query_file,"r")
    query=[]
    for i in x:
        i=i.replace("\n","")
        query.append(i)
    y=open(collated_file,"r")
    collection=[]
    for i in y :
        i=i.replace("\n","")
        i=i.split(":")
        collection.append(i)
    answer=[]
    for i in range(len(query)):
        answer.append(BinarySearch(collection,0,len(collection)-1,query[i]))
    y = open("song_ids.txt", "w")
    for i in range(len(answer)):
        y.write(str(answer[i]) + "\n")




process("example_songs.txt")
collate("sorted_words.txt")
# lookup("collated_ids.txt","example_queries.txt")