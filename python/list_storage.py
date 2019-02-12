import json # JSON formāts, kas ļauj ērti pārvērst datus no LIST uz failā ierakstāmu STRING
            # JSON un LIST ir līdzīgi, bet ne vienādi!!!!
list = []  # šeit glabāsim mūsu sarakstu
file_name = 'lists.txt'
print('Programma, kas lauj veidot savu personigo SARAKSTU :) ')

try:
    with open(file_name, "r") as data_file:
        list = json.loads(data_file.read())
except (ValueError, OSError):  # noķeram formāta vai faila neesamības kļūdu
    list = []  # Izveidojam tukšu sarakstu, ja nav izdevies ielasīt no faila

while True:
    print('\n\n')
    print('Ja vēlaties apskatīt sarakstu, nospiediet R (Read)')
    print('Ja vēlaties papildināt sarakstu, nospiediet A (Add)')
    print('Ja vēlaties iziet no programmas, nospiediet X (Exit)')
    choice = input('Jūsu izvēle: ... ')
    if choice.lower() not in ['r', 'a', 'x']:
        print('Jūst esat izdarījis kļūdainu izvēli!')
        continue  # veids kā izlaist visu tālāko cikla darbību un sākt vēlreiz no sākuma
    if choice.lower() == 'r':
        print('\n')  # tukša rindiņa uz ekrāna pārskatāmībai
        print('Jūsu saraksts!')
        if len(list) == 0:
            print('Jūsu saraksts ir tukšs.')
        ix = 1
        for item in list:
            print('{}. elements ir: {}'.format(ix, item))
            ix += 1

    if choice.lower() == 'a':
        print('Elementa pievienosana!')
        value = input('Lūdzu ievadiet kārtējo saraksta elementu: ... ')
        list.append(value)

    if choice.lower() == 'x':
        print('Paldies par darbu!')
        break

with open(file_name, "w") as data_file:
    data_file.write(json.dumps(list))
