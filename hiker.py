# this can check the number of valley based on path input
# U abovesealevel
# D belowsealevel
#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_
# slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

if __name__ != '__hiker__':
    #path = "UDDDUDUU"
    path = "DDUUUUDD"
    #input path DOWN DOWN UP UP etc>>

    sea = 0  #sealevel counter
    valley = 0 #valey counter
    for p in path: #iterate path
        if p == "U": #check if above or below sea
            sea += 1
        elif p == "D":
            sea -= 1
        if p == "U" and sea == 0: # check for valley
            valley += 1
    print(valley) #return valley

