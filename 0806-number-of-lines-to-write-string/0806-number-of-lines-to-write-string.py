class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        curr_width=0
        for i in s:
            w=widths[ord(i)-ord('a')]
            if curr_width+w<=100:
                curr_width+=w
            else:
                lines+=1
                curr_width=w
                
        return [lines,curr_width]