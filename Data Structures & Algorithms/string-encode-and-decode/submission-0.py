class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []
        for string in strs:
            to_list = list(string)
            new_list = []
            for letter in to_list:
                new_list.append(letter)
            new_list.append('t')
            new_list.append('5')
            new_list.append('#')
            new_strs.append(''.join(new_list))
        return ''.join(new_strs)
    def decode(self, s: str) -> List[str]:
        old_strs = []
        char1 = ''
        char2 = ''
        char3 = ''
        current_word = []
        for char in list(s):
            current_word.append(char)
            char1 = char2
            char2 = char3
            char3 = char
            if char1 == 't' and char2 == '5' and char3 == '#':
                current_word.pop()
                current_word.pop()
                current_word.pop()
                old_strs.append(''.join(current_word))
                current_word.clear()

        return old_strs

                
                
