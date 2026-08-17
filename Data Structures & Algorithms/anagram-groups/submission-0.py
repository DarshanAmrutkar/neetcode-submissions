class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = dict()
        for word in strs:
            tempWord = ''.join(sorted(word))
            if tempWord not in myMap:
                myMap[tempWord] = [word]
            else:
                myMap[tempWord].append(word)

        return [values for values in myMap.values()]
