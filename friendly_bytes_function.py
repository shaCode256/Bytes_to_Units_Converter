import math

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
    if decimals is not 0:
        num_by_unit = round(number / p, decimals) 
    if decimals is 0:
        num_by_unit= math.trunc(number/p)
    unit= size_units[unitDesc]
    if(binary):
        if size_units[unitDesc]!= "B":
            unit= size_units[unitDesc][0]+"i"+size_units[unitDesc][1]
    if(neg):
        num_by_unit= (-1)*num_by_unit
    return (str(num_by_unit)+" "+unit)

numbers= (212321, 45450, 903428347234, 238942.443, 8343493409.22212, 840933049, 0, 0.00, 483434093, 24, 24.0, 0.3, 90.59438934, 122133, 328939324239329234, 3434904393490, 349823093209, 332423.3232432, 48234023409, 32.3, 239023932, 0, 11)
decimals= (43443.2334243, 43456.879889, 12223.889, 32324.009, 873489732.079067, 1283.003643, 38732.3402424, 11.22, 32873298329.32, 3832.1)
small= (0, 0.00, 0.00001, 0.00000009)
allSizes= ( 1230000000000000000 ,4300000000000000000000,1000000000000000000000000, 51000000000000000000000000)



print("import pytest")
print("from friendly_bytes_function import friendly_bytes")

print ("def test_on_positive():")
for num in numbers: #on positive
    friendly_num= friendly_bytes(num)
    print("assert(friendly_bytes(",num,") == '",friendly_num,"')")

print ("def test_on_negative():")
for num in numbers: #on negative
    friendly_num= friendly_bytes(-num)
    print("assert(friendly_bytes(-",num,") == '",friendly_num,"')")

print ("def test_on_decimals():")
for num in decimals: #on decimals
    friendly_num= friendly_bytes(num)
    print("assert(friendly_bytes(",num,") == '",friendly_num,"')")

print("def test_decimal_parameter():")
for num in decimals: #on decimals
    for i in range (10):
        friendly_num= friendly_bytes(num, decimals=i)
        print("assert (friendly_bytes(",num,",decimals=",i,") == '",friendly_num,"')")

print ("def test_binary_parameter():")
for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=True)
    print("assert (friendly_bytes(",num,", binary=True) == '",friendly_num,"')")

print ("def test_false_binary_parameter():")
for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=False)
    print("assert(friendly_bytes(",num,", binary=False) == '",friendly_num,"')")

print ("def test_eb_to_yb_sizes():")
for num in allSizes: #big sizes
    for i in range (7):
        friendly_num= friendly_bytes(i*num)
        print("assert(friendly_bytes(",i*num,", binary=False) == '",friendly_num,"')")



#print(friendly_bytes(2343234434535))