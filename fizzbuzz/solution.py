counter_3 = 1
counter_5 = 1
for number in range(1,100):
    if counter_3==3:
        counter_3=0
    if counter_5==5:
        counter_5=0

    if counter_3==0 and counter_5==0:
        print('FizzBuzz')
    elif counter_3==0:
        print('Fizz')
    elif counter_5==0:
        print('Buzz')
    else:
        print(number)

    counter_3+=1
    counter_5+=1
