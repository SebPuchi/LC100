class Solution:
    def codeFound(self, s, j):
        num = "" 

        for i in range(j, len(s)):
            if s[i].isnumeric():
                num+=s[i]
                continue
            elif s[i] == "$":
                return (True, num)
        return (False, num)

    def encode(self, strs: List[str]) -> str:
        encoded_string = '' 

        for word in strs:
            encoded_string+=(str(len(word))+ "$" + word)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            print("I", i)
            (valid, offset) = self.codeFound(s, i)
            print(valid, offset)
            if valid:
                output.append(s[i+(len(offset) +1) : i + (len(offset)+1) + int(offset)])
                i+=(len(offset) + 1 + int(offset))
            
            print(output, i)
        return output

