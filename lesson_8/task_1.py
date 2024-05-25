# Aceasta este tema pentru lecția 8 legată de loops
# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
# CODUL TĂU VINE MAI JOS:
numbers_list = []
for i in range(1, 11):
    numbers_list.append(i)
print("numbers_list contains:", numbers_list)    
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.
# CODUL TĂU VINE MAI JOS:
for i in numbers_list:
    if i % 2 == 0:
        print(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.
# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
      print(i)
      i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.
# CODUL TĂU VINE MAI JOS:
person = {
    'name': 'Name',
    'age': 30,
    'city': 'City'
}

for key, value in person.items():
    print(f'{key}: {value}')
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.
# CODUL TĂU VINE MAI JOS:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.
# CODUL TĂU VINE MAI JOS:
numbers = range(1, 6)

for number in numbers:
    print(number)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.
# CODUL TĂU VINE MAI JOS:
for index, value in enumerate(numbers_list):
    print(f'Index: {index}, Value: {value}')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.
# CODUL TĂU VINE MAI JOS:
letters_list  = ['a', 'b', 'c', 'd']
for number, letter in zip(numbers_list, letters_list):
    print(number, letter)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
# CODUL TĂU VINE MAI JOS:
new_numbers_list = []
for i in range(1, 11):
    new_numbers_list.append(i)
print("new_numbers_list contains:", new_numbers_list) 
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.
# CODUL TĂU VINE MAI JOS:
while new_numbers_list[0] <= 50:
      new_numbers_list = [number * 2 for number in new_numbers_list]
print('after doubling the values the new_numbers_list contains:', new_numbers_list)          
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].
# CODUL TĂU VINE MAI JOS:
perfect_squares = [number for number in range(1, 101) if int(number ** 0.5) ** 2 == number]
print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.
# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
    print(f"7 * {i} = {7 * i}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
# CODUL TĂU VINE MAI JOS:
pairs_list = [[i, j] for i in range(1, 6) for j in range(1, 6)]
print(pairs_list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .
# CODUL TĂU VINE MAI JOS:
for pair in pairs_list:
    if pair[0] < pair[1]:
        print(pair)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".
# CODUL TĂU VINE MAI JOS:
import random
random_numbers = [random.randint(1, 20) for _ in range(10)]
found = False
count = 0
while count < len(random_numbers):
    if random_numbers[count] > 10:
        print('Prima valoare mai mare decât 10: ', random_numbers[count])
        print(random_numbers)
        found = True
        break
    count += 1
if not found:
    print("Nu există valori mai mari decât 10.")
    print(random_numbers)
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****
# CODUL TĂU VINE MAI JOS:
size = int(input("Enter the square size: "))
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos
# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456
# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    print("".join(str(number) for number in range(1, i+1)))
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:
# 54321
# 5432
# 543
# 54
# 5
# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    print("".join(str(j) for j in range(5, 5 - i, -1)))
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:
# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g
# CODUL TĂU VINE MAI JOS:
letters = 'abcdefg'
for i in range(len(letters)):
    print(letters[i:])
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# CODUL TĂU VINE MAI JOS:
for i in range(8):
    if i % 2 == 0:
        print("".join(["+-"] * 8))
    else:
        print("".join(["-+"] * 8))
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:
# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243
# CODUL TĂU VINE MAI JOS:
numbers = [3, 9, 27, 81, 243]
for i in range(len(numbers)):
    print(" ".join(str(number) for number in numbers[:i+1]))
numbers.pop(0)
while numbers:
    print(" ".join(str(number) for number in numbers))
    numbers.pop(0)
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.