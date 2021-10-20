text = "Hello world !"
def pig_it(text):
    lWords = text.split() 
    newText = ""
    for i in lWords:
        if i.isalpha():
            newText = newText + "".join(list(i)[1:]) +"".join(list(i[0])) + "ay "
        else:
            newText = newText +i+" "
            print (newText)
    return newText[:-1]
