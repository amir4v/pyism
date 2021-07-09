from app import pyism


text = open('test.html', 'r').read()

result = pyism(text)

open('out.test.html', 'w').write(result)