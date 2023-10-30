import random
r = random.randint(1., 100)
while True:
    
    answer = input('請猜數字：')
    if answer == 'q':
        break
    answer = int(answer)
    if answer == r:
        print('恭喜猜對了!')
        break    
    else:
        if answer < r:
            print('小於答案，請再猜一次。')
        else:
            print('小於答案，請再猜一次。')

