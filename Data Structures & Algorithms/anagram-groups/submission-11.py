class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedArray = {}

        for word in strs:
            temp = ''.join(sorted(word))
            if temp in sortedArray:
                sortedArray[temp].append(word)
            else:
                sortedArray[temp] = [word]
        return list(sortedArray.values())
            