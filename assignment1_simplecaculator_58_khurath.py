a=float(input("enter a number : "))
b=float(input("enter another number :"))
c=input("enter operation(add,subract,multiply,divide,reminder,exponent,floordivision):")


## ADDITION 
if(c=="add"):
    res_add=a+b
    print(res_add)
    
## SUBRACTION
elif(c=="subract"):
    res_sub=a-b
    print(res_sub)

## MULTIPLICATION
elif(c=="multiply"):
    res_mult=a*b
    print(res_mult)

## DIVISION
elif(c=="divide"):
    res_div=a/b
    print(res_div)

## MODULUS
elif(c=="reminder"):
    res_mod=a%b
    print(res_mod)

## EXPONENT
elif(c=="exponent"):
    res_exp=a**b
    print(res_exp)

## FLOOR DIVISON 
elif(c=="floordivision"):
    res_divv=a//b
    print(res_divv)

else:
    print("please enter valid inputs!!")


