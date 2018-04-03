'''
 BMI = W / (H*H)
 W = weight_in_kilogram
 H = height_in_meters
'''

h = float(input("Въведете височина в метри: "))
w = float(input("Въведете тегло в килограми: "))

bmi = round(w/(h*h),2)

if bmi <= 18.8 :
    category = 'Underweight'
elif bmi > 18.5 and bmi <= 24.9:
    category = 'Normal'
elif bmi > 25 and bmi <= 29.9:
    category = 'Overweight'
else:
    category = 'Obesity'

print('Вашият BMI е {} и Вие сте в категория {}'.format(bmi,category))