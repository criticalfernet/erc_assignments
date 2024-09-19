

def calc_area(side1, side2, side3):
    semi = (side1 + side2 + side3)/2
    area_sqr = semi*(semi-side1)*(semi-side2)*(semi-side3)
    area = area_sqr ** 0.5
    return area

_side1 = float(input("Side 1:"))
_side2 = float(input("Side 2:"))
_side3 = float(input("Side 3:"))
print(calc_area(_side1,_side2,_side3))
