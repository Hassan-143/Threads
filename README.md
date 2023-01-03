# THREADS

The program uses the ‘threading module’ which provides a simple and powerful mechanism for creating and managing threads. A thread object is created with the target function and any arguments to be passed. It uses an event object to synchronize the threads and signal them to start and stop. The global keyword is used to declare a global variable only once, at the top of the file.

The Python program includes the ‘input_thread’ function that handles the user input and sets a global variable that the other threads can access. Next, the ‘reverse_thread,’ ‘capital_thread’, and ‘shift_thread’ functions wait for the input event before processing the input string and printing their results. In the shifting function, the isalpha( ) method is used to check if a character is a letter, along with the islower( ) method to check if a character is a lowercase before shifting the characters two times. This allows the program to skip the shift operation for non-letter characters and capital letters, making the code more efficient.

The main code includes the creation of thread objects for each thread. The threading.Thread( ) constructor takes the target function and any arguments for the specific function as arguments. Each thread starts executing on the start( ) method and the target function executes in a separate thread. Finally, to join all the threads, the join( ) method is used, so that the main thread waits for the other threads to finish before it exits the program. This helps to ensure that all threads have a chance to release any resources they are holding before the program exits.

![image](https://user-images.githubusercontent.com/74555200/210422612-bb4c168d-9051-478e-9743-a09405af6d88.png)

