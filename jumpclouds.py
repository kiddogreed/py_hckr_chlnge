#cloud jumping game
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_
# l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#return minimum/least required jumps from [0] to the last [c] while avoiding 1
#only allowed to jump beween 0
c = [0, 0, 1, 0, 0, 1, 0]
#sample input

#0010010
ctr = 0 #counters
jmp = 0 #number of jumps
if len(c) == 1:
    print(0) #check if the length of array is 1 then return 0
while ctr < len(c):  #iterating the array within len
    if ctr+2 < len(c) and c[ctr+2] == 0: #check if adding 2 steps on counter and still lower than the length
        jmp += 1  #add 1 jump
        ctr += 2 #add 2 ctr
    elif ctr + 1 < len(c) and c[ctr+1] == 0: #check if adding 1 step on counter and still lower than len
        jmp += 1
        ctr += 1 # add 1 to both
    else:
        ctr += 1 #else continue adding 1 to counter until finished within the len
print(jmp)# return the final number of jumps
