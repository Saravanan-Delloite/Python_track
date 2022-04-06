def sample(func):
    def multiply(num1, num2):
        func(num1,num2)
        func(num1,num2)
    return multiply
@sample
def test(num1,num2):
    print(num1+num2)

lst=test(2,2)
print(lst)