#use of multiple inheritance...solve Diamond Problems

class Food:
    def cook(self, name):
        print("cooked food::" + name)



class Pizza:
        def cook(self,name):
            print("cooked pizza::"+name)

class ChiPizza(Pizza,Food):  #calls priority is first argument ... removing multiple inheritance python doesnt support interface
        pass


c = ChiPizza()
c.cook("chicken")

