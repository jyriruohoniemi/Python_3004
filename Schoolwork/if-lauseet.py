print("Mikä on nimesi?")
annettuNimi = input()
if annettuNimi.islower():
    annettuNimi = annettuNimi.capitalize()
print("Nimesi on siis:", annettuNimi)