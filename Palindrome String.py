s='malayalam'
def palindrome(s):
    return s==s[::-1]
ans=palindrome(s)
if ans:
    print("yes")
else:
    print("no")

# Another Method 

t='kalyan'
w=""
for i in t:
    w=i+w
print(w)
if(t==w):
    print("yes")
else:
    print("no")
