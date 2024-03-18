from PIL import Image

print("### START Kapitel 1 ###")

originalJPG = Image.open("example1.png")
size = originalJPG.size
original = originalJPG.load()
newImage = Image.new(mode="RGB", size=size)
newPixel = newImage.load()
for x in range(size[0]):
    for y in range(size[1]):
        r, g, b = original[x, y]
        grey = int((r + g + b) / 3.0)
        newPixel[x, y] = (grey, grey, grey)

newImage.save("newImage.png")
print("### ENDE ###")