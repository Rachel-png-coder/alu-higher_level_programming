#!/usr/bin/python3
for ascii_code  in range(97, 123):
    if(ascii_code == 101) or (ascii_code == 113):
        continue
        print(chr(ascii_code).format(), end="")
