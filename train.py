#! /usr/bin/python3

from sense_hat import SenseHat
from mappix import mappix


sense = SenseHat()

sense.clear()



# initialize
col_bg	= (44, 176, 55)
col_rail= (100,100,100)
width	= 8
height	= 8
map	= []

for h in range(0,height):
	line	= []
	for w in range(0,width):
		line.append(mappix(col_bg[0],col_bg[1],col_bg[2]))
	map.append(line)

def draw_map(map,x0,y0):
	for y in range(y0,y0+8):
		for x in range(x0,x0+8):
			sense.set_pixel(x,y,map[x][y].col())

def set_rail(map,x,y):
	map[x][y].r = col_rail[0]
	map[x][y].g = col_rail[1]
	map[x][y].b = col_rail[2]
	map[x][y].is_rail=True

def set_route_squared(map,x0,y0,x1,y1):
	for x in range(x0+1,x1):
		set_rail(map,x,y0)
		set_rail(map,x,y1)
	for y in range(y0+1,y1):
		set_rail(map,x0,y)
		set_rail(map,x1,y)



set_route_squared(map,0,0,7,7)
draw_map(map,0,0)
