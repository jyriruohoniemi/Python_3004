#Ex04 Sanojen lisääminen listaan kunnes sanotaan 'stop'
wordList = []
print("Give words")
item = str(input("Please add words to the list: "))
wordList.append(item)
#Kun listassa ei ole sanaa 'stop' niin ohjelma jatkuu
while item != "stop":
    item = str(input("Please add more words to the list: "))
    wordList.append(item)
if item == "stop":
    #stopin laittaessa poistetaan sana listasta ja tulostetaan koko listan sisältö
    wordList.remove("stop")
    print(wordList)
    print("That's your list")
