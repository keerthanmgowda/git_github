def valid_par(s:str):
    mapp={")":"(","}":"{","]":"["}
    st=[]
    for char in s:
        if char in mapp:
            if st and st[-1]==mapp[char]:
                st.pop()
            else:
                return False
        else:
            st.append(char)
    return not st
print(valid_par(input("Enter parenthesis : ")))

