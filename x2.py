s = "Feyman.txt" 

pronouns = ['i','me','you','we','my']
 
def count_words(text):
    file = open(text,"r") 

    c2 = 0
    for line in file:
        wordlist = line.split()
        for word in wordlist:
            c2 += 1
    print("Number of words in document {}".format(c2))
    return c2



def count_sentences(text):
    file = open(text,"r") 

    c1 = 0 
    for line in file:
        for char in line:
            if char == '.' or char == '?' or char == '!':
                c1 += 1
    print("Number of sentences in document {}".format(c1))
    return c1
        

def avg_words(w,s):
    a = w/s
    return print("Avwerage number of words per sentence {}".format("%.2f" % a) )



def personal_pro(text):
    file = open(text,"r") 

    c3 = 0
    for line in file:
        wordlist = line.split()
        for word in wordlist:
            if word.lower() in pronouns:
                
                c3 += 1
    print("Number of personal pronouns: {}".format(c3))
    return c3




r1 = count_words(s)
r2 = count_sentences(s)
r3 = personal_pro(s)

avg_words(r1,r2)







       

