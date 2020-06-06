def farenheit(celsius):
    farenheit = ((celsius * 9/5)+32)
    return farenheit

def celsius(farenheit):
    celsius = ((farenheit - 32) * 5/9)
    return celsius

while True:
        print(" 1. For convertion of celsius to farenheit: ")
        print(" 2. For convertion of farenheit to celsius: ")
        ch=int(input("Enter either 1 or 2 :"))

        if ch==1:
         celsius =int(input("Enter the temp in celsius : "))
         print("The degree in farenheit is :",farenheit(celsius))
         print("")

        if ch==2:
                farenheit =float(input("Enter the temp in farenheit: "))
                print("The degree in celsius is :",celsius(farenheit))
                print("")
        elif ch >=3:
         print("invalid input")
