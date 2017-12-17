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
