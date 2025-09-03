#-----------------------------------------------------------------
list_of_numbers = [10, 20, 30, 40, 50] 

try:
    index = int(input("Enter index: ")) # langsung konversi ke integer
    print(f"Data in index {index} is {list_of_numbers[index]}")
except ValueError:
    print("Enter the number!")
except IndexError:
    print("Index not found!")
exit()

#-----------------------------------------------------------------
print("What is the result of 10 divided by the number you chose?") #Berapakah hasil 10 dibagi dengan angka yang kamu pilih?

try:
    divisor = int(input("Enter divisor: ")) # meminta user memasukkan angka (pembagi)
    results = 10/divisor
    print(f"10 : {divisor} = {results}")
except ZeroDivisionError:
    print("Cannot be divided by zero!") # menangani jika user memasukkan angka 0 (Tidak bisa dibagi dengan nol!)
except ValueError:
    print("Input must be a number!") # menangani jika user mengetik huruf (Tidak bisa dibagi dengan huruf!)
exit()

#-----------------------------------------------------------------
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
exit()

#-----------------------------------------------------------------
try:
    numerator = int(input("Enter the numerator: ")) #pembilang
    denominator = int(input("Enter the denominator: ")) #penyebut
    results = numerator / denominator
    print(f"Division results: {results}") #pembagian
except ZeroDivisionError:
    print("The denominator cannot be zero!")
exit()

#-----------------------------------------------------------------
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
#-----------------------------------------------------------------
