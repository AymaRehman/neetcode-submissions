class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in sorted_strs:
                sorted_strs[sorted_word] = []

            sorted_strs[sorted_word].append(word)

        return list(sorted_strs.values())
        