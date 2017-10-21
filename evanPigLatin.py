def pigLatin(string):
    firstLetter = string[0]
    restOfWord = string[1:-1] + string[-1]
    string = restOfWord + firstLetter + "ay"
    return string
    



word = input("enter a word: ")

print(pigLatin(word))


sentence = "the cow jumped"
spaceIndex = sentence.find(" ") #finds index of first space in a sentence
firstWord = sentence[0:spaceIndex] #finds characters up until first space of sentence

print(spaceIndex)
print(firstWord)
    
endOfWord = sentence.find(" ", spaceIndex+1) #finds the second space in a sentence 


secondWord =sentence[spaceIndex+1:endOfWord] #finds characters in between first space & second space

print("\n")


print(len(sentence))