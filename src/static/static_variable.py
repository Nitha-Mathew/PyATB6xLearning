#static variable or class variable
# variables shared by all objects

class tickets:
    base_price=10000 #class variable
    def __init__(self):
        tickets.count=tickets.count+1


    def movie_tkt(self):
        print("tickets booked")

    def exhibition_tkt(self):
        print("Exhibition tkts booked")

tkt=tickets()
tkt2=tickets()
print("counter = ", tickets.count)

