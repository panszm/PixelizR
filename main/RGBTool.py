from PIL import Image

def repaint(darknessBorder=100, lightBorder=200, imagePath='main/picture.jpg', outputPath='main/newCopy.jpg'):
    image = Image.open(imagePath)
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixelColors = image.getpixel((x,y))
            if pixelColors[0]<darknessBorder and pixelColors[1]<darknessBorder and pixelColors[2]<darknessBorder :
                image.putpixel((x,y),(0,0,0))
            elif pixelColors[0]>lightBorder and pixelColors[1]>lightBorder and pixelColors[2]>lightBorder:
                image.putpixel((x, y), (255, 255, 255))
            elif pixelColors[0]>pixelColors[1] and pixelColors[0]>pixelColors[2]:
                image.putpixel((x, y), (255, 0, 0))
            elif pixelColors[1]>pixelColors[0] and pixelColors[1]>pixelColors[2]:
                image.putpixel((x, y), (0, 255, 0))
            else:
                image.putpixel((x, y), (0, 0, 255))
    image.save(outputPath)