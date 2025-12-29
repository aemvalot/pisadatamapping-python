from p5 import *
from regions import get_region_coords

region_list = []
pins = []
map_img = None


def preload():
    global map_img
    map_img = load_image('mercator_bw.png')
    if map_img:
        print(f"Map loaded: {map_img.width} x {map_img.height}")
    else:
        print("Failed to load map image")


def setup():
    size(991, 768)        # EXACTLY the image size
    preload()
    load_data ('/home/user/pisa-project/pisa-results.csv')
   # load_data('pop.csv')
    background(255)


def draw():
    if map_img:
        image(map_img, 0, 0)   # NO scaling

    draw_data()


def draw_pin(x, y, colour):
    no_stroke()
    fill(colour)
    rect(x - 5, y - 5, 10, 10)   # center pin


def load_data(file_name):
    with open(file_name) as f:
        for line in f:
            info = line.strip().split(',')
            region_list.append({
                'region': info[0],
                'mean_score': info[1],
                'start_deviation': info[2]
            })


def draw_data():
    pins.clear()
    green_value = 255

    for region in region_list:
        coords = get_region_coords(region['region'])

        x = coords['x']
        y = coords['y']

        colour = Color(0, max(0, green_value), 0)
        draw_pin(x, y, colour)

        pins.append({
            'x': x - 5,
            'y': y - 5,
            'w': 10,
            'h': 10,
            'data': region
        })

        green_value -= 1


def mouse_pressed():
    for pin in pins:
        if (
            pin['x'] <= mouse_x <= pin['x'] + pin['w'] and
            pin['y'] <= mouse_y <= pin['y'] + pin['h']
        ):
            d = pin['data']
            print('Country : ', d['region'])
            print('Average score in mathematics : ', d['mean_score'])
          #  print('Population density:', d['population_density'])
            return

    print('Region not detected')


run()
