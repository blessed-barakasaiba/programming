import os
if os.path.exists("document.txt"):
    f = open("document.txt", "r")
    print(f.read())
    f.close()
else:
    f = open("document.txt", "a")
    f.write("saiba your a rich")
    f =open("document.txt", "r")
    print(f.read())
    f.close()

g = open("document2.txt", "a")
g.write("hello baraka mwamakambaa ")
g= open("document2.txt", "r")
print(g.read())


h = open("document3.txt", "w")
h.write("hello baraka")
h = open("document3.txt", "r")
print(h.read())
h.close()

i = open("document.txt", "w")
i.write("hello baraka  i love you")
i = open("document.txt", "r")
print(i.read())
i.close()

if os.path.exists("document.txt"):
    os.remove("document.txt")
else:
    print("no such document")    


    
    
    
