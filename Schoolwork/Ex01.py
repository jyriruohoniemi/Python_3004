#Ex01 Listan tulostus takaperin
#Fruit = ["apples", "oranges", "pears", "bananas"]
#L = len(Fruit)
#for i in range(int(L/2)):
    # Peilataan listan indekstit
    # jotta saadaan lista printatuksi takaperin
    # 0 = 3, 1 = 2 jne.
   # n = Fruit[i]
 #   Fruit[i] = Fruit[L-i-1]
  #  Fruit[L-i-1] = n
#print(Fruit)

#Ex02 Stringistä joka toisen kirjaimen tulostaminen
#s=input("Please enter a string: ")
# x[startAt:endBefore:skip] 
# Käytännössä skippaa joka 
# toisen kirjaimen stringistä
#print(s[0::2])

#Ex03 parillisten ja parittomien numerojen laskenta listassa
list1 = [10, 21, 4, 45, 66, 93, 1] 
even_count, odd_count = 0, 0
# for-loopilla listan tarkistaminen
for num in list1:       
    if num % 2 == 0: 
        even_count += 1 
    else: 
        odd_count += 1
          
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count)

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

#Ex05 N-määrän keskiarvon laskenta
num = int(input('How many numbers: '))
total_sum = 0
#For-loopilla numeroiden lisääminen num:n verran
for n in range(num):
   numbers = float(input('Enter number : '))
total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)