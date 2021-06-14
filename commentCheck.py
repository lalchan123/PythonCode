cmt = input("Enter a comment.If valid,print valid and else print invalid:\n")
length = len(cmt)
if cmt[0]=='/' and cmt[1]=='/':
    print ("valid")
elif  (cmt[0]=='/' and cmt[1]=='/')or(cmt[length-2]=='*' and cmt[length-1]=='/'):
    print ("Valid")
else:
    print ("Invalid")