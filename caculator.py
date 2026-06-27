print("caculator + - / *")
while 1>0:
    number = int(input())
    thing = str(input("(+ - * / end)"))
    numbor = int(input())
    if thing == "+":
        print (number,"+",numbor,"=",number+numbor)
    if thing == "-":
        print (number,"-",numbor,"=",number-numbor)
    if thing == "*":
        print (number,"*",numbor,"=",number*numbor)
    if thing == "/":
        print (number,"/",numbor,"=",number/numbor)
    if thing == "end":
        break