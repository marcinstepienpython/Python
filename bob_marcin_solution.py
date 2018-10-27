import string

def isSilence(sentence):
    sentence = sentence.strip(' ')
    sentence = sentence.strip('\n\r\t ')
    
    if len(sentence) == 0:
        return True
    
    return False

def isQuestion(sentence):
    sentence = sentence.strip(' ')
    if sentence[-1] == '?': 
        return True
    return False

def isYelling(sentence):
    sentence = sentence.strip(' ')
    
    if not any(char.isalpha() for char in sentence):
        return False

    for char in sentence:
        if char in string.ascii_lowercase:
            return False
        
    return True

def isQuestionYelling(sentence):
    sentence = sentence.strip(' ')
    if isYelling(sentence) and sentence[-1] =='?':
        return True
    return False

def hey(sentence):
    if isSilence(sentence):
        return 'Fine. Be that way!'
    elif isQuestionYelling(sentence):
        return "Calm down, I know what I'm doing!"
    elif isQuestion(sentence):
        return 'Sure.'
    elif isYelling(sentence):
        return 'Whoa, chill out!'
    
    return 'Whatever.'
