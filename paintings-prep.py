from PIL import Image
import json
import os

# Define the maximum width and height
max_size = (800, 800)

# Define the quality
qual = 15

json_file = {
    'order':[],
    'paintings':[]
}

def compress(img_list: list):
    for i,file in enumerate(img_list):
        img = Image.open(f"./static/assets/artworks/{file}")
        file = file[:-4]
        file = file.replace('{CROP}','').strip()
        img_dict = {
            'sno':i+1,
            'name':file[:-4],
            'size':'',
            'details':'',
            'file':f'{file}.jpg'
        }
        json_file['paintings'].append(img_dict)
        img.resize(max_size,Image.LANCZOS)
        img.save(f"./static/assets/artworks_compressed/{file}.jpg", optimize=True, quality=qual)

image_list = [f for f in os.listdir('./static/assets/artworks') if f.endswith('.jpg')]

compress(image_list)

with open('./static/assets/paintings.json','w') as f:
    json.dump(json_file,f)