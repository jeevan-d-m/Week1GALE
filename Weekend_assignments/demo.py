class Demo():
    def __init__(self, size):
        self.size = size
        self.array=[[] for i in range(self.size)]
        

    # def hash(self, key):
    #     index = key % self.size
    #     # print(self.size)
    #     return index
    

    def set(self, key, value):
            self.array[key%self.size].append([key, value])
            # print("Collision")

    def get(self, key):
        for i in [self.array[key%self.size]]:
            for j in i:
                if key in j:
                    print(j[1])
        return False


# [[[13,"preetam"]],[]]
obj = Demo(6)
obj.set(1,"jeevan")
obj.set(2,"ullas")
obj.set(13,"preetam")
obj.set(4,"yashwanth")
obj.set(5,"varsha")

# name =[[1, "yashwa"], [[2,"jeevan"]]]
# mumap = Demo(len(name))
# for i in name:
#     mumap.set(i[0],i[1])

obj.get(1)