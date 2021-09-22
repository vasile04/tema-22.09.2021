v=list(eval(input('Introdu venitul din fiecare zi al firmei: ')))
z=['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']
if len(v)>7:
    print('eroare')
print('Venitul saptamanal al intreprinderii este:', sum(v))
venit_mediu=(v[0]+v[1]+v[2]+v[3]+v[4]+v[5]+v[6])/7
if v[0]== max(v):
    print('ziua cu cel mai mare venit-', z[0])

if v[1]==max(v):
    print('ziua cu cel mai mare venit-', z[1])

if v[2] ==max(v):
    print(' ziua cu cel mai mare venit-', z[2])

if v[3] ==max(v):
    print(' ziua cu cel mai mare venit-', z[3])

if v[4] ==max(v):
    print(' ziua cu cel mai mare venit-', z[4])

if v[5] ==max(v):
    print(' ziua cu cel mai mare venit-', z[5])

if v[6] ==max(v):
    print( ' ziua cu cel mai mare venit-', z[6])

if v[0] ==min(v):
    print(' ziua cu cel mai mic venit-', z[0])

if v[1] ==min(v):
    print( ' ziua cu cel mai mic venit-', z[1])

if v[2] ==min(v):
    print( ' ziua cu cel mai mic venit-', z[2])

if v[3] ==min(v):
    print( ' ziua cu cel mai mic venit-', z[3])

if v[4] ==min(v):
    print(' ziua cu cel mai mic venit-', z[4])

if v[5] ==min(v):
    print( 'ziua cu cel mai mic venit-', z[5])

if v[6] ==min(v):
    print('este ziua cu cel mai mare venit-', z[6])