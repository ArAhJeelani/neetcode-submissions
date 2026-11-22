class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        str1 = defaultdict(int)
        str2 = defaultdict(int)    
        if (len(list(s))) != (len(list(t))):
            return False
        else:     
            for char in s:
                str1[char]+= 1
            for char in t:
                str2[char]+=1
            for keys in str1:
                if str1[keys] == str2[keys]:
                    continue
                else: 
                    return False
            return True    


        