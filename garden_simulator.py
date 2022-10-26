# Моделировать в виде пошаговой симуляции, с возможностью изменения (например, добавление, удаление) элементов модели

# Предметная область - выращивание растений на садовом участке в зависимости от погодных условий и вредителей

# Сущности - Грядка, Сад, Семена, Овощи, Деревья, Фрукты, Полив, Погода, Дождь, Солнце, Засуха

# Взаимодействия - Посадка, Полив, Уборка, Урожай, Погода, Вредители

# Все сущности имеют свойства и методы (например, Грядка - размер, площадь, количество растений, методы - посадка, уборка, урожай)

# реализовать с помощью классов и наследования

import os


# Сущности - Грядка
class Garden:
    def __init__(self, name, size, area):
        self.name = name
        self.size = size
        self.area = area
        self.plots = []

    def __str__(self):
        return f'Garden {self.name} has size {self.size} and area {self.area}'

    def __repr__(self):
        return f'Garden {self.name} has size {self.size} and area {self.area}'

    def add_plot(self, plot):
        if len(self.plots)+self.size >= self.area:
            os.system('cls||clear')
            print('Not enough space in garden \n')
            return
        self.plots.append(plot)
        os.system('cls||clear')
        print("Plot created! \n")

    def get_plots(self):
        return self.plots

    def get_plot_by_name(self, name):
        for plot in self.plots:
            if plot.name == name:
                return plot
        print('Plot with name ' + name + ' not found')
        return None

    def remove_plot_by_name(self, name):
        for i in range(len(self.plots)):
            if self.plots[i].name == name:
                del self.plots[i]
                return
        raise Exception('Plot with name ' + name + ' not found')

    def get_plots_count(self):
        return len(self.plots)

    def get_garden_name(self):
        return self.name

    def water(self, plant):
        plant.watered = True

    def weed(self, plant):
        plant.weeded = True

# Сущности - Сад


class Plot:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def get_plants(self):
        return self.plants

    def get_plant(self, index):
        return self.plants[index]

    def get_plant_by_name(self, name):
        for plant in self.plants:
            if plant.name == name:
                return plant
        return None

    def __str__(self):
        return self.name


class Plant:
    def __init__(self, name, growth_rate, growth_time, harvest_time):
        self.name = name
        self.growth_rate = growth_rate
        self.growth_time = growth_time
        self.harvest_time = harvest_time
        self.growth = 0

    def grow(self):
        self.growth += self.growth_rate

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time

    def __str__(self):
        return self.name

# Сущности - Семена


class Seed(Plant):
    def __init__(self, plant):
        self.plant = plant

    def __str__(self):
        return self.plant.name + " seed"

# Сущности - Овощ


class Vegetable(Plant):
    def __init__(self, name, growth_rate, growth_time, harvest_time, seed_rate, treat_time):
        super().__init__(name, growth_rate, growth_time, harvest_time)
        self.seed_rate = seed_rate

    def grow(self):
        super().grow()
        if self.is_grown():
            self.seed = Seed(self)

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time

    def __str__(self):
        return self.name

# Сущности - Деревья


class Tree(Plant):
    def __init__(self, name, growth_rate, growth_time, harvest_time, seed_rate, dig_time):
        super().__init__(name, growth_rate, growth_time, harvest_time)
        self.seed_rate = seed_rate
        self.dig_time = dig_time

    def grow(self):
        super().grow()
        if self.is_grown():
            self.seed = Seed(self)

    def is_grown(self):
        return self.growth >= self.growth_time

    def is_harvested(self):
        return self.growth >= self.harvest_time

    def __str__(self):
        return self.name

# Сущности - Фрукты


class Weather:
    def __init__(self, name, growth_rate):
        self.name = name
        self.growth_rate = growth_rate

    def __str__(self):
        return self.name


class Rain(Weather):
    def __init__(self):
        super().__init__("Rain", 0.5)


class Sun(Weather):
    def __init__(self):
        super().__init__("Sun", 1)


class Drought(Weather):
    def __init__(self):
        super().__init__("Drought", 0.1)

# Сущности - вредителей


class Pests:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'Pests {self.name} has damage {self.damage}'

    def __repr__(self):
        return f'Pests {self.name} has damage {self.damage}'


class GardenSimulator:
    def __init__(self, garden):
        self.garden = garden
        self.weather = None

    def set_weather(self, weather):
        os.system('cls||clear')

        if weather == "1":
            self.weather = Rain()
            print("Weather is Rain \n")
        elif weather == "2":
            self.weather = Sun()
            print("Weather is Sun \n")
        elif weather == "3":
            print("Weather is Drought \n")
            self.weather = Drought()

    def simulate(self):
      # Garden simulator with growth of plants
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                plant.grow()
                if self.weather.name == "Rain":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Sun":
                    plant.growth += self.weather.growth_rate
                elif self.weather.name == "Drought":
                    plant.growth += self.weather.growth_rate

                if plant.is_grown():
                    print(f'{plant} is grown')

        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    continue
                if plant.is_grown():
                    print(f'{plant} is harvested')
                    plant.growth = 0
                    plant.harvested = True
                    if isinstance(plant, Vegetable):
                        plot.add_plant(plant.seed)
                    elif isinstance(plant, Tree):
                        plot.add_plant(plant.seed)

        os.system('cls||clear')
        print(f"Simulation of garden {self.garden.get_garden_name()}\n")
        print(f"To check result with print garden\n")

    def print_garden(self):
        for plot in self.garden.get_plots():
            print(plot)
            for plant in plot.get_plants():
                print(plant, plant.growth)
            print()

    def harvest(self):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.is_harvested():
                    plot.add_plant(plant.seed)
                    plant.seed = None

    def get_plot_by_name(self, name):
        return self.garden.get_plot_by_name(name)

    def get_plant_by_name(self, name):
        for plot in self.garden.get_plots():
            for plant in plot.get_plants():
                if plant.name == name:
                    return plant
        return None


class GardenSimulatorApp:
    def __init__(self):
      # create garden with parameters name, size, area, plants
        self.garden = self.set_garden()
        self.simulator = GardenSimulator(self.garden)
        self.weather = None

    def set_garden(self):
        print('Create garden')
        name = input('Enter name: ')
        size = int(input('Enter size: '))
        area = int(input('Enter area: '))
        os.system('cls||clear')
        print(f"Welcome to the {name}! \n")
        return Garden(name, size, area)

    def create_plot(self):
        name = input("Enter plot name: ")
        plot = Plot(name)
        self.garden.add_plot(plot)

    def create_plant(self, choice, name, growth_rate, growth_time,
                     harvest_time, seed_rate, dig_time=0, treat_time=0):

        if choice == '1':
            plant = Tree(name, growth_rate, growth_time,
                         harvest_time, seed_rate, dig_time)
        elif choice == '2':
            plant = Vegetable(name, growth_rate, growth_time,
                              harvest_time, seed_rate, treat_time)

        plot_name = input("Enter plot name: ")
        plot = self.simulator.get_plot_by_name(plot_name)

        if plant and plot:
            plot.add_plant(plant)
            os.system('cls||clear')
            print("Plant added to plot \n")

    def set_weather(self, weather):
        self.simulator.set_weather(weather)

    def simulate(self):
        self.simulator.simulate()

    def print_garden(self):
        self.simulator.print_garden()

    def get_plant(self):
        name = input("Enter plant name: ")
        plant = self.simulator.get_plant_by_name(name)
        print(plant)

    def get_plot(self):
        name = input("Enter plot name: ")
        plot = self.simulator.get_plot_by_name(name)
        print(plot)


class Gui:
    def __init__(self, app):
        self.app = app

    def run(self):
        while True:
            print("1. Create plot")
            print("2. Create plant")
            print("3. Set weather")
            print("4. Simulate")
            print("5. Print garden")
            print("6. Get plant")
            print("7. Get plot")
            print("0. Exit \n")
            command = input("Enter command: ")
            print("\n")

            if command == '1':
                self.app.create_plot()
            elif command == '2':
                print("1. Tree,    2. Vegetable \n")
                plant_type = input("Enter choice: ")
                name = input("Enter name: ")
                growth_rate = float(input("Enter growth rate: "))
                growth_time = int(input("Enter growth time: "))
                harvest_time = int(input("Enter harvest time: "))
                seed_rate = float(input("Enter seed rate: "))

                if plant_type == '1':
                    dig_time = int(input("Enter dig time: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, dig_time)
                elif plant_type == '2':
                    treat_time = int(input("Enter treat time: "))
                    self.app.create_plant(plant_type, name, growth_rate, growth_time,
                                          harvest_time, seed_rate, treat_time)

                os.system('cls||clear')
                print("Plant created \n")
            elif command == '3':
                print("1. Rain")
                print("2. Sun")
                print("3. Drought")
                choice = input("Enter your choice: ")
                self.app.set_weather(choice)
            elif command == '4':
                self.app.simulate()
            elif command == '5':
                self.app.print_garden()
            elif command == '6':
                self.app.get_plant()
            elif command == '7':
                self.app.get_plot()
            elif command == '0':
                break


def main():
    print("Welcome to the Garden Simulator! \n")

    app = GardenSimulatorApp()
    gui = Gui(app)
    gui.run()


if __name__ == "__main__":
    main()
