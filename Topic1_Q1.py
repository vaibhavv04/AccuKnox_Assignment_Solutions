import time
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Receiver with a delay to simulate blocking work
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(3)  # Simulate a 3-second blocking operation
    print("Receiver finished")

# Function to trigger the signal and measure time
def trigger_signal():
    start_time = time.time()
    print("Sending signal")
    my_signal.send(sender=None)  # Trigger the signal
    print("Signal sent")
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

# Run the test
if __name__ == "__main__":
    trigger_signal()
