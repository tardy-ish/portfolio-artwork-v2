from PIL import Image
from pprint import pprint
import json
import os

# Define the maximum width and height
max_size = (800, 800)

# Define the quality
qual = 15

def compress(img_list: list,src :str,des :str):
    new_list = []
    for i,file in enumerate(img_list):
        file_new = file[:-4].lower()
        crop = ''
        if '{crop}' in file_new:
            file_new = file_new.replace('{crop}','').strip()
            crop = '[CROP]'
        file_new = file_new.replace('copy','').strip()
        name = file_new.title()
        fname = file_new.replace(' ','_')
        img = Image.open(f"{src}/{file}")
        img.resize(max_size,Image.LANCZOS)
        img.save(f"{des}/{fname}.jpg", optimize=True, quality=qual)
        
        temp_data ={
            'name':name,
            'crop':crop,
            'file':fname
        }
        # print(temp_data)
        new_list.append(temp_data)
    return new_list

def metaDataWrite(img_list: list, fld: str):
    keyList = ['year','size','details']
    for i,image in enumerate(img_list):
        name = image['name']
        fname = image['file']
        if os.path.isfile(f'{fld}/{fname}.json'):
            continue
        metaData = {
            'name':name,
            'year':'',
            'size':'',
            'details':'',
            'file':f"{fname}.jpg",
            'crop':image['crop']
        }
        print(f"For the painting {name}:")
        for key in keyList:
            metaData[key] = input(f'{key.title()}: ')
        with open(f'{fld}/{fname}.json','w') as f:
            json.dump(metaData,f)
        print()



src = './static/assets/images/artworks'
des = './static/assets/images/artworks_prepped'
image_list = [f for f in os.listdir(src) if f.endswith('.jpg')]

image_list = compress(image_list,src,des)

metaDataWrite(img_list=image_list,fld=des)

def wrap(f,des):
    return json.load(open(f'{des}/{f}'))

json_file = [wrap(f,des) for f in os.listdir(des) if f.endswith('.json')]


with open(f'./static/assets/paintings.temp.json','w') as f:
    json.dump(json_file,f)