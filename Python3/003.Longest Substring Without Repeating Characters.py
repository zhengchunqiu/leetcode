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
