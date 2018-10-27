def isSilence(sentence):
    sentence = sentence.strip(' ')
    sentence = sentence.strip('\n\r\t ')
    
    if len(sentence) == 0:
        return True


print(isSilence('\n\r \t'))


