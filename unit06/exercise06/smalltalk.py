import re

#functions
def number_1to5(number):
    cond1 = len(number) == 1
    cond2 = number != '0'
    cond3 = re.match(r'\d', number)
    cond4 = number <= '5'
    return cond1 and cond2 and cond3 and cond4


# ask for mood
saved_mood = 0 

while True: 
    user_mood = input('How are you feeling today on a scale of 1 - 5? ')
    if number_1to5(user_mood):
        saved_mood = int(user_mood)
        break
    else:
        print('Please enter a number from 1 to 5')

if saved_mood >= 4:
    print('It is amazing that you have a good day!')
elif saved_mood >= 2:
    print('Keep your head up, your day will be better for sure!')
else:
    print('Consider doing something that cheers you up, or just simply take a coffee :D')


# ask for weather


while True:
    weather_opinion = input('Do you like the weather today? (yes or no answers only)')
    if weather_opinion == 'yes':
        print('That is great!')
        break
    elif weather_opinion == 'no':
        print('That is too bad')
        break
    else:
        print('Please answer with yes or no!')


