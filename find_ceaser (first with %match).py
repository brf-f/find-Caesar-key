def decrypt(message, key):

    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for l in message:
        if l in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(l) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + l
    return result

def break_caesar(message):
    
    print(message)
    
    # wordlist WORDS
    shift = 0
    realWords = 0
    margin = 0.8
    
    while ( (len(message.split()) - realWords) > (len(message.split())*margin)):
        shift+=1
        
        n_message = decrypt(message, shift)
        
        print(n_message)
        
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n_words = n_message.split()
        
        for i in n_words:
            for l in i:
                if not (l.upper() in alpha):
                    i = i.replace(l, "")
                
            if i.lower() in WORDS:
                realWords +=1
    
    return  shift # the most likely shift value as an integer