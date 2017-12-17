# ex:5.3
alien_color='green'

if alien_color== 'green':
	print('You\'ve earned 5 point')

if alien_color =='red':
	print('no points for this alien')
	
# ex:5.4
if alien_color!='green':
	print("\nYou've earned 10 points")
else:
	print('\nYou\'ve earned 5 point')
	

#ex:5.5
alien_color='red'
if alien_color == 'green':
	print('You\'ve earned 5 points')
elif alien_color == 'Yellow':
	print('You\'ve earned 10 points')
elif alien_color == 'red':
	print('You\'ve earned 15 points')
else:
	print(' ')
	
'''• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.
'''
age=25
if age < 2:
	print('this is a baby')
elif age >=2 and age < 4:
	print('this is a toddler')
elif age >=4 and age < 13:
	print('this is a kid')
elif age >=13 and age < 20:
	print('this is a teenager')
elif age >=20 and age < 65:
	print('this is a adult')
else:
	print('this is an elder')