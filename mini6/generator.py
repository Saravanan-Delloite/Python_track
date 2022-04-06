def fib(number):
    number1=0
    number2=1
    sum=0
    i=2
    if number==1:
        yield 0
        return ""
    yield 0
    yield 1
    while i<number:
        sum=number2+number1
        yield sum
        number1=number2
        number2=sum
        i+=1

lst=fib(12)
print([i for i in lst])