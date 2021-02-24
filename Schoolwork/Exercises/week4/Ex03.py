def vowelCount(wordString):
    lowercase = wordString.lower()
#Convert to lowercase
    vowel_counts = {}

    for vowel in "aeiouyäö":
        count = lowercase.count(vowel)
        vowel_counts[vowel] = count
    
    return vowel_counts

wordString = input()
print(vowelCount(wordString))
