from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in shorter:
        if i in longer:
            longer = longer.replace(i, '', 1)
    return longer        

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))

# s = 'dododo' 
# str_new = s.replace('d', 'c', 0) 
# print(str_new) # cocodo