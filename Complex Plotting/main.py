from modules.plotter import Plotter
from modules.ComplexCalculator import ComplexCalculator
import cmath

def main():
    dimension = Plotter.getDimensions()
    resolution = Plotter.getResolution(dimension)
    
    dx = (dimension[1][0] - dimension[0][0]) / float(resolution[0])
    dy = (dimension[1][1] - dimension[0][1]) / float(resolution[1])

    Plotter.makeImage(resolution, (dimension[0][0], dimension[1][1]), dx, dy)
    
            
    

if __name__ == "__main__":
    main()

