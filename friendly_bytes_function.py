import math

def friendly_bytes(number, decimals=2, binary=False, keep_width=False):
    neg= False
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
    num_by_unit = round(number / p, decimals) 
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

for num in numbers: #on positive
    friendly_num= friendly_bytes(num)
    print("self.assertEqual(friendly_bytes(",num,"),'",friendly_num,"')")

for num in numbers: #on negative
    friendly_num= friendly_bytes(-num)
    print("self.assertEqual(friendly_bytes(-",num,"),'",friendly_num,"')")

for num in decimals: #on decimals
    friendly_num= friendly_bytes(num)
    print("self.assertEqual(friendly_bytes(",num,"),'",friendly_num,"')")

for num in decimals: #on decimals
    for i in range (10):
        friendly_num= friendly_bytes(num, decimals=i)
        print("self.assertEqual(friendly_bytes(",num,",decimals=,",i,"),'",friendly_num,"')")

for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=True)
    print("self.assertEqual(friendly_bytes(",num,", binary=True),'",friendly_num,"')")

for num in numbers: #on binary
    friendly_num= friendly_bytes(num, binary=False)
    print("self.assertEqual(friendly_bytes(",num,", binary=False),'",friendly_num,"')")



#print(friendly_bytes(2343234434535))