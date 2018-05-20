from PIL import Image
from PIL import ImageFilter
im = Image.open("F:\\人像.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("F:\\人像轮廓.jpg")
