import random
import hashlib

source = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cheap_hash = lambda input: hashlib.sha384(input).hexdigest()[:81]
cmd = raw_input(">>> Input string(0 for random):")

seed = ""
i = 0
#enter = raw_input("input enter:")
#print enter,",strlen of enter:",len(enter)
if cmd=="0":
    for i in range(0,81):
        seed += str( source[random.randint(0,26)])
else:
    repeat = raw_input(">>> SHA time(enter for 1 time):")
    if len(repeat) == 0:
        i_repeat = 1
    else:
        try:
            i_repeat = int(repeat)
        except ValueError:
            print ">>> Error input, SHA only 1 time."
            i_repeat = 1
    for i in range(0,i_repeat):
        cmd = cheap_hash(cmd)
    for i in range(0,81):
        seed += str( source[ord(cmd[i])%27])
print ">>> SEED:",seed," Stringlen:",len(seed)
