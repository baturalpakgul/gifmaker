from PIL import Image, ImageDraw

images=[]


width=200

center=width//2

color_1=(184,51,255)

color_2=(255,243,51)

max_radius=int(center*1.5)

step=8

for i in range(10):
    im=Image.new("RGB", (width,width), color_2)
    draw=ImageDraw.Draw(im)
    draw.ellipse((center-i, center-i, center+i, center+i),fill=color_1)

    images.append(im)

    images[0].save("pillow_imagedraw.gif", save_all=True, append_images=images[1:],optimize=False, duration=150)



