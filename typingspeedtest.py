import time

# Define the test text
test_text = "The quick brown fox jumps over the lazy dog."

# Print the test text and start the timer
print(test_text)
start_time = time.perf_counter()

# Get the user's input and stop the timer
typed_text = input()
end_time = time.perf_counter()

# Calculate the elapsed time and the typing speed (in words per minute)
elapsed_time = end_time - start_time
typing_speed = len(test_text.split()) / (elapsed_time / 60)

# Print the results
print("Time elapsed: {:.2f} seconds".format(elapsed_time))
print("Typing speed: {:.2f} words per minute".format(typing_speed))
