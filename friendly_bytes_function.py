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

numbers= (212321, 45450, 903428347234, 238942.443, 8343493409.22212, 840933049, 0, 0.00, 483434093, 24, 24.0, 0.3, 90.59438934, 122133, 328939324239329234, 3434904393490, 349823093209, 332423.3232432, 48234023409, 32.3, 239023932, 0, 11)
decimals= (43443.2334243, 43456.879889, 12223.889, 32324.009, 873489732.079067, 1283.003643, 38732.3402424, 11.22, 32873298329.32, 3832.1)
small= (0, 0.00, 0.00001, 0.00000009)
allSizes= ( 1230000000000000000 ,4300000000000000000000,1000000000000000000000000, 51000000000000000000000000)



print("import pytest")
print("from friendly_bytes_function import friendly_bytes")
print("")
print ("def test_on_positive():")
print("")
for num in numbers: #on positive
    friendly_num= friendly_bytes(num)
    print("    assert(friendly_bytes(",num,") == '",friendly_num,"')")
print("")
print ("def test_on_negative():")
print("")
for num in numbers: #on negative
    friendly_num= friendly_bytes(-num)
    print("    assert(friendly_bytes(-",num,") == '",friendly_num,"')")
print("")
print ("def test_on_decimals():")
print("")
for num in decimals: #on decimals
    friendly_num= friendly_bytes(num)
    print("    assert(friendly_bytes(",num,") == '",friendly_num,"')")
print("")
print("def test_decimal_parameter():")
print("")
for num in decimals: #on decimals
    for i in range (10):
        friendly_num= friendly_bytes(num, decimals=i)
        print("    assert (friendly_bytes(",num,",decimals=",i,") == '",friendly_num,"')")
print("")
print ("def test_binary_parameter():")
print("")
for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=True)
    print("    assert (friendly_bytes(",num,", binary=True) == '",friendly_num,"')")
print("")
print ("def test_false_binary_parameter():")
print("")
for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=False)
    print("    assert(friendly_bytes(",num,", binary=False) == '",friendly_num,"')")
print("")
print ("def test_eb_to_yb_sizes():")
print("")
for num in allSizes: #big sizes
    for i in range (7):
        friendly_num= friendly_bytes(i*num)
        print("    assert(friendly_bytes(",i*num,", binary=False) == '",friendly_num,"')")
print("")
print ("def test_keep_width_true():")
print("")
for num in numbers: #big sizes
    for i in range (7):
        friendly_num= friendly_bytes(i*num, keep_width=True)
        print("    assert(friendly_bytes(",i*num,", keep_width=True) == '",friendly_num,"')")