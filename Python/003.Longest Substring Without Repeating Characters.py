class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest,start,temp = 0,0,[False for i in range(256)]
        for i,char in enumerate(s):
            if temp[ord(char)] ==False:
                temp[ord(char)] = True
            else:
                while s[start] != char:
                    temp[s[start]] = False
                    start +=1
                start +=1
            longest = max(longest,i - start + 1)
        return longest