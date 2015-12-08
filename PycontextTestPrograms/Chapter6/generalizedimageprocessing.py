from cImage import *

def negativePixel(oldPixel):
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel

def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + \
                   oldpixel.getBlue()
    aveRGB = intensitySum // 3

    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel

def pixelMapper(oldimage,rgbFunction):

    width = oldimage.getWidth()          
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)     

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = rgbFunction(originalPixel)          
            newim.setPixel(col,row,newPixel)
            
    return newim

def generalTransform(imageFile):
    myimagewindow = ImageWin("Image Processing",600,200)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)
    
    newimage = pixelMapper(oldimage,grayPixel)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()


def main():
    generalTransform("mickey.gif")
    
main()