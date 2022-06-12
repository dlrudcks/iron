import cgi
form = cgi.FieldStorage()
a=form.getvalue('a')
b=form.getvalue('b')
result = int(a) * int(b)
print('Contest-type: text/plain')
print()
print(f'Result:{result}')