'''
name, phone, email, address
'''


class Contacts(object):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_String(self):
        print(f'[Contacts] \nName: {self.name} \nPhone: {self.phone} \nEmail: {self.email} \nAddress: {self.address}')


def set_contact() -> object:             # 함수
    return Contacts(input('name'), input('phone'), input('email'), input('address'))    # 생성자에 의해 리턴된 인스턴스 는 객체


def get_contacts(ls):
    for i in ls:
        i.to_String()


def del_contact(ls, name):              # return type 없으니 void
    for i, j in enumerate(ls):          # index가 필요
        if name == j.name:
            del ls[i]


def print_menu(ls) -> int:              # -> int ; return type 명시
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):          # enumerate:열거하다 / 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
        t += str(i)+'-'+j+'\t'
    return int(input(t))


def main():
    ls = []
    while 1:
        menu = print_menu(['Exit', 'Add', 'Print', 'Delete'])
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contacts(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break


if __name__ == '__main__':
    # ls = ['0-Exit', '1-Add', '2-Print', '3-Delete']
    # ls2 = ['Exit', 'Add', 'Print', 'Delete']
    # print(menu(ls2))
    main()