from functions import say_hello, check_if_prime

print(say_hello('Andis'))
# print(say_hello(name='Peteris'))
# print(say_hello('Anna'))
#
# title = say_hello('Olegs')
# print('<b>{}</b>'.format(title))


for i in range(1, 51):
    if check_if_prime(i):
        print(i, end=', ')
print('\n')

while True:
    number = input('Ludzu ievadiet skaitli vai X lai izietu: ')
    if number.lower() == 'x':
        break
    is_prime = check_if_prime(int(number))
    if is_prime:
        print('Jūsu ievadītais skaitlis {} ir pirmskaitlis'.format(number))
    else:
        print('Jūsu ievadītais skaitlis {} NAV pirmskaitlis'.format(number))
