class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myMap = dict()
        for char in s:
            if char in myMap.keys():
                myMap[char] += 1
            else:
                myMap[char] = 1
        
        for char in t:
            if char in myMap.keys():
                myMap[char] += 1
            else:
                myMap[char] = 1

        for freq in myMap.values():
            if freq == 1:
                return False
        return True
        