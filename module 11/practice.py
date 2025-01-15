from PIL import Image

def new_photo(name):
    image = Image.open(name)
    print (image.format, image.size, image.mode)
    w, h = image.size
    return  image.resize((w//2, h//2))

im = new_photo("supra.jpg")
im_2 = new_photo("image.png")


im.paste(im_2,(0, 0))

im.show()