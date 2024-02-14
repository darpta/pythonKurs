age = 27
isDrunk = False
isRestrictedArea = False

if age < 18:
    print('You are too young to buy alcohol')
elif isDrunk:
    print('Are you drunk? We cannot sell you alcohol')
elif isRestrictedArea:
    print('Restricted area. Alcohol is forbiden')
else:
    print('Ok, you can buy alcohol')

''' --- if zagniezdzony
if age < 18:
    print('You are too young to buy alcohol')
else:
    if isDrunk:
        print('Are you drunk? We cannot sell you alcohol')
    else:
        if isRestrictedArea:
            print('Restricted area. Alcohol is forbiden')
        else:
            print('Ok, you can buy alcohol')
'''

# zadania

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 300
num_shares= 550

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    if num_likes <MIN_LIKES:
        print('We still need more likes to start the promotion')
    else:
        print('We still need more shares to start the promotion')

##############################################

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
elif num_likes <MIN_LIKES:
     print('We still need more likes to start the promotion')
else:
     print('We still need more shares to start the promotion')

##############################################

isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
else:
    if isWeekend:
        print('Come back on non-Weekend day')
    else:
        print('You need to order Pizza or Big drink to have a Burger coupon')

##############################################

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
elif isWeekend:
    print('Come back on non-Weekend day')
else:
    print('You need to order Pizza or Big drink to have a Burger coupon')