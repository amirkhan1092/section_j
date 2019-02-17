a = 'hello python'
h = []
st = ''
for k in a:
    num = a.count(k)
    if k in st:
        h.append(None)
    else:
        h.append(num)
        st += k

print('String', list(a), end='')
print('list  ', h)
