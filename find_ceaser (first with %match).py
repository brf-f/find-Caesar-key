alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(message, key):

    result = ""

    for l in message.upper():
        if l in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            result = result + alpha[(alpha.find(l) - key) % len(alpha)]
        else:
            result = result + l
    return result

def break_caesar(message):
    
    print("Decrypting: "+message+"\n//")
    
    # wordlist WORDS
    shift = -1
    realWords = 0
    margin = 0.8
    
    while ( (len(message.split()) - realWords) > (len(message.split())*margin)):
        shift+=1
        
        n_message = decrypt(message, shift)
        
        print(n_message)
        
        n_words = n_message.split()
        
        for i in n_words:
            for l in i:
                if not (l.upper() in alpha):
                    i = i.replace(l, "")
                
            if i.lower() in WORDS:
                realWords +=1
    
    return  shift # the most likely shift value as an integer