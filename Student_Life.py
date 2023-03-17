import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 2
        self.money = 10
        self.chill = 5
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.24
        self.chill -= 1
        self.gladness -= 5

    def to_Job(self):
        print("Time to Job")
        self.progress -= 0.5
        self.money += 10
        self.chill -= 1
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.chill += 2

    # conditions
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0 or self.chill <=-10:
            print("Depression…")
            self.alive = False
        elif self.progress > 5 or self.money <10:
            print("Passed externally…")
            self.alive = False

    # print info of day after self.day
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Chill = {self.chill}")
        print(f"Money = {self.money}")
        print(f"Progress = {round(self.progress, 2)}")

    # print info about this day
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)

        # if something is needed
        if self.money <10:
            self.to_Job()
            self.end_of_day()
            self.is_alive()
        elif self.gladness <20:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif self.progress < 1:
            self.to_study()
            self.end_of_day()
            self.is_alive()
        elif self.chill<0:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        else:
        # Random day
            if live_cube == 1:
                self.to_study()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 2:
                self.to_sleep()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 3:
                self.to_chill()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 4:
                self.to_Job()
                self.end_of_day()
                self.is_alive()

nick = Student(name="Nick")



for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)