from math import sqrt
from random import randint


WIDTH = 30
HEIGHT = 10
NUM_PLATES = 8


class World:
    def __init__(self):
        self.plates = []
        self.tiles = []

    def create_plates(self):
        for i in range(NUM_PLATES):
            self.plates.append(Plate(randint(0, WIDTH), randint(0, HEIGHT), randint(400, 800)/1000, i))

    def show_plates(self):
        for plate in self.plates:
            print(f"x: {plate.x}, y: {plate.y}, weight: {plate.weight}, id: {plate.id}")
        print("==========")

    def create_tiles(self):
        for y in range(HEIGHT):
            row = []
            for x in range(WIDTH):
                row.append(Tile(y*WIDTH + x, x, y))
            self.tiles.append(row)

        for row in self.tiles:
            for tile in row:
                tile.find_plate(self.plates)

    def show_tiles(self):
        for row in self.tiles:
            for tile in row:
                print(tile, end='')
            print('')
        print("==========")

    def find_borders(self):
        for row in self.tiles:
            for tile in row:
                tile.set_borders(self.tiles)

    def show_borders(self):
        for row in self.tiles:
            for tile in row:
                print(f"{tile.border}", end='')
            print('')
        print("==========")

    def show_x(self):
        for row in self.tiles:
            for tile in row:
                print(f"{tile.x}", end='')
            print('')
        print("==========")

    def show_y(self):
        for row in self.tiles:
            for tile in row:
                print(f"{tile.y}", end='')
            print('')
        print("==========")


class Plate:
    def __init__(self, x, y, weight, uid):
        self.x = x
        self.y = y
        self.weight = weight
        self.tiles = []
        self.id = uid


class Tile:
    def __init__(self, uid, x, y):
        self.uid = uid
        self.elevation = 0
        self.plate = 0
        self.border = 0
        self.x = x
        self.y = y

    def find_plate(self, plates):
        min_distance = 0
        host_plate = 0
        for plate in plates:
            distance = sqrt((self.x - plate.x) * (self.x - plate.x) + (self.y - plate.y) * (self.y - plate.y))
            weighted_distance = distance * plate.weight
            if weighted_distance < min_distance or host_plate == 0:
                host_plate = plate.id
                min_distance = weighted_distance
        self.plate = host_plate

    def __str__(self):
        return str(self.plate)

    def set_borders(self, tiles):
        if self.x > 0:
            if self.y > 0:
                if self.plate != tiles[self.y-1][self.x-1].plate:
                    self.border = 1
            if self.plate != tiles[self.y][self.x-1].plate:
                self.border = 1
            if self.y < HEIGHT-1:
                if self.plate != tiles[self.y+1][self.x-1].plate:
                    self.border = 1

        if self.y > 0:
            if self.plate != tiles[self.y-1][self.x].plate:
                self.border = 1
        if self.y < HEIGHT-1:
            if self.plate != tiles[self.y+1][self.x].plate:
                self.border = 1

        if self.x < WIDTH-1:
            if self.y > 0:
                if self.plate != tiles[self.y-1][self.x+1].plate:
                    self.border = 1
            if self.plate != tiles[self.y][self.x+1].plate:
                self.border = 1
            if self.y < HEIGHT-1:
                if self.plate != tiles[self.y+1][self.x+1].plate:
                    self.border = 1


if __name__ == '__main__':
    world = World()
    world.create_plates()
    world.show_plates()
    world.create_tiles()
    world.show_tiles()
    # world.show_borders()
    world.find_borders()
    world.show_borders()
    # world.show_x()
    # world.show_y()
