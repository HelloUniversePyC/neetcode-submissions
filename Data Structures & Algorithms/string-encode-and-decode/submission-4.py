import re
class Solution:
    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for word in strs:
            output_str+=f"[{len(word)}]{word}"
        return output_str
    def decode(self, s: str) -> List[str]:
        pattern = r"\[\d+\]"
        output = re.split(pattern, s)
        output.remove("")
        return output


            
        
       
