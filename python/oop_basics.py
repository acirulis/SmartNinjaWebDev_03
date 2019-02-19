from datetime import datetime


class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2,
                          rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)


print(lebron.full_name())
# print(kev_dur.full_name())
# print(lebron.weight_to_lbs())


class Human:
    def __init__(self, name, birth_year):
        self.full_name = name
        self.year_of_birth = birth_year

    def age(self, check_year=None):
        if not check_year:
            now = datetime.now()
            check_year = now.year
        return check_year - self.year_of_birth


janis = Human('Janis', 1984)
anna = Human('Anna', 2000)

draugi = [janis, anna]
#
# for draugs in draugi:
#     print('{} age is {}'.format(draugs.full_name, draugs.age()))
#     print('{} age at 2035 will be {}'.format(draugs.full_name, draugs.age(2035)))


class HTMLForm:
    def __init__(self, name, method, action):
        self.fields = []
        self.name = name
        self.method = method
        self.action = action

    def add_field(self, label, type, min_width):
        if type not in ['text', 'password', 'email', 'checkbox', 'radiobutton', 'textarea']:
            raise ValueError('Type is not allowed!: ' + type)
        field = {'label': label,
                 'type': type,
                 'min_width': min_width}
        self.fields.append(field)

    def show(self):
        print('==={}==='.format(self.name))
        print('<form method="{}" action="{}">'.format(self.method, self.action))
        for field in self.fields:
            if field['type'] == 'text':
                print('{}:  <input type="text" name="" value="" />'.format(field['label']))
            elif field['type'] == 'password':
                print('{}:  <input type="password" name="" value="" />'.format(field['label']))
            elif field['type'] == 'email':
                print('{}:  <input type="email" name="" value="" />'.format(field['label']))
        print('</form>')


kontaktforma = HTMLForm(name="Kontaktforma", method="POST", action="/contactform/submit")
kontaktforma.add_field(label='Vārds', type='text', min_width=6)
kontaktforma.add_field(label='Epasts', type='email', min_width=6)
kontaktforma.add_field(label='Telefons', type='text', min_width=9)


kontaktforma.show()