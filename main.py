import photographer as pg
import ripper as rip
import json

data = json.load(open('config.json', 'r'))
photographer = pg.Photographer(data['base_url'],data['base_name'])
ripper       = rip.Ripper(data['split_height'],data['base_name'])

for path in data['paths']:
    for width in data['device_widths']:
        img = photographer.get_image(path[0],path[1],width)
        ripper.split_image(img,path[0]+"_"+str(width))
