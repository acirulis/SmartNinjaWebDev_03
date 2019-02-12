some_list = [1, 34, 12, 17, 87]

print(some_list)

some_list.append(99)
some_list.append(33)
some_list.sort(reverse=True)


for element in some_list:
    print("Mana saraksta kārtējais elements ir: {}!".format(element))

print(len(some_list)) #nosakam garumu




other_list = []
other_list.append('Abols')
other_list.append('Apelsins')
other_list.append('Kivi')
other_list.append('Avene')
ix = 1
for auglis in other_list:
    print('{}. elements pēc kārtas ir {}'.format(ix, auglis))
    ix += 1


saraksts = [1,2,3,4,5,6]

print(saraksts[::-1]) # LIST SLICING


boxA = {"height": 20, "width": 45, "length": 30}
boxB = {"height": 30, "width": 55, "length": 40}
boxC = {"height": 40, "width": 65, "length": 50}

boxes = [boxA, boxB, boxC]

for box in boxes:
    print('Kastes parametri:')
    print('Augstums: {}'.format(box['height']))
    print('Platums: {}'.format(box['width']))
    print('Garums: {}'.format(box['length']))


