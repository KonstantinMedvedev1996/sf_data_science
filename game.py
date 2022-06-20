import numpy as np

numbers = np.random.randint(1,101)
count = 0

while True:
    count += 1
    predict_number = int(input('Guess number from 1 to 100'))
    
    if predict_number > numbers:
        print('your number is high than the right number')
    
    elif predict_number < numbers:
        print('your number is less than the right number')
        
    else:
        print('your enter the right number {} for {} tries'.format(numbers, count))
        break
        