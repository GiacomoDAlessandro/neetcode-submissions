class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedArray = {}
        
        for i, word in enumerate(strs):
            wordSort = "".join(sorted(word))
            if wordSort in sortedArray:
                sortedArray[wordSort].append(word)
            else:
                sortedArray[wordSort] = [word]
        return list(sortedArray.values())