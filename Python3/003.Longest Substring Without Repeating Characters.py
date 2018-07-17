#1.暴力 596ms 13.06%
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        length = len(s)
        if (length == 0 or length == 1):
            max_len = length
        
        lens=length-1
        for i in range(lens):
            for j in range(i + 1, length):
                if s[j] in s[i:j]:
                    if j - i > max_len:
                        max_len = j - i
                    break
                elif j == lens:
                    if max_len < length- i :
                        max_len = length-i
        return max_len
#2.字典
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        maxLength=currMax=0
        length=len(s)
        for i in range(length):
            if s[i] in dic and i-dic[s[i]]-1<currMax:
                if maxLength<currMax:
                    maxLength=currMax
                currMax=i-dic[s[i]]-1
            currMax+=1
            dic[s[i]]=i
        return maxLength if currMax<maxLength else currMax


####################################################################
if 'b' in 'ab':
    print('OK')

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    length = len(s)

    if (length == 0 or length == 1):
        max_len = length

    for i in range(length - 1):
        for j in range(i + 1, length):
            if s[j] in s[i:j]:
                if j - i > max_len:
                    max_len = j - i
                break

            elif j == length - 1:
                if max_len < j - i + 1:
                    max_len = j - i + 1

    print(max_len)
    return max_len
str='abcade'
lengthOfLongestSubstring(str)
