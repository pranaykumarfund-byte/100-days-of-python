nm = "Pranay"
print(len(nm))
# nm[0] = "y",strings are immutable
print(nm)
print(nm.upper())
print(nm.lower())
nm1 = "pranay!!!!!!"
print(nm1)
print(nm1.rstrip("!"))
nm2 = "!!!!pranay!!!!!pranay!!!"
print(nm2.replace("pranay","kinkytail"))
nm3 = "!!! pranay kumar !!!"
print(nm3.split(" "))
blogHeading ="introduction to python"
print(blogHeading.capitalize())  
blogHeading1 = "introductioN tO jS"
print(blogHeading1.capitalize())
str = "welcome to the vit-ap"
print(str)
print(str.center(50))
print(str.center(20))
print(str.center(60))
print(str.center(30))
print(str.center(100))
str1 = "pranay pranay pranay"
print(str1.count("pranay"))
str2 = "welcome to the consele !!!"
print(str2.endswith("!!!"))
print(str2.endswith("to",4,10))
print(str2.endswith("to",4,12))
str3 = "hello pranay,your are honest person"
print(str3.find("pr"))
print(str3.find("ihh"))
str4 = "pranay kumar"
# print(str4.index("py"))
str5 = "leetcodetop1!!!"
str6 = "leetcodetop"
print(str5.isalnum())
print(str6.isalnum())
str7="thekingofmassimara"
print(str7.isalpha())
str8="thekingofjungle!!"
print(str8.isalpha())
a1 = "the boy!"
a2= "the bo22y!"
a3= "the Boy!"
print(a1.islower())
print(a2.islower())
print(a3.islower())
b1="hello pranay"
print(b1.isprintable())
b2="hello pranay\n"
print(b2.isprintable())
c1 = "   "
print(c1.isspace())
c2 = "hello    world"
print(c2.isspace())
d1 = "Hello Pranay Kumar"
print(d1.istitle())
d2 = "hello pranay kumar"
print(d2.istitle())
e1 = "python is a interpreted language"
e2 = " hey,python is a interpreted language"
print(e1.startswith("python"))
print(e2.startswith("python"))
f1="pranay"
f2="Pranay"
f3="PRANAY"
print(f1.swapcase())
print(f2.swapcase())
print(f3.swapcase())
g1="hi iam pranay,how are You"
print(g1.title())