class Csv:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':
    my_csv = Csv()
    print("I'm a csv!")
    print(my_csv)
    while False:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_csv.accelerate()
        elif action == 'B':
            my_csv.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_csv.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_csv.average_speed()))
        my_csv.step()
        my_csv.say_state()