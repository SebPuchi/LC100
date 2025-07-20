class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Psuedocode
        # Begin by couting all the freqs of each character within the input s
        # This can be up to 26
        # Withing each window, check to see what the current max freq element is
        # Next check to see if the lenght of the current string allows for k many relpacements 
        # If so, make the repalcmeents, and update, if not, change the position of the pointers to the next

