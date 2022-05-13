#https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l
# =interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#this take string input which will define the patern of infinite str
# and a number which define the length of the string

s = "abcac" #string patern
n = 1000000000000000000 #number of repetions of the pattern

first = s.count("a") #initial count of index of a patern
second = n//len(s) # get the floor value of the length
third = s[:n % len(s)].count("a") # find item on the final number of list define [:n]

print(f"{first * second + third}") #using fstring to concatinate and add math operation between

#this is sample nodejs version for the code above
#function repeatedString(s, n) {
# let
# c = 0,
# ca = 0,
# r = n % s.length
#
# for (let i = s.length; i-- > 0;) {
# if (s.charAt(i) == 'a') {
# ++c
#
# if (i < r)
# ++ca
# }
# }
#
# return ((n - r) / s.length * c) + ca
#}