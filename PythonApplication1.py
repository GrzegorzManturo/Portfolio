#BMI calculator
while True:
    a = input('Do you prefere using metric system? Y/N: ')
    if a == 'Y' or a == 'y':
        w=input('Enter your weight in kilograms: ')
        h=input('Enter your height in meters: ')
        BMI=float(w)/(float(h)**2)
    elif a == 'N' or a == 'n':
        w=input('Enter your weight in pounds: ')
        h=input('Enter your height in inches: ')
        BMI=float(w)/(float(h)**2)*703

    BMI = round(BMI,3)

    if BMI < 18.5:
        print ('Your BMI equals to: ', BMI)
        print ('You are underweight')
    elif BMI >= 18.5 and BMI < 25:
        print ('Your BMI equals to: ', BMI)
        print ('Your weight is normal')
    elif BMI >= 25 and BMI < 30:
        print ('Your BMI equals to: ', BMI)
        print ('You are overweight')
    else:
        print ('Your BMI equals to: ', BMI)
        print ('You are obese')
