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
    realWords = []
    total = 26
    
    for c in range(total):
        shift+=1
        realWords.append(0)
        
        n_message = decrypt(message, shift)
        
        print(n_message)

        n_words = n_message.split()
        
        for i in n_words:
            for l in i:
                if not (l.upper() in alpha):
                    i = i.replace(l, "")
                
            if i.lower() in WORDS:
                realWords[c] +=1
    
    best_case = realWords.index(max(realWords)) 
    return  best_case # the most likely shift value as an integer