class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            a = [0] * 26
            for i in word:
                a[ord(i) - ord('a')] += 1
            d[tuple(a)].append(word)
        return list(d.values())