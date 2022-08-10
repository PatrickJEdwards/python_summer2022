## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    if type(txt) in [int, float]:
        raise TypeError("This is an integer or float. Input should be a single string.")
    if type(txt) not in [str]:
        raise TypeError("This is not a string. Input should be a single string.")
    txt = txt.upper()
    return txt


## reverse all characters in string
def reverse(txt):
    if type(txt) in [int, float]:
        raise TypeError("This is an integer or float. Input should be a single string.")
    if type(txt) not in [str]:
        raise TypeError("This is not a string. Input should be a single string.")
    septxt = [i for i in txt]
    septxt.reverse()
    revtxt = "".join(septxt)
    return revtxt
    

## reverse word order in string
def reversewords(txt):
    if type(txt) in [int, float]:
        raise TypeError("This is an integer or float. Input should be a single string.")
    if type(txt) not in [str]:
        raise TypeError("This is not a string. Input should be a single string.")
    sepwords = txt.split(" ")
    sepwords.reverse()
    revwords = " ".join(sepwords)
    return revwords


## reverses letters in each word
def reversewordletters(txt):
    if type(txt) in [int, float]:
        raise TypeError("This is an integer or float. Input should be a single string.")
    if type(txt) not in [str]:
        raise TypeError("This is not a string. Input should be a single string.")
    sepwords = txt.split(" ")
    output = []
    for words in sepwords:
        output.append(reverse(words))
    output  = " ".join(output)
    return output



## optional -- change text to piglatin.. google it!
#def piglatin(txt):



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.

string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

# Create nonletters exception.
class NonLettersException(Exception): 
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# use
raise NonLettersException(3)
    


# Redo `reverse` function with `try` option.
def reverse(txt):
    try:
        if type(txt) in [int, float]:
            raise TypeError("This is an integer or float. Input should be a single string.")
        if type(txt) not in [str]:
            raise TypeError("This is not a string. Input should be a single string.")
        # Raise error is `word` contains non-letters passed as strings.
        nonletters = []
        for letter in txt:
            nonletters.append(not letter.isalpha())
        if any(nonletters):
            raise NonLettersException(txt)
        septxt = [i for i in txt]
        septxt.reverse()
        out = "".join(septxt)
    except TypeError:
        print("Make sure your input is a single string, returning None")
        out = None
    except NonLettersException as e:
        raise ValueError("Your string must only contain letters! Returning None")
        out = None
    except:
        print("I caught an unexpected error! Returning None.")
        out = None
    finally:
        return out


reverse_list = []
for string in string_list:
    rev = reverse(string)
    reverse_list.append(rev)
    

