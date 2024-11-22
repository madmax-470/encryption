## rail fence encryption! with added row shifting functionality!!!

data = input("enter the data to encrypt: ")
depth = int(input("enter a number between 2 to 6 to define the depth: "))
datalist = list(data)
                       
def depth2():
    upperrow = ''.join(datalist[0::2]) # skips every second element in the list(string)
    lowerrow = ''.join(datalist[1::2])
    edata = upperrow + lowerrow
    print(edata)
    
    

def depth3():
    datalist = list(data)
    row1 = ''.join(datalist[0::3])
    row2 = ''.join(datalist[1::3])
    row3 = ''.join(datalist[2::3])


    edata = row1 + row2 + row3
    print(edata)


def depth4():
    datalist   = list(data)
    row1   = ''.join(datalist[0::4])
    row2 = ''.join(datalist[1::4])
    row3 = ''.join(datalist[2::4])
    row4   = ''.join(datalist[3::4])
    edata = row1 + row2 + row3 + row4
    print(edata)



def depth5():
    datalist    = list(data)
    row1    = ''.join(datalist[0::5])
    row2  = ''.join(datalist[1::5])
    row3  = ''.join(datalist[2::5])
    row4  = ''.join(datalist[3::5])
    row5    = ''.join(datalist[4::5])
    edata = row1 + row2 + row3 + row4 +  row5
    print(edata)
    
def depth6():
    datalist    = list(data)
    row1    = ''.join(datalist[0::6])
    row2  = ''.join(datalist[1::6])
    row3  = ''.join(datalist[2::6])
    row4  = ''.join(datalist[3::6])
    row5  = ''.join(datalist[4::6])
    row6    = ''.join(datalist[5::6])
    edata = row1 + row2 + row3 + row4 +  row5 + row6
    print(edata)

    
if depth == 2:
    depth2()
elif depth == 3:
    depth3()
elif depth == 4:
    depth4()
elif depth == 5:
    depth5()
elif depth ==6:
    depth6()



# I am thinking of adding a shuffling mechanism to it, if anyon's intrested can contribute!!!!
