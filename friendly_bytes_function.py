#If some of the rules are not clear enough, take a decision and describe it in your explanations.
#any restrictions on the number the functions gets? does it have to be an integer/ whole?
#right now I decide it must be an integer, for simplicity

from math import log

def friendly_bytes(number, decimals=2, binary=False, keep_width=False):
    #using log rules to determine what's the biggest unit we can use to describe this number
    #and using conversion rules to convert from base 1000 to 1024 whether the parameter binary=True
    unitNum = log(number)
    numByUnit=0
    unit=""
    if unitNum < 3:
       numByUnit=number
       unit= "B"
    if unitNum >=3 and unitNum <6:
        numByUnit= number/1000
        unit="KB"
        if (binary):
            unit= "KiB"
            numByUnit= numByUnit/1.02400
    if unitNum >= 6 and unitNum <9 :
        numByUnit= number/1000000
        unit= "MB"
        if (binary):
            unit= "MiB"
            numByUnit= numByUnit/1.048576

    if unitNum >= 9 and unitNum < 12:
        numByUnit= number/1000000000
        unit= "GB" 
        if (binary):
            unit= "GiB"
            numByUnit= numByUnit/1.07374182

    if unitNum >= 12 and unitNum < 15:
        numByUnit= number/1000000000000
        unit= "TB" 
        if (binary):
            unit= "TiB"
            numByUnit= numByUnit/1.09951163

    if unitNum >= 15 and unitNum < 18:
        numByUnit= number/10^15
        unit= "PB" 
        if (binary):
            unit= "PiB"
            numByUnit= numByUnit/1.12589991

    if unitNum >= 18 and unitNum < 21 :
        numByUnit= number/10^18
        unit = "EB"
        if (binary):
            unit= "EiB"
            numByUnit= numByUnit/1.1529215

    if unitNum >= 21 and unitNum < 24:
        numByUnit= number/10^21
        unit= "ZB" 
        if (binary):
            unit= "ZiB"
            numByUnit= numByUnit/1.1805916207174

    if unitNum > 24 and unitNum < 27:
        numByUnit= number/10^24
        unit= "YB" 
        if (binary):
            unit="YiB" 
            numByUnit= numByUnit/1.2089258196146
    finalNum =round(numByUnit,decimals) #to truncate the num according to the parameter decimal.
    return(finalNum, " ",unit)

print(friendly_bytes(333))