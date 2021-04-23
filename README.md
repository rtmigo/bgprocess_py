Unpublished Python library for for reading the output of processes with a time limit.

``` python3
from bgprocess import BackgroundProcess, LineWaitingTimeout

with BackgroundProcess(["some_program", "arg1", "arg2"]) as bp:

    try:
        # waiting for the first line from the process output
        str1 = bp.next_line()
        
        # waiting for the second line from the process output
        str2 = bp.next_line()
        
        # waiting for the next line, but not too long
        str3 = bp.next_line(read_timeout=0.25)  # 0.25 seconds
        
        # skipping lines until we get the line mathing the condition
        str4 = bp.next_line(match = lambda line: line.startswith('a'))
    
        # skipping lines until we get the line matching the condition.
        # But if we cannot find the matching line after 3 seconds, getting None 
        str5 = bp.next_line(
            match = lambda line: line.startswith('a'),
            match_timeout = 3)
            
    except LineWaitingTimeout:
        # we may get this exception when running next_line with 
        # read_timeout or match_timeout 
    
        print("Timeout!")
```

If the process is finished, `next_line` returns `None` instead of a `str`.



