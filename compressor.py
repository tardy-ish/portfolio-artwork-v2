from PIL import Image
import os
src = './static/assets/images/artworks'
des = './static/assets/images/exhibitions_prepped'
max_size = (800, 800)
qual = 15
img_list = [img for img in os.listdir(src)]

def compress(img_list: list,src :str,des :str):
    for i,file in enumerate(img_list):
        img = Image.open(f"{src}/{file}")
        img.resize(max_size,Image.LANCZOS)
        img.save(f"{des}/{file}", optimize=True, quality=qual)

compress(img_list=img_list,src=src,des=des)