#Ex05 N-määrän lukuja keskiarvon laskenta
num = int(input('How many numbers: '))
total_sum = 0
#For-loopilla numeroiden lisääminen num:n verran
for n in range(num):
   numbers = float(input('Enter number : '))
total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)