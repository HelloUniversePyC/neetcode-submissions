class Solution:
    def isValid(self, s: str) -> bool:
        remaining_chars = []
        pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
        }
        for char in s:
            if char in pairs.keys():
                remaining_chars.append(char)
            elif (
                (char == ")" and remaining_chars and remaining_chars[-1] == "(")
                or (char == "]" and remaining_chars and remaining_chars[-1] == "[")
                or (char == "}" and remaining_chars and remaining_chars[-1] == "{")
            ):
                remaining_chars.pop()
            else:
                return False
        return not remaining_chars

            
        