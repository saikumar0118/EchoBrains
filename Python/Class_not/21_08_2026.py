# regex, regular data expression
'''which is contain the the matipul files in daid the folder is clla '''
import re
text="my is 20 amd my friend is 30  @ $ #"
result=re.search(r"[^a-zA-Z\s]","X",text)
print(result)

import re
text="my is 20 amd my friend is 30  @ $ #"
result=re.findall(r"\d","X",text)
print(result)

import re
text="my is 20 amd my friend is 30  @ $ #"
result=re.match(r"[^a-zA-Z\s]","X",text)
print(result)


import re
text="my is 20 amd my friend is 30  @ $ #"
result=re.sub(r"[^a-zA-Z\s]","X",text)
print(result)

#exception handaling 
'''we dont knw the error 
"except exception as e:"if we dont know type of errors then we use this to call 
print("Type Error",e)
"finally:" if error occur also this will print parmanent printing.
"except" after "try" block we can use multiple times as elif block
"raise" without print statment it prints the valuves
"try" we can use this only ones like if condition
'''