word = "APPLE"

reversed = word[::-1]
ltr = []
ct = 0
for r in reversed:
    if ct < 2:
        ltr.append(r)
        ct += 1
print(reversed)
print("".join(ltr))