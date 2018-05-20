from PIL import Image
im = Image.open("F:\\123.jpg")
r,g,b = im.splist()
om = Image.merge("RGB",(g,r,b))
om.save("F:\\ps后图.jpg")
