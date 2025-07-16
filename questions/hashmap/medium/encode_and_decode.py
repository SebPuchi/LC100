class Solution:
    def codeFound(self, s, i):
        num = "" 
        for i in range(i, len(s)):
            print("NUM", num)
            if s[i].isnumeric():
                num+=s[i]
                continue
            elif s[i] == "$":
                print("NUM", num)
                return (True, num)
            return (False, num)
        return (False, num)



    def encode(self, strs: List[str]) -> str:
        encoded_string = '' 

        for word in strs:
            encoded_string+=(str(len(word))+ "$" + word)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        for i in range(len(s)):
            (valid, offset) = self.codeFound(s, i)
            print(valid, offset)
            if valid:
                output.append(s[i+2 : i + 2 + int(offset)])
                i+=(1 + int(offset))
        return output


