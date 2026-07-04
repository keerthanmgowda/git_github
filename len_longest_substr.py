def long_substr(s: str):
    max_len=0
    start=0
    count_dict={}
    for end in range(len(s)):
        if s[end] in count_dict:
            start=max(start,count_dict[s[end]]+1)
        count_dict[s[end]]=end
        max_len=max(max_len,end-start+1)
    return max_len

a=long_substr(input("Enter a string"))
print(a)
    
