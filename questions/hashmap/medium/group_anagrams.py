class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]
        # Need to consider how to make an array a key, as keys need to be immutable, and arrays are not
        hashmap = {}
        for word in strs: 
            letter_count = [0]*26
            for i in range(len(word)):
                letter_count[ord(word[i]) - ord('a')] +=1
            itemKey = str(letter_count)
            if itemKey in hashmap:
                hashmap[itemKey].append(word)
            else: 
                hashmap[itemKey] = [word]
        return hashmap.values()      

