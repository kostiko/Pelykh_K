def filter_words(st):
    # Your code here.
    a= ' '.join(st.split())
    s=a.lower()
    return print(s[0].upper()+s[1:len(s)])
filter_words("HELLO world!")