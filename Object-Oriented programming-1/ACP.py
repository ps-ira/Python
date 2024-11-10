class Robot:
    def __init__(self, name, model, battery_level=100):
        self.name = name
        self.model = model
        self.battery_level = battery_level

    def greet(self):
        print(f"Hello, I am {self.name}, a {self.model} robot. How can I assist you today?")

    def move(self, distance):
        if self.battery_level <= 0:
            print("Battery is dead! Please charge me.")
        else:
            print(f"{self.name} is moving {distance} meters.")
            battery_consumed = distance * 0.1
            self.battery_level -= battery_consumed
            if self.battery_level < 0:
                self.battery_level = 0
            print(f"Battery level: {self.battery_level}%")

    def charge(self):
        print(f"{self.name} is charging...")
        self.battery_level = 100
        print(f"{self.name} is fully charged!")

    def status(self):
        print(f"{self.name} ({self.model}) - Battery Level: {self.battery_level}%")

if __name__ == "__main__":
    robot1 = Robot("Robix", "Model A", 75)
    robot1.greet()
    robot1.status()
    robot1.move(50)
    robot1.charge()
    robot1.move(30)
