
def dekor(f):

    def w():

        print('!!!Witamy w Naszym salonie!!!')
        return f()

    return w

def check_brand(list, b):

    if b in list:
        return True
    else:
        print('Przykro nam, nie mamy tej marki w ofercie.')
        return False


def check_model(list, m):

    # if m in list.key() and list[m] >= 0:
    if m in list and list[m] >= 0:
        return True
    else:
        print('Przykro nam, nie mamy tego modelu.')
        return False

def buy_car(list, m):
    list[m] -= 1
    print('Zostales wlascicielem jednego z naszych ', m)
    exit()

def exit():

    a = input('Czy mozemy zapronowowac inne auto (Y/N)? ')
    a = a.upper()
    if a == 'Y':
        main()
    else:
        print('Zapraszamy ponownie. Do widzenia')


@dekor
def main():
    print('Posiadamy w ofercie marki i modele w liczbie sztuk:')
    for i, j in brand.items():
        print(i, j)

    b = input('Jakiej marki szukasz? ')
    b = b.upper()

    if check_brand(brand, b) is True:
        if b == 'AUDI':
            l = brand[b]
            print(l)
        else:
            l = brand['BMW']
            print(l)

        m = input('Jakiego modelu szukasz? ')
        m = m.upper()
        if check_model(l, m) is True:
            b = input('Mamy ten model. Chcesz kupić (Y/N)? ')
            b = b.upper()
            if b == 'Y':
                buy_car(l, m)

        else:
            exit()
    else:
        exit()

if __name__ == '__main__':

        brand = {'AUDI': {'A3': 10, 'A4': 12}, 'BMW': {'3': 5, '5': 5}}

        main()

