import timeit
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

join = str(input("Do you want to calculate the time the machine needs to proccess your input?\n ")).lower

if join() == 'y' or join() == 'yes':

    user_input = input("What is your input: ")

    @timer
    def calculate_input(user_input):
        calculate = timeit.Timer(lambda: list(user_input))
        elapsed_time = calculate.timeit(number=10000)
        print(f"Elapsed time: {elapsed_time:.6f}")
        return elapsed_time

    calculate_input(user_input)

else:
    print("Invalid answer or you dont want to")
