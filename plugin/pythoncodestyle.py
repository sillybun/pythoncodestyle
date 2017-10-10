import re


def style_sentence(sentence):
    if "'" in sentence:
        return sentence
    newsentence, n = re.subn('\s*,\s*', ', ', sentence)
    newsentence, n = re.subn('[ ]*\[\s*', '[', newsentence)
    newsentence, n = re.subn('\s*\]\s*', ']', newsentence)
    newsentence, n = re.subn('\s*[ ]+\s*', ' ', newsentence)
    newsentence, n = re.subn('\s*\+=\s*', ' += ', newsentence)
    newsentence, n = re.subn('\s*-=\s*', ' -= ', newsentence)
    newsentence, n = re.subn('\s*\*=\s*', ' *= ', newsentence)
    newsentence, n = re.subn('\s*\/=\s*', ' /= ', newsentence)
    newsentence, n = re.subn('\(\s*', '(', newsentence)
    newsentence, n = re.subn('\s\)', ')', newsentence)
    newsentence, n = re.subn('\s*=\s*', ' = ', newsentence)
    newsentence, n = re.subn('\s*==\s*', ' == ', newsentence)
    return newsentence


def style_code(code):
    return [style_sentence(sentence) for sentence in code]


if __name__ == '__main__':
    sentence = style_sentence('z=[1,2,3,4]')
    print(sentence) 
