def hey(sentence):
    sentence = sentence.strip()
    
    if sentence == '':
        return 'Fine. Be that way!'
    
    elif sentence.isupper() and sentence.endswith('?'):
        return "Calm down, I know what I'm doing!"
    
    elif sentence.endswith('?'):
        return 'Sure.'
    
    elif sentence.isupper():
        return 'Whoa, chill out!'
    
    else:
        return 'Whatever.'



