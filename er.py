import re


while True:
    i = re.search(r"""([-+]?\d+)   # first match
                      ([^0-9+-]+)? # delimiter
                      ([-+]?\d+)?  # second match
                      ([^0-9+-]+)? # delimiter
                      ([-+]?\d+)?  # third match
                      ([^0-9+-]+)? # delimiter
                      ([-+]?\d+)?  # fourth match
                      ([^0-9+-]+)? # delimiter
                      ([-+]?\d+)?  # last match
                      """,
                  input("? ").strip(),
                  re.VERBOSE)
    print(i)
    print(i.groups())
    
    for n in range(1, 10, 2):
        a = i.group(n) if i.group(n) else 'wtf'
        print(a)
    