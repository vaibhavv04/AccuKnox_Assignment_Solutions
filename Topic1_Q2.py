import time
import threading
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Receiver that prints thread name and simulates work
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}")
    time.sleep(2)  # Simulate a 2-second task
    print("Receiver finished")

# Function to trigger the signal and print thread name
def trigger_signal():
    print(f"Caller running in thread: {threading.current_thread().name}")
    start_time = time.time()
    print("Sending signal")
    my_signal.send(sender=None)  # Trigger the signal
    print("Signal sent")
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

# Run the test
if __name__ == "__main__":
    trigger_signal()
