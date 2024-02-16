# funkcja SWITCH nie wystepuje w Pythonie
# jak ja zaimplementowac
# tak wyglada funkcja SWITCH z jezyka Java
'''
function(argument) {
    switch(argument) {
        case 0:
            return "lundi";
        case 1:
            return "mardi";
        case 2:
            return "mercredi";
        case 3:
            return "jeudi";
        case 4:
            return "vendredi";
        case 5:
            return "samedi";
        case 6:
            return "dimanche";
        default:
            return "! error !";
    };
};
'''

def WeekDayInFrench(daynumber):
    
    names = {
        0: 'lundi',
        1: 'mardi',
        2: 'mercredi',
        3: 'jeudi',
        4: 'vendredi',
        5: 'samedi',
        6: 'dimanche'
    }
    
    return names.get(daynumber,'error') # obsluga bledu jak za wysoka wartosc

print(WeekDayInFrench(4))
print(WeekDayInFrench(9))