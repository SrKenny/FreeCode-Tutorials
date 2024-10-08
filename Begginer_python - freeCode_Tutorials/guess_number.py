import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivinhe um número entre 1 e {x}: "))
        if guess < random_number:
            print("Desculpe, mas tente novamente. Muito baixo.")
        elif guess > random_number:
            print("Desculpe, mas tente novamente. Muito alto.")
    
    print(f"Nice. Parabéns você adivinhou o número {random_number} corretamente.")    

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed yout number {guess} correctly!')

guess(100)