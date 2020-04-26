import random
countof_T = 0
countof_H = 0
change = 0
sequenceof_T = 0
sequenceof_H = 0

for a in range(5):
    x = random.choice("HT")
    print(x)
    if a == 0:
        y = x
        if y == "H":
            sequenceof_H += 1
        else:
            sequenceof_T += 1
    if x == "H":
        countof_H += 1
        if x == y:
            sequenceof_H += 1
    else:
        countof_T += 1
        if x == y:
            sequenceof_T += 1
    if y != x:
        y = x
        change += 1

print("Heads came up",countof_H,"times.")
print("Tails came up",countof_T,"times.")
print("There were",change,"changes that occured.")
print(sequenceof_H,sequenceof_T)
