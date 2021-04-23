Unpublished Python library for for reading the output of processes with a time limit.

``` python

from bgprocess import BackgroundProcess, LineWaitingTimeout

with BackgroundProcess(["some_program", "arg1", "arg2"]) as bp:

    # waiting for the first line from the process output
    str1 = bp.next_line()
    
    # waiting for the second line from the process output
    str2 = bp.next_line()
    
    # reading next line, but not waiting too long.
    # If process does not print anything, getting None
    str3_or_none = bp.next_line(read_timeout=0.25)  # 0.25 seconds
    
    # skipping lines until we get the line mathing the condition
    matched1_or_none = bp.next_line(match = lambda line: line.startswith('a'))

    # skipping lines until we get the line mathing the condition.
    # But if we cannot find the matching line after 3 seconds, getting None 
    matched2_or_none = bp.next_line(
        match = lambda line: line.startswith('a'),
        match_timeout = 3)
```



