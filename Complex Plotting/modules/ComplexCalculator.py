import cmath

class ComplexCalculator:
    #calculates a complex function at z, returns 0 if error occurs
    def function(z) -> complex:
        i = complex(0,1)
        try:
            zOut = (z**2 - 1) * (z - 2 - i) ** 2 / (z**2 + 2 + 2 * i)
        except Exception as e:
            return 0+0j
        return zOut
    
    def polarForHSV(z):
        r = round(100 - 100 / (1 + cmath.polar(z)[0] ** 2), 3)
        arg = int((cmath.polar(z)[1] * 180 / cmath.pi) % 360)
        
        return (r, arg)