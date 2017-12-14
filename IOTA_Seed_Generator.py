import random
import hashlib

source = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cheap_hash = lambda input: hashlib.sha384(input).hexdigest()[:81]
cmd = raw_input(">>> Input string(0 for random):")

seed = ""
i = 0
if cmd=="0":
    for i in range(0,81):
        seed += str( source[random.randint(0,26)])
else:
    tmp = cheap_hash(cmd)
    for i in range(0,81):
        seed += str( source[ord(tmp[i])%27])
print seed," stringlen:",len(seed)
