Unpublished Python library for for reading the output of processes with a time limit.

Tested on Linux and macOS with Python 3.7-3.9.

---

``` python3
from bgprocess import BackgroundProcess, LineWaitingTimeout

with BackgroundProcess(["some_program", "arg1", "arg2"]) as process:

    # The process is already up and running in background.
    # We can continue to perform operations in our program
    
    do_something()
    do_something_more()
    
    # ok, let's check how the process is doing

    try:
        # getting for the first line from the process output.
        # If no line was output, this call will wait for the line 
        # and only then will return the result
        str1 = process.next_line()
        
        # waiting for the second line from the process output
        str2 = process.next_line()
        
        # waiting for the next line, but not too long.
        # If the line does not appear in 0.25 seconds, 
        # LineWaitingTimeout exception will be raised
        str3 = process.next_line(read_timeout = 0.25)  # 0.25 seconds
        
        # skipping lines until we get the line matching the condition
        str4 = bp.next_line(match = lambda line: line.startswith('a'))
    
        # skipping lines until we get the line matching the condition.
        # If the mathing line does not appear in 3 seconds, 
        # LineWaitingTimeout exception will be raised 
        str5 = process.next_line(
            match = lambda line: line.startswith('a'),
            match_timeout = 3)
            
    except LineWaitingTimeout:
        # we may get this exception when running next_line with 
        # read_timeout or match_timeout 
        print("Timeout!")
```

If the process is finished, `next_line` returns `None` instead of a `str`.
