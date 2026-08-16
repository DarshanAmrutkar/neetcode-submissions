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
        
        myMap1 = dict()
        for char in t:
            if char in myMap1.keys():
                myMap1[char] += 1
            else:
                myMap1[char] = 1

        for char, freq in myMap.items():
            if char in myMap1:
                if myMap1[char] != freq:
                    return False
            else:
                return False
        return True
        