# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

# FINISHED!!
X = [1] * 10
for i in range(1, len(X) - 1):
    print(i)
    X[i + 1] = X[i] + X[i - 1]


"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    word_list = list(word)
    word_logical = []
    for i in range(0, len(word_list)):
        if word_list[i] == "e":
            word_logical.append(True)
        else:
            word_logical.append(False)
    if any(word_logical):
        return False
    else:
        return True
    


"""return true if there is e in 'word', else false"""
def has_e(word):
    word_list = list(word)
    word_logical = []
    for i in range(0, len(word_list)):
        if word_list[i] == "e":
            word_logical.append(True)
        else:
            word_logical.append(False)
    if any(word_logical):
        return True
    else:
        return False
    

"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    d
    
# Experimentation.
w1 = "piggy"
w2 = "private"

w1_list = list(w1)
w2_list = list(w2)

w1_matchlog = []
for i in range(0, len(w1)):
    if w1_list[i] == any(w2_list):
        w1_matchlog.append(True)
    else:
        w1_matchlog.append(False)




"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):


"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):