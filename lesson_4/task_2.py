# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python
# Creează o variabilă numită `name` și seteaz-o la numele tău
# CODUL TĂU VINE MAI JOS:
name = "Mariana"
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`
# CODUL TĂU VINE MAI JOS:
print(f'Value of "name" is: {name}')
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`
# CODUL TĂU VINE MAI JOS:
name2 = name
print(f'Value of "name2" is: {name2}')
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea
# CODUL TĂU VINE MAI JOS:
print(f'The last character of "name" is: {name[len(name)-1]}')
print(f'The last character of "name" is: {name[-1]}')
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing
# CODUL TĂU VINE MAI JOS:
print(f'The first 3 characters of "name" are: {name[0:3]}')
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`
# CODUL TĂU VINE MAI JOS:
print(f'Value of "name" in uppercase: {name.upper()}')
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`
# CODUL TĂU VINE MAI JOS:
print(f'Value of "name" in lowercase: {name.lower()}')
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`
# CODUL TĂU VINE MAI JOS:
print(f'Result of "name" and "name2" concatenation is: {name + name2}')
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri
# CODUL TĂU VINE MAI JOS:
text = '''Python is a popular programming language.
Python can be used on a server to create web applications.'''
print(f'Value of "text" is: {text}')
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`
# CODUL TĂU VINE MAI JOS:
print(f'Result of text.find("Python") is: {text.find("Python")}')
print(f'Result of text.rfind("Python") is: {text.rfind("Python")}')
print(f'Result of text.count("Python") is: {text.count("Python")}')
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`
# CODUL TĂU VINE MAI JOS:
print(f'Result of text.replace("a", "e") is: {text.replace("a", "e")}')
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte
# CODUL TĂU VINE MAI JOS:
print(f'Result of text.split() is: {text.split()}')
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`
# CODUL TĂU VINE MAI JOS:
f_str = f'Variables {name} and {name2} have the same value!'
print(f'Result of f_str is: {f_str}')
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`
# CODUL TĂU VINE MAI JOS:
print(f'Result of f_str.endswith("!") is: {f_str.endswith("!")}')
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`
# CODUL TĂU VINE MAI JOS:
print(f'Result of f_str.startswith("Hello") is: {f_str.startswith("Hello")}')
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat
# CODUL TĂU VINE MAI JOS:
print(f'Result of f_str.find("!") is: {f_str.find("!")}')
print(f'Result of f_str.index("!") is: {f_str.index("!")}')
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă
# CODUL TĂU VINE MAI JOS:
print(f'Result of f_str.find("o") is: {f_str.find("o")}')

search = input('Enter a value to be searched in f_str via index() method: ')
try:
    index = f_str.index(search)
    print(f'Index of "{search}" in f_str is: {index}')
except ValueError:
    print(f'"{search}" is not present in f_str')
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`
# CODUL TĂU VINE MAI JOS:
f_str2 = f'This string contains {name} and {name2}!'
print(f'Result of f_str2 is: {f_str2}')
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`
# CODUL TĂU VINE MAI JOS:
print(f'Result of f_str2 and text concatenation is: {f_str2+text}')
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat
# CODUL TĂU VINE MAI JOS:
print(f'Length of f_str2 is: {len(f_str2)}')
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină
