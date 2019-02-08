#
#
#
# # 1 ... 9
#
# i = 1
# while i < 10:
#     print(i)
#     i += 2 # i = i + 1
#
# # uzdevums 10 ... 1
# i = 10
# while i > 0:
#     print(i)
#     i -= 1 # tas pats kas i = i - 1
#
# # izdrukāt visus pāra skaitļus no 1 - 20, izņemot tos, kas dalās ar 4
# print('3. uzdevums')
# i = 2
# while i <= 20:
#     if i % 4 != 0:
#         print(i)
#     i += 2
#
#
# print('4. uzdevums')
# number = 20
# guess = 0
# while guess != number:
#     guess = input('Please enter any number: ')
#     guess = int(guess)
#     print('You entered: ', guess)
#
# print('Done!') #pēc atkāpēm redzam, ka šī operācija jau ir PĒC cikla

# 5. uzdevums : lietotajs ievada skaitli 2 .. 100 , programma izvada visus pāra skaitļus no 2 līdz lietotāja ievadītājam!

# lietotājs ievada: 11
# programma izvada: 2 4 6 8 10

# number = input('Ludzu ievadiet skaitli: ')
# number = int(number)
#
# start = 2
#
# while (start <= number):
#     print(start)
#     start += 2
#
#
# i = 1
# while i < 20:
#     if i == 10:
#         break # tehnisks veids, kā iziet no cikla jebkurā laikā!
#     print(i)
#     i += 1
#
#
for i in range(1,6):
    print(i)


secret_number = 789

with open("score.labvakar", "w") as score_file:
    score_file.write(str(secret_number))

