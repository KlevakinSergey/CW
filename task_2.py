class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.sugar = 1000
        self.coffee = 1000


     

    def make_coffee(self,milk,sugar, coffee):
        if self.milk < milk and self.sugar < sugar and self.coffee < coffee:
            res1 = milk - self.milk
            res2 = sugar - self.sugar
            res3 = coffee - self.coffee
            print(f'Пополните запасы молока на {res1} мл! ')
            print(f'Пополните запасы сахара на {res2} гр!')
            print(f'Пополните запасы кофе на {res3} гр!')

        elif  self.milk < milk and self.coffee < coffee:
            res1 = milk - self.milk
            res2 = coffee - self.coffee
            print(f'Пополните запасы молока на  {res1} мл. и запас кофе на {res2} гр.')  


        elif  self.milk < milk and self.sugar < sugar:
            res1 = milk - self.milk
            res2 = sugar - self.sugar
            print(f'Пополните запасы молока на  {res1} мл. и запас сахара на {res2} гр.') 


        elif  self.sugar < sugar and self.coffee < coffee:
            res1 = sugar - self.sugar
            res2 = coffee - self.coffee
            print(f'Пополните запасы сахара на  {res1} гр. и запас кофе на {res2} гр.')     





        elif self.milk > milk and self.sugar < sugar and self.coffee > coffee:
            res = sugar - self.sugar
            print(f'Пополните запасы сахара на {res} гр!')   
    
        
        elif self.milk < milk and self.sugar > sugar and self.coffee > coffee:
            res = milk - self.milk
            print(f'Пополните запасы молока на {res} мл!')
          


        elif self.milk > milk and self.sugar > sugar and self.coffee < coffee:
            res = coffee - self.coffee
            print(f'Пополните запасы кофе на {res} гр!')


    


        else:
            print('Процесс приготовления кофе завершен!')
            self.__subtract_milk(milk)
            self.__subtract_sugar(sugar)
            self.__subtract_coffee(coffee)

    

    def __subtract_milk(self,milk):
        self.milk -= milk
        print(f'Осталось {self.milk} мл. молока')

    def __subtract_sugar(self,sugar):
        self.sugar -= sugar
        print(f'Осталось {self.sugar} гр. сахара')


    def __subtract_coffee(self,coffee):
        self.coffee -= coffee
        print(f'Осталось {self.coffee} гр. кофе')



def main():
    a = CoffeeMachine()
    a.make_coffee(100,10000,10000)

if __name__ == '__main__':
    main()

