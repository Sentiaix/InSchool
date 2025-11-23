# 절자척 전화기 구현

phone1 = ['mike', '01012345678', 80]
contacts1 = {'jake':'4567', 'fin':'4556'}

def call(phone, contacts, name):
    print(f'calling from {phone[1]}')
    print(f"to {contacts[name]}")

call(phone1, contacts1,'fin')

class myphone:
    def __init__ (self, name = 'hong'):
            self.name = name
            self.battery = 100
            self.number = 123 # member 변수
            number = 456 # local 변수
            self.contacts = {'jake':'4567', 'fin':'4556'}
    def call(self, name):
        print('calling from', self.number)
        print('to', self.contacts[name])

phone2 = myphone('Alba')
# phone2.name = 'Tyson'
phone2.contacts['Fury'] = '7531'
print(phone2.number, phone2.name)
print(phone2.contacts)
phone2.call('jake')