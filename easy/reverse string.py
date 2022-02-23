st="Suyash Pathak Hello"
stri=st.split(' ')
s=''
print(stri)

for word in stri:
    wo=''.join(word[::-1])
    s=s+str(wo)+" "
print(s.strip())