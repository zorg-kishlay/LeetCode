class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False
        pattern_word_map = {}
        word_pattern_map = {}
        
        
        for ch,wo in zip(pattern,words):
            # if pattern in map and pattern is not mapped to current word
            if ch in pattern_word_map and pattern_word_map[ch] != wo:
                return False
            
            if wo in word_pattern_map and word_pattern_map[wo] != ch:
                return False
            
            word_pattern_map[wo] = ch
            pattern_word_map[ch] = wo
        
        
        return True
            
        