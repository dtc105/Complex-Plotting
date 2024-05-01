from PIL import Image, ImageColor
from modules.ComplexCalculator import ComplexCalculator
import re

class Plotter:
    #Takes in two complex numbers and returns them as a nested tuple
    def getDimensions() -> tuple:
        while True:
            #asks for the bottom left corner until it matches
            while True:
                try:
                    zIn = input("Bottom Left Corner (a+bi): ")
                    m = re.match(r"(-?\d+(\.\d+)?)([+-]\d+(\.\d+)?)i", zIn)
            
                    if m:
                        aLower = float(m.group(1))
                        bLower = float(m.group(3))
                        break
                    else:
                        raise Exception("Please input a complex number in the form a+bi\n")
                except Exception as e:
                    print(e)
            #asks for the top right corner until it matches
            while True:
                try:
                    zIn = input("Top Right Corner (a+bi): ")
                    m = re.match(r"(-?\d+(\.\d+)?)([+-]\d+(\.\d+)?)i", zIn)
            
                    if m:
                        aUpper = float(m.group(1))
                        bUpper = float(m.group(3))
                        break
                    else:
                        raise Exception("Please input a complex number in the form a+bi\n")
                except Exception as e:
                    print(e)
            #checks to see if the numbers make sense
            try:
                if (aUpper > aLower) and (bUpper > bLower):
                    break
                else:
                    raise Exception("Top Right Corner must have a greater real and imaginary part\n")
            except Exception as e:
                print(e)
        
        return ((aLower,bLower),(aUpper,bUpper))
    
    #Takes a nested tuple then asks for resolution along real axis and returns a tuple 
    def getResolution(z12) -> tuple:
        try:
            if (z12[0][0] < z12[1][0]) and (z12[0][1] < z12[1][1]):
                ratio = (z12[1][1]-z12[0][1])/(z12[1][0]-z12[0][0])
        except IndexError as e:
            print(e)
        
        try:
            x = int(input("How many pixels along real axis?: "))
        except TypeError as e:
            print(e)
        
        y = int(x * ratio)
        
        if y < 1:
            y = 1
        
        return (x, y)

    def makeImage(resolution, initial, dx, dy):
         im = Image.new('RGB', resolution)
         zIn = complex(initial[0], initial[1])
         
         for i in range(resolution[0]):
             for j in range(resolution[1]):
                 zOut = ComplexCalculator.function(zIn)
                 p = ComplexCalculator.polarForHSV(zOut)
                 im.putpixel((i,j), ImageColor.getrgb('hsv(' + str(p[1]) + ',100%,' + str(p[0]) + '%)'))
                 zIn = complex(zIn.real, zIn.imag - dy)
             zIn = complex(zIn.real, initial[1])
             zIn = complex(zIn.real + dx, zIn.imag)
                 
         im.save('img.png')