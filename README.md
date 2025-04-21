# AccuKnox_Assignment_Solutions
**Solutions for Django Trainee at Accuknox**

As mentioned in the assignment, the code does not need to be elegant and production ready so I have focused on logic alone and tried to explain it with comments.

**Resources that I have used** : django documentation, geekforgeeks, vscode IDE, git, and github

### Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Django signals are executed synchronously. When a signal is sent, the connected receivers are called immediately in the same thread, blocking the sender until all receivers complete.

<ins>**Code Explanation**</ins>

**Signal Definition:** my_signal = Signal() creates a custom signal.

**Receiver:** my_receiver is connected to my_signal using the @receiver decorator. It includes a 3-second time.sleep() to simulate a time-consuming task.

**Trigger Function:** trigger_signal sends the signal and measures the time taken from sending to completion.

**Synchronous Proof:** If the signal is synchronous, the time.sleep(3) in the receiver will block the main thread, and the total time taken will be approximately 3 seconds. If it were asynchronous, the signal would return immediately, and the total time would be near 0 seconds.

<ins>**Expected Output**</ins>

![image](https://github.com/user-attachments/assets/a00f5844-efe7-4c4a-99c0-e5001e227777)


<ins>**Conclusion**</ins>

The output shows that "Signal sent" appears after the receiver completes, and the total time is ~3 seconds, proving that the signal is executed synchronously. The main thread waits for the receiver to finish before continuing, as evidenced by the delay and timing. If the signal were asynchronous, "Signal sent" would print immediately, and the total time would be near 0 seconds.

### Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Django signals run in the same thread as the caller, as they are executed synchronously. When a signal is sent, the receivers are called immediately in the same thread, blocking the caller until all receivers complete.

<ins>**Code Explanation**</ins>

**Signal Definition:** my_signal = Signal() creates a custom signal.

**Receiver:** my_receiver is connected to my_signal and prints the current thread’s name using threading.current_thread().name. A 2-second time.sleep() simulates a blocking task.

**Trigger Function:** trigger_signal prints the caller’s thread name, sends the signal, and measures the time taken. It runs in the main thread (typically named "MainThread").

**Thread Proof:** If the receiver runs in the same thread as the caller, both will print the same thread name (e.g., "MainThread"). The total time taken will be ~2 seconds, confirming synchronous execution in the same thread. If the receiver ran in a different thread (asynchronous), the thread names would differ, and the total time would be near 0 seconds.
Timing: The timing measurement reinforces synchronicity, as the caller waits for the receiver’s 2-second delay.

<ins>**Expected Output**</ins>

![image](https://github.com/user-attachments/assets/da6b17d1-4047-42ec-b6b5-842c7548230c)

<ins>**Conclusion**</ins>

The output shows:

Both the caller and receiver run in the "MainThread", proving they execute in the same thread.
The total time is ~2 seconds, confirming synchronous execution, as the caller waits for the receiver’s 2-second delay.
This aligns with Django’s default behavior, where signals are processed in the caller’s thread, blocking until all receivers complete.


### Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Django signals do not automatically run in the same database transaction as the caller.

<ins>**Code Explanation**</ins>

**Setup:** The script configures Django to use an in-memory SQLite database and defines two models: User and Log. The post_save signal on User triggers a receiver that creates a Log entry.

**Receiver:** The log_user_creation receiver creates a Log entry when a User is saved, simulating a database operation that depends on the caller’s action.

**Test Function:** test_signal_transaction:

Creates the necessary database tables.

Starts a transaction using transaction.atomic().

Creates a User, which triggers the post_save signal and the receiver’s Log creation.

Checks the Log count to confirm the receiver’s action.

Raises an exception to force a transaction rollback.

After the rollback, checks the counts of User and Log objects.

**Transaction Proof:** If the receiver’s database operation (Log.objects.create) runs in the same transaction as the caller’s User.objects.create, the rollback will undo both the User and Log creation, resulting in zero counts for both. If the receiver operated in a separate transaction, the Log entry would persist despite the rollback.

<ins>**Expexted Output**</ins>

![image](https://github.com/user-attachments/assets/2e26bb8c-7bbb-483f-a9cc-d16e416fec7f)

<ins>**Conclusion**</ins>

The output demonstrates that Django signals’ database operations run in the same database transaction as the caller by default:

The User creation triggers the post_save signal, and the receiver creates a Log entry.
During the transaction, the Log count is 1, showing the receiver’s action took effect.

After the deliberate rollback, both the User and Log counts are 0, proving that the receiver’s Log.objects.create was part of the same transaction as the caller’s User.objects.create. If the receiver operated in a separate transaction, the Log entry would have persisted (e.g., Log count: 1).

This confirms that, for signals like post_save, the receiver’s database operations use the same database connection and transaction context as the caller, unless explicitly overridden (e.g., by using a different connection or transaction.atomic() in the receiver).

# Task - Custom Classes in Python

An instance of the Rectangle class requires length:int and width:int to be initialized.

We can iterate over an instance of the Rectangle class 

When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

<ins>**Code Explanation**</ins>

**Initialization:** __init__ takes length: int and width: int, stores them as self.length and self.width.

**Iterability:** __iter__ uses a generator to yield {'length': <value>} first, then {'width': <value>}.

**Purpose:** Creates an iterable class that produces two dictionaries in the specified order when looped over (e.g., for item in rect).

<ins>**Expected Output**</ins>

![image](https://github.com/user-attachments/assets/51b4c08d-dd17-4182-aed0-3d76c41855a6)

<ins>**Conclusion**</ins>

Yields {'length': 14} then {'width': 31}, in the correct order and format.

