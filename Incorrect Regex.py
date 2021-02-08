# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def comprueba(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    
    print(comprueba(input()))