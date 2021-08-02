class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_String(self):
        print(f'[Person Info] \nName: {self.name} \nAge: {self.age} \nAddress: {self.address}')


def main():
    persons = []
    while 1:
        print('0-Exit 1-Add 2-Print')
        menu = input('Choose One Number')
        if menu == '0':
            return
        elif menu == '1':
            persons.append(Person(input('name: '), input('age: '), input('address')))
        elif menu == '2':
            for i in persons:
                i.to_String()


if __name__ == '__main__':
    main()