# Aceasta este a doua sarcină legată de tuples
# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5
# CODUL TĂU VINE MAI JOS:
numbers = (1, 2, 3, 4 ,5)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'Tuple "numbers" contains: {numbers}')
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la tuple `numbers`
# CODUL TĂU VINE MAI JOS:
number6 = (6,)
numbers = numbers + number6
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'Tuple "numbers" contains: {numbers}')
# CODUL TĂU VINE MAI SUS:

# Afișeați primul element din tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'First element of "numbers" tuple is: {numbers[0]}')
# CODUL TĂU VINE MAI SUS:   

# Afișeați ultimul element din tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'Last element of "numbers" tuple is: {numbers[-1]}')
# CODUL TĂU VINE MAI SUS:

# Afișeați primele două elemente din tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'The first 2 elements of "numbers" tuple: {numbers[0:2]}')
# CODUL TĂU VINE MAI SUS:

# Afișeați ultimele două elemente din tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'The first 2 elements of "numbers" tuple: {numbers[-2:]}')
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'Tuple "numbers" length: {len(numbers)}')
# CODUL TĂU VINE MAI SUS:

# Afișați suma elementelor din tuple `numbers`
# CODUL TĂU VINE MAI JOS:
sum = 0
for i in numbers:
    sum += i
print(f'The sum of elements from "numbers" tuple is: {sum}')   
# CODUL TĂU VINE MAI SUS:

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10
# CODUL TĂU VINE MAI JOS:
numbers_list = list(numbers)
numbers_list[2] = 10
numbers = tuple(numbers_list)
# CODUL TĂU VINE MAI SUS:

# Afișați tuple `numbers`
# CODUL TĂU VINE MAI JOS:
print(f'Tuple "numbers" contains: {numbers}')
# CODUL TĂU VINE MAI SUS:

# Ștergeți tuple `numbers`
# CODUL TĂU VINE MAI JOS:
del numbers
try:
    print(f'Tuple "numbers" contains: {numbers}')
except NameError:
    print('Tuple "numbers" is not defined')
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste