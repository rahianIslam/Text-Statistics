
#Rahian Islam
s = "Feyman.txt" 

pronouns = ['i','me','you','we','my'] # this is  alist o fthe all the pronouns listed. 
 
def count_words(text):
    file = open(text,"r")  # i ahd to open files seperately for all the functions because after going through one of the rfunctions it would stop and my values wopuld be zero. 

    c2 = 0
    for line in file:
        wordlist = line.split()
        for word in wordlist:
            c2 += 1
    print("Number of words in document {}".format(c2))
    return c2
# this function gose throughv all the words as I used split function to do so and counts the number of splits and returns the number of words 


def count_sentences(text):
    file = open(text,"r") 


    c1 = 0 
    for line in file:
        for char in line:
            if char == '.' or char == '?' or char == '!':
                c1 += 1
    print("Number of sentences in document {}".format(c1))
    return c1
# this function goes through each of the lines and counts the characters that end sentences        

def avg_words(w,s):
    a = w/s
    return print("Avwerage number of words per sentence {}".format("%.2f" % a) )

# the average word per sentence is number of words divuided by sentences 
# so this function returns that value

def personal_pro(text):
    file = open(text,"r") 

    c3 = 0
    for line in file:
        wordlist = line.split()
        for word in wordlist:
            if word.lower() in pronouns: # it checks for the pronouns in text file
                
                c3 += 1
    print("Number of personal pronouns: {}".format(c3))
    return c3




r1 = count_words(s)
r2 = count_sentences(s)
r3 = personal_pro(s)

avg_words(r1,r2)







       

