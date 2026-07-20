class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            length = len(strs[i])
            result += (str(length) + "#" + strs[i])
        
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        full_length = len(s)
        
        while index < full_length:
            idx = s.find("#", index)
            place_length = s[index:idx]
            length = int(place_length)
            index = idx + 1
            
            placeholder = ""
            
            placeholder = s[index:length + index]

            result.append(placeholder)

            index += length

        return result
        
        
            

