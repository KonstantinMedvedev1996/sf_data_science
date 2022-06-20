''''   
game 'Guess the right number'
computer is guessing numbers itself

'''


import numpy as np

def random_predict(number:int=1) -> int:
    
    """ 'Guess number randomly'

    Args:
        number (int, optional): Invented number. Defaults to 1.

    Returns:
        int: Number of tries
    """    
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1,300)
        if number == predict_number:
            break
    return count

def score_game(random_predict)->int:
    """ How much tries does our algorithm need to guess the number for 1000

    Args:
        random_predict (_type_): 'guess function'

    Returns:
        int: tries' mean
    """    
    count_ls =[]
    np.random.seed(3)
    random_array = np.random.randint(1,101,size =(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print('your algorith guess the number approximatly for {}'.format(score))
    return score

if __name__ == '__main__':
    score_game(random_predict)  
    
