#* https://python.plainenglish.io/making-a-synth-with-python-oscillators-2cb8e68e9c3b

#* Lazy Iteration
import time

#Function that processes values.
def some_function(value):
    time.sleep(1)
    return value * 2

# A generator expression
processed_values_gen = (some_function(i) for i in range(30))
next(processed_values_gen)
def generator_function():
    for i in range(30):
        yield some_function(i)

processed_values_gen = generator_function()
next(processed_values_gen)