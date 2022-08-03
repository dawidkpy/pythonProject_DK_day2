
def dekor(f):

    def w():

        print('!!!Witamy w Naszym salonie!!!')
        return f()

    return w

def check_brand(list):
    pass

def check_model(list):
    pass

def buy_car():
    pass

@dekor
def main():
    pass

if __name__ == '__main__':

        brand = ['AUDI', 'BMW']
        modelAudi = {'A3': 10, 'A4': 12}
        modelBMW = {'3': 5, '5': 5}

        main()

