import re
import subprocess


def make(text : str):
    From = text.find('@python')+8
    to = text.find('@end', From)
    code = text[From:to]

    if code.startswith(' '):
        indent = re.search('[a-zA-Z]+', code).span(0)[0]
        code = code[indent:]
    
    code = code.replace('\n'+ ' '*indent, '\n')

    return code


def pyism(text : str):
    while('@python' in text):
        code = make(text)

        result = subprocess.getoutput(f"python3 -c \"{code}\" ")

        result = result.replace('\n', '<br>')
        # ConCat
        From = text.find('@python')
        to = text.find('@end', From)+4

        text = text[:From] + result + text[to:]
    
    return text