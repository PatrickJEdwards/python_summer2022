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

shout("SHOUT LOUD AND CLEAR")
shout(5)
shout(["Happy", "Days"])

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
    
reverse("abcd")
reverse("SHOUT LOUD AND CLEAR")
reverse(5)
reverse(["Happy", "Days"])
    

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

reversewords("I love you")    
reversewords("SHOUT LOUD AND CLEAR")
reversewords(5)
reversewords(["Happy", "Days"])


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
    return output

reversewordletters("I love you")
reversewordletters("SHOUT LOUD AND CLEAR")
reversewordletters(5)
reversewordletters(["Happy", "Days"])








## optional -- change text to piglatin.. google it!
def piglatin(txt):



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			

