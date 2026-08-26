class Solution:

    def encode(self, strs: List[str]) -> str:
        #Strat -> add a period
        return "".join([f"{s}‽" for s in strs])
        

    def decode(self, s: str) -> List[str]:
        return s.split("‽")[:-1]
       
