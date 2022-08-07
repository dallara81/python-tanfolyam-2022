'''
Míg a legtöbb programnyelvnél a behúzás (indentation) csak a jobb olvashatóságot segíti elő,
a Pythonban nagyon fontos szerepe van. Így határozzuk meg az összetartozó kódblokkokat.
'''

# Példa

print('Behúzással')
if 3 < 7:
    print('Három kisebb, mint hét.')

# Helytelen - le sem fut (IndentationError: expected an indented block)
#print('Behúzás nélkül')
#if 3 < 7:
#print('Három kisebb, mint hét.')