from PIL import Image

def repaint(imagePath='main/picture.jpg', outputPath='main/newCopy.jpg', precision=5, lightFactor=0, contrastFactor=0, blendFactor=10):
    image = Image.open(imagePath)
    width, height = image.size
    for x in range(0,width,precision):
        for y in range(0,height,precision):
            sumR,sumG,sumB = 0,0,0
            for miniX in range(x,x+precision):
                for miniY in range(y,y+precision):
                    if(miniX>=width):miniX=width-1
                    if(miniY>=height):miniY=height-1
                    pixelColors = image.getpixel((miniX,miniY))
                    sumR+=pixelColors[0];sumG+=pixelColors[1];sumB+=pixelColors[2]
            averagePixel = Image.new('RGB',(precision,precision),((int) (sumR/pow(precision,2)+lightFactor+(sumR/pow(precision,2)-128)*contrastFactor),(int)(sumG/pow(precision,2)+lightFactor+(sumG/pow(precision,2)-128)*contrastFactor),(int)(sumB/pow(precision,2)+lightFactor+(sumB/pow(precision,2)-128)*contrastFactor)))
            prevColors1,prevColors2=(-1,-1,-1),(-1,-1,-1)
            if x>0:
                prevColors1 = image.getpixel((x-1,y))
            if y>0:
                prevColors2 = image.getpixel((x,y-1))
            if prevColors1 is not (-1,-1,-1):
                if abs(averagePixel.getpixel((0,0))[0]-prevColors1[0])+abs(averagePixel.getpixel((0,0))[1]-prevColors1[1])+abs(averagePixel.getpixel((0,0))[2]-prevColors1[2])<blendFactor*3:
                    averagePixel = Image.new('RGB',(precision,precision),prevColors1)
            if prevColors2 is not (-1,-1,-1):
                if abs(averagePixel.getpixel((0,0))[0]-prevColors2[0])+abs(averagePixel.getpixel((0,0))[1]-prevColors2[1])+abs(averagePixel.getpixel((0,0))[2]-prevColors2[2])<blendFactor*3:
                    averagePixel = Image.new('RGB', (precision, precision), prevColors2)

            image.paste(averagePixel,(x,y))
            image.save(outputPath)