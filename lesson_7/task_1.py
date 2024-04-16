# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.
# Creați o variabilă numită number și atribuiți-i o valoare întreagă.
# CODUL TĂU VINE MAI JOS:
number = 3
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if number > 0:
    print(f'{number} is a positive number')
else:
    print(f'{number} is a negative number')   
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number') 
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.
# CODUL TĂU VINE MAI JOS:
text = 'Python is a popular programming language.'
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
search = input('Enter a word to be searched in text: ')
if search.lower() in text.lower():
    print(f'{search} is present in text')
else:
    print(f'{search} is not present in text')   
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
search = input('Enter a word to be searched in text: ')
if search.lower() in text.lower():
    print(f'{search} is present in text')
else:
    print(f'{search} is not present in text')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print('"Python" is present in text')
elif "Java" in text:
    print('"Java" is present in text')
else:
    print('Neither "Python" nor "Java" are present in text')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if "Python" in text and "Java" in text:
    print('Both "Python" and "Java" are present in text')
elif "Python" in text or "Java" in text:
    print('Either "Python" or "Java" is present in text')
else:
    print('Neither "Python" nor "Java" are present in text')
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"
# CODUL TĂU VINE MAI JOS:
number = int(input("Introduceți un număr de la 1 la 5: "))
if number == 1:
    print("Unu")
elif number == 2:
    print("Doi")
elif number == 3:
    print("Trei")
elif number == 4:
    print("Patru")
elif number == 5:
    print("Cinci")
else:
    print("Numărul introdus nu este în intervalul specificat")
# CODUL TĂU VINE MAI SUS:
