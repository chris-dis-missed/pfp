def fizzbuzz(number):
    if type(number) != int:
        print('Not an integer!')
    else:
        for i in range(1, number+1):
            if i % 15 == 0 :
                yield "fizzbuzz"
            elif i % 5 == 0:
                yield "buzz"
            elif i % 3 == 0:
                yield "fizz"
            else :
                yield i 