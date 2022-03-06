import math
#not sure about how do the keep_width and decimals parameters work together.
#assumed that if the number is 10.02 with 2 decimal points and it's KB so there should be 
# 3 numbers after the decimal point according to keep_width=True, so 10.020 KB

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    if digits==0:
        return math.trunc(number)
    return math.trunc(stepper * number) / stepper

def friendly_bytes(number, decimals=2, binary=False, keep_width=False):
    neg= False
    if (abs (number) >0 and abs(number) < 1):
        return (str(number) +" B")  
    if (number< 0):
        number= (number*(-1))
        neg= True
    if (number== 0):
       return "0 B"
    size_units= ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    base= 1000
    if(binary):
        base=1024
    unitDesc = int(math.floor(math.log(number, base))) #to get the biggest unit that we can describe this number by
    p = math.pow(base, unitDesc) #the bytes to divide by
    num_by_unit = truncate(number / p, decimals) 
    unit= size_units[unitDesc]
    if(binary):
        if size_units[unitDesc]!= "B":
            unit= size_units[unitDesc][0]+"i"+size_units[unitDesc][1]
    if(neg):
        num_by_unit= (-1)*num_by_unit
    if keep_width:
        num_zeros= math.floor(math.log(p, 10))
        numStr= str(num_by_unit)
        if numStr != None and '.' in numStr:
            lenAfterDot =len(numStr.split('.')[1])
            zeros_string= '0'*(num_zeros-lenAfterDot+1)
            return str(num_by_unit)+zeros_string+" "+unit
    return (str(num_by_unit)+" "+unit)