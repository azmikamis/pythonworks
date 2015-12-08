from cImage import *

def double(oldimage):
    oldw = oldimage.getWidth()    
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw*2,oldh*2)   

    for row in range(oldh):
        for col in range(oldw):
            oldpixel = oldimage.getPixel(col,row)
            
            newim.setPixel(2*col,2*row,oldpixel)   
            newim.setPixel(2*col+1,2*row,oldpixel)
            newim.setPixel(2*col,2*row+1,oldpixel)
            newim.setPixel(2*col+1,2*row+1,oldpixel)  

    return newim
    
def resize(imageFile):
    myimagewindow = ImageWin("Image Processing",600,400)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)
    
    newimage = double(oldimage)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()


def main():
    resize("mickey.gif")
    
main()