class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = '' 

        for word in strs:
            encoded_string+=(str(len(word))+ "$" + word)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        for i in range(len(s)):
            if s[i].isnumeric() and i+1< len(s) and s[i+1] == "$":
                print(s[i], s[i+1])
                output.append(s[i+2 : i + 2 + int(s[i])])
                i+=(1 + int(s[i]))
        return output

