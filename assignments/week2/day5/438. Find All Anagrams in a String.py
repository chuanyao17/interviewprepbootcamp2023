# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/
def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len,p_len=len(s),len(p)
        s_count=[0]*26
        p_count=[0]*26
        output=[]
        for c in p:
            p_count[ord(c)-ord('a')]+=1
        
        
        for i in range(s_len):
            cur_c=s[i]
            s_count[ord(cur_c)-ord('a')]+=1
            
            if i>=p_len:
                s_count[ord(s[i-p_len])-ord('a')]-=1
            
            if s_count==p_count:
                output.append(i-p_len+1)
        
        return output