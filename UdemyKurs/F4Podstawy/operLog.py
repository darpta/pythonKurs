# == is equal
# != not equal
# > greater than
# >= greater or equal

IsWeekend = True    # True i False z duzej litery, a 'and' 'or' 'not' z malej
Temperature = 22
ToDoList = ''

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print('Is Happy =', IsHappy)

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != '' # 'not Temperature < 20'
print('Is Happy =', IsHappy)

IsWeekend = False
Temperature = 18
ToDoList = 'Shopping'

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
print('Is Happy =', IsHappy)

# zadania

# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = True
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = False
 
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)