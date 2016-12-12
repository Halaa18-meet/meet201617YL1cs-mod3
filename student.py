class student:
    def __init__(self, name, hometown, age, height, favicecreamflavor):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favicecremflavor

    def print_summary(self):

        print("my name is" + str(self.name)+"i live in" + str(self.hometown)+"i am" + str(self.age)+ "i am" + str(self.height)+ "my fav ice cream flavor is"+str(self.favicecreamflavor))

    def get_giraffe_gap(self):
        return (str(500-int(self.height)))
            
