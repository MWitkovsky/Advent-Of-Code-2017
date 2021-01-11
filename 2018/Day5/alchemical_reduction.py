# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def print_town(town):
    for row in town:
        print_row = ""
        for val in row:
            print_row += "{} ".format(val)
        print(print_row)

def fill_building_info(specs):
    building = {
        "id": i+1,
        "height": specs[0],
        "width": specs[1]
    }
    door_row = specs[2]
    door_column = specs[3]
    if door_row == 1:
        building["door_facing"] = "N"
    elif door_row == building["height"]:
        building["door_facing"] = "S"
    elif door_column == 1:
        building["door_facing"] = "W"
    else:
        building["door_facing"] = "E"
    return building

town_info = [int(i) for i in input().split(" ")]
town = [[0 for i in range(town_info[1])] for j in range(town_info[0])]

buildings = {}
biggest_building = None
biggest_building_score = -1
for i in range(town_info[2]):
    buildings[i] = fill_building_info([int(n) for n in input().split(" ")])
    if buildings[i]["width"] * buildings[i]["height"] > biggest_building_score:
        biggest_building = buildings[i]
        biggest_building_score = buildings[i]["width"] * buildings[i]["height"]

for i in range(biggest_building["height"]):
    for j in range(biggest_building["width"]):
        town[i][j] = biggest_building["id"]

print_town(town)
