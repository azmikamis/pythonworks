from cImage import *

def verticalFlip(oldimage):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw,oldh)

    maxp = oldw-1      
    for row in range(oldh):
        for col in range(oldw):
            
            oldpixel = oldimage.getPixel(maxp-col,row)   

            newim.setPixel(col,row,oldpixel)  

    return newim
    
def resize(imageFile):
    myimagewindow = ImageWin("Image Processing",600,400)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)
    
    newimage = verticalFlip(oldimage)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()


def main():
    resize("mickey.gif")
    
main()