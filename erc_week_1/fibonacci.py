
def fibonacci(index):
    terms = [1,1]

    if (index > 2):
        for i in range(2,index):
            _val = terms[i-2] + terms[i-1]
            terms.append(_val)

    return terms



# we are using the function print_arr to make sure we dont directly print from the fibonacci function
# it is generally considered a good practise to keep input/output control out of logical functions.
# and have seperate specific functions for input and output control

def print_arr(list):
    for item in list:
        print(item)

number = int(input("Enter the number of terms:"))


print_arr(fibonacci(number))
