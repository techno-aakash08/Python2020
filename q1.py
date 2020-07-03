#Given a string, find the length of the longest substring without repeating characters.
#Input: "abcabcbb"
#Output: 3 


NO_OF_CHARS = 256
  
def longestUniqueSubsttr(string):
    lastIndex = [-1] * NO_OF_CHARS
    n = len(string) 
    res = 0   
    i = 0
    for j in range(0, n):
        i = max(i, lastIndex[ord(string[j])] + 1);
        res =  max(res, j - i + 1)
        lastIndex[ord(string[j])] = j;
    return res
string = "abcabcbb"
print ("The input string is " + string) 
length = longestUniqueSubsttr(string) 
print ("The length of the longest non-repeating character" +
       " substring is " + str(length))
