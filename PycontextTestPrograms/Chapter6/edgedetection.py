from cImage import *
import math

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


def convolve(anImage,pixelRow,pixelCol,kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1
    
    sum = 0
    for row in range(kernelRowBase,kernelRowBase+3):
        for col in range(kernelColumnBase,kernelColumnBase+3):
            kColIndex = col-kernelColumnBase
            kRowIndex = row-kernelRowBase
            
            apixel = anImage.getPixel(col,row)
            intensity = apixel.getRed()
            
            sum = sum + intensity * kernel[kRowIndex][kColIndex]
    
    return sum
    
def edgeDetect(theImage):
    grayImage = pixelMapper(theImage,grayPixel)    
    newim = EmptyImage(grayImage.getWidth(), grayImage.getHeight())
    black = Pixel(0,0,0)
    white = Pixel(255,255,255)
    xMask = [ [-1,-2,-1],[0,0,0],[1,2,1] ]
    yMask = [ [1,0,-1],[2,0,-2],[1,0,-1] ]      

    for row in range(1,grayImage.getHeight()-1):    
        for col in range(1,grayImage.getWidth()-1):   
            gx = convolve(grayImage,row,col,xMask)  
            gy = convolve(grayImage,row,col,yMask)
            g = math.sqrt(gx**2 + gy**2) 
            
            if g > 175:
                newim.setPixel(col,row,black)
            else:
                newim.setPixel(col,row,white)

    return newim    

def resize(imageFile):
    myimagewindow = ImageWin("Image Processing",600,400)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)
    
    newimage = edgeDetect(oldimage)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()


def main():
    resize("mickey.gif")
    
main()