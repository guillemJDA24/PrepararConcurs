from PIL import Image, ImageDraw

img = Image.new('RGB', (600, 400), 'White')
dib = ImageDraw.Draw(img)

dib.ellipse([150, 50, 449, 349], 'Crimson')
dib.ellipse([125, 35, 400, 300], 'Blue')
img.save('output.png')