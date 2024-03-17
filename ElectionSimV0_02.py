import math as m

# VERSION 0.01 - DHONDT ONLY

def main():
    print('Welcome to the election simulator V0.01!')
    print('Here, you can test out different apportionement') 
    print('methods and all that fun stuff :)')
    print()
    menu1()
    
def menu1():
    print('Main Menu')
    gamemode = input('1 - Proportional, 2 - Exit Program: ')
    while gamemode == '1':
        proportional()
        print('Main Menu')
        gamemode = input('1 - Proportional, 2 - Exit Program: ')

def floate(value):
    try:
        integer = float(value)
        return integer
    except ValueError:
        print('Invalid: Letters Inputted')
        return 0

# PROPORTIONAL
def proportional():
    print('Pick an allocation method')
    pmethod = input('1 - D\'hondt, 2 - Sainte Lague,  3 - Exit Program: ')
    while pmethod != '1' and pmethod != '2' and pmethod != '3':
        print('Invalid Selection')
        pmethod = input('1 - D\'hondt, 2 - Sainte Lague, 3 - Exit Program: ')
    while pmethod == '1' or pmethod == '2':
        if pmethod == '1':
            dhondt()
            print()
            print('Pick an allocation method')
            pmethod = input('1 - D\'hondt, 2 - Sainte Lague, 3 - Exit Program: ')
        if pmethod == '2':
            saintelague()
            print()
            print('Pick an allocation method')
            pmethod = input('1 = D\'hondt, 2 = Sainte Lague, 3 - Exit Program: ')

# D'hondt method
def dhondt():
    dhontdata = []
    dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    data = []
    if dhontinput != '1' and dhontinput != '2' and dhontinput != '3':
        print('Invalid Selection')
        print()
        dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    parties = 0
    totalp = 0
    while dhontinput == '1':
        party = []
        percent = 0
        party += [input('Party: ')]
        index = len(data)
        party += [index]
        print('Percent Left: '+str(100-totalp)+'      Note: Any leftover percentages will be converted to "Others"')
        percent = floate(input('Percentage: '))
        while percent == 0:
            print('Invalid Percent')
            percent = floate(input('Percentage: '))
        while percent > 100 - totalp:
            print('Percent over 100%!')
            percent = floate(input('Percentage: '))
            while percent == 0:
                print('Invalid Percent')
                percent = floate(input('Percentage: '))
        totalp += percent
        party += [percent]
        data += [party]
        parties += 1
        dhontinput = input('Choose a Party - 1, Run Program - 2, Exit Program - 3: ')
    if dhontinput == '2':
        parties += 1
        party = []
        party += ['Others']
        index = len(data)
        party += [index]
        party += [(100-totalp)]
        data += [party]
        seats = int(input('Number of Legislature Seats: '))
        tot = []
        winners = []
        for i in range(seats):
            for j in range(len(data)):
                tot += [[((data[j][2])/100)/(i+1),data[j][1]]]
        max1 = []
        indexmax = []
        maximum = []
        for i in range(len(tot)):
            max1 += [tot[i][0]]
        for i in range(len(tot)):
            indexmax += [tot[i][1]]
        for i in range(seats):
            finalmax = max(max1)
            indfinalmax = max1.index(finalmax)
            finalindex = indexmax[indfinalmax]
            maximum += [[finalmax,finalindex]]
            max1.pop(indfinalmax)
            indexmax.pop(indfinalmax)
        finalcount = []
        for i in range(len(maximum)):
            finalcount += [maximum[i][1]]
        results = []
        for i in range(parties):
            partycount = [finalcount.count(i)]
            partyindex = [data[i][0]]
            results += [[partycount,partyindex]]
        print()
        for i in range(len(results)):
            print(results[i][1][0],': ',results[i][0][0],' Seats')
            print()

# Sainte Lague method
def saintelague():
    dhontdata = []
    dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    data = []
    if dhontinput != '1' and dhontinput != '2' and dhontinput != '3':
        print('Invalid Selection')
        print()
        dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    parties = 0
    totalp = 0
    while dhontinput == '1':
        party = []
        percent = 0
        party += [input('Party: ')]
        index = len(data)
        party += [index]
        print('Percent Left: '+str(100-totalp)+'      Note: Any leftover percentages will be converted to "Others"')
        percent = floate(input('Percentage: '))
        while percent == 0:
            print('Invalid Percent')
            percent = floate(input('Percentage: '))
        while percent > 100 - totalp:
            print('Percent over 100%!')
            percent = floate(input('Percentage: '))
            while percent == 0:
                print('Invalid Percent')
                percent = floate(input('Percentage: '))
        totalp += percent
        party += [percent]
        data += [party]
        parties += 1
        dhontinput = input('Choose a Party - 1, Run Program - 2, Exit Program - 3: ')
    if dhontinput == '2':
        parties += 1
        party = []
        party += ['Others']
        index = len(data)
        party += [index]
        party += [(100-totalp)]
        data += [party]
        seats = int(input('Number of Legislature Seats: '))
        tot = []
        winners = []
        for i in range(seats):
            for j in range(len(data)):
                tot += [[((data[j][2])/100)/(2*i+1),data[j][1]]]
        max1 = []
        indexmax = []
        maximum = []
        for i in range(len(tot)):
            max1 += [tot[i][0]]
        for i in range(len(tot)):
            indexmax += [tot[i][1]]
        for i in range(seats):
            finalmax = max(max1)
            indfinalmax = max1.index(finalmax)
            finalindex = indexmax[indfinalmax]
            maximum += [[finalmax,finalindex]]
            max1.pop(indfinalmax)
            indexmax.pop(indfinalmax)
        finalcount = []
        for i in range(len(maximum)):
            finalcount += [maximum[i][1]]
        results = []
        for i in range(parties):
            partycount = [finalcount.count(i)]
            partyindex = [data[i][0]]
            results += [[partycount,partyindex]]
        print()
        for i in range(len(results)):
            print(results[i][1][0],': ',results[i][0][0],' Seats')
            print()

# Imperiali method
def imperiali():
    dhontdata = []
    dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    data = []
    if dhontinput != '1' and dhontinput != '2' and dhontinput != '3':
        print('Invalid Selection')
        print()
        dhontinput = input('Add a Party - 1, Run Program - 2, Back - 3: ')
    parties = 0
    totalp = 0
    while dhontinput == '1':
        party = []
        percent = 0
        party += [input('Party: ')]
        index = len(data)
        party += [index]
        print('Percent Left: '+str(100-totalp)+'      Note: Any leftover percentages will be converted to "Others"')
        percent = floate(input('Percentage: '))
        while percent == 0:
            print('Invalid Percent')
            percent = floate(input('Percentage: '))
        while percent > 100 - totalp:
            print('Percent over 100%!')
            percent = floate(input('Percentage: '))
            while percent == 0:
                print('Invalid Percent')
                percent = floate(input('Percentage: '))
        totalp += percent
        party += [percent]
        data += [party]
        parties += 1
        dhontinput = input('Choose a Party - 1, Run Program - 2, Exit Program - 3: ')
    if dhontinput == '2':
        parties += 1
        party = []
        party += ['Others']
        index = len(data)
        party += [index]
        party += [(100-totalp)]
        data += [party]
        seats = int(input('Number of Legislature Seats: '))
        tot = []
        winners = []
        for i in range(seats):
            for j in range(len(data)):
                tot += [[((data[j][2])/100)/(i+2),data[j][1]]]
        max1 = []
        indexmax = []
        maximum = []
        for i in range(len(tot)):
            max1 += [tot[i][0]]
        for i in range(len(tot)):
            indexmax += [tot[i][1]]
        for i in range(seats):
            finalmax = max(max1)
            indfinalmax = max1.index(finalmax)
            finalindex = indexmax[indfinalmax]
            maximum += [[finalmax,finalindex]]
            max1.pop(indfinalmax)
            indexmax.pop(indfinalmax)
        finalcount = []
        for i in range(len(maximum)):
            finalcount += [maximum[i][1]]
        results = []
        for i in range(parties):
            partycount = [finalcount.count(i)]
            partyindex = [data[i][0]]
            results += [[partycount,partyindex]]
        print()
        for i in range(len(results)):
            print(results[i][1][0],': ',results[i][0][0],' Seats')
            print()

main()
