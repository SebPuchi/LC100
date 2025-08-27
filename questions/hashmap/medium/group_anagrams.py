class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for i in range(len(strs)):
            current_word = strs[i]
            key = [0] * 26

            current_word.lower()
            for letter in current_word:
                key[ord(letter) -97] +=1
            key = tuple(key)
            if key in hash_map.keys():
                hash_map[key].append(current_word)
            else:
                hash_map[key] = [current_word]
        return list(hash_map.values()



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]
        # Need to consider how to make an array a key, as keys need to be immutable, and arrays are not
        hashmap = {}
        for word in strs: 
            letter_count = [0]*26
            for i in range(len(word)):
                letter_count[ord(word[i]) - ord('a')] +=1
            itemKey = tuple(letter_count)
            if itemKey in hashmap:
                hashmap[itemKey].append(word)
            else: 
                hashmap[itemKey] = [word]
        return list(hashmap.values())

