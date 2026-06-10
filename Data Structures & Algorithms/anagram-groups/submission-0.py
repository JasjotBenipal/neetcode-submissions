class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for strings in strs:

            counting = [0] * 26

            for charac in strings:

                counting[ord(charac) - ord("a")] += 1
            
            store[tuple(counting)].append(strings)
        
        return list(store.values())