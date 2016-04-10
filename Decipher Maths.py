print("DECIPHER MATHS:\n") #Name of Program

print("Welcome to Decipher Maths!") #Welcome message

print("""\nThe available modules are:\n
 - differentiation
 - integration
 - factorisation
 - expansion
 - polynomial remainder
 - binomial expansion
 - graph transformations\n""") #List of modules

module = str(input("What would you like to do today? (Please enter a module): ")) #Selection of module

while module not in {"differentiation", "integration", "factorisation", "expansion", "polynomial remainder", "binomial expansion", "graph transformations"}:

    print("\n - Invalid input. Please enter a listed module.\n") #Validation of module selection

    module = str(input("What would you like to do today? (Please enter a module): "))


def inputINTEGER(message): #Validation for integer

    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("\n - Invalid input. Please enter an integer.\n")
            continue
        else:
            return userInput
            break

if module == "differentiation": #Differentiation

    print("\nDifferentiation:\n") #Name of Module

    #Below are the terms for 'y' equation

    term1 = inputINTEGER("Please input a coefficient of x^4: ") #x^4 term

    term2 = inputINTEGER("Please input a coefficient of x^3: ") #x^3 term

    term3 = inputINTEGER("Please input a coefficient of x^2: ") #x^2 term

    term4 = inputINTEGER("Please input a coefficient of x: ") #x term

    term5 = inputINTEGER("Please input a '+ c' value: ") #c value

    print("\ny =",term1,"x^4  + ",term2,"x^3  + ",term3,"x^2  + ",term4,"x  + ",term5,"\n") #'y' equation

    print("dy/dx =",4*term1,"x^3  + ",3*term2,"x^2  + ",2*term3,"x  + ",term4) #'dy/dx' equation

if module == "integration": #Integration

    print("\nIntegration:\n") #Name of Module

    #Below are the terms for 'y' equation

    term1 = inputINTEGER("Please input a coefficient of x^4: ") #x^4 term

    term2 = inputINTEGER("Please input a coefficient of x^3: ") #x^3 term

    term3 = inputINTEGER("Please input a coefficient of x^2: ") #x^2 term

    term4 = inputINTEGER("Please input a coefficient of x: ") #x term

    term5 = inputINTEGER("Please input a '+ c' value: ") #c value

    print("\ny =",term1,"x^4  + ",term2,"x^3  + ",term3,"x^2  + ",term4,"x  + ",term5,"\n") #'y' equation

    print("S(",term1,"x^4  + ",term2,"x^3  + ",term3,"x^2  + ",term4,"x  + ",term5,")") #Equation to be integrated

    #Below I have created new variables for the integral terms, rounded to 3 s.f.

    iTerm1 = "%.3g"%(term1/5) #x^4 term

    iTerm2 = "%.3g"%(term2/4) #x^3 term

    iTerm3 = "%.3g"%(term3/3) #x^2 term

    iTerm4 = "%.3g"%(term4/2) #x term

    iTerm5 = "%.3g"%(term5) #c value

    print("\n=",iTerm1,"x^5  + ",iTerm2,"x^4  + ",iTerm3,"x^3  + ",iTerm4,"x^2  + ",iTerm5,"x  + c") #Integrated equation

if module == "factorisation": #Factorisation

    print("\nFactorisation:\n") #Name of Module

    #Below are the terms for 'y' equation

    term1 = inputINTEGER("Please input a coefficient of x^2: ") #x^2 term

    term2 = inputINTEGER("Please input a coefficient of x: ") #x term

    term3 = inputINTEGER("Please input a '+ c' value: ") #c value

    print("\ny =",term1,"x^2  + ",term2,"x  + ",term3,"\n") #'y' equation

    Disc = (term2**2)-(4*term1*term3) #Discriminant of 'y' equation

    if Disc < 0: #Discriminant < 0

        print("The quadratic equation that you entered has no real solutions and hence no rational factors.\n")

    elif Disc == 0: #Discriminant = 0

        x = (-term2)/(2*term1) #'x' value

        u = (-x)

        print("y = ( x +","%.3g"%(u),") ( x +","%.3g"%(u),")") #Factors of 'y' equation

        print("\nx =","%.3g"%(x)) #Solution

    else: #Discriminant > 0

        x1 = ((-term2)+(Disc**0.5))/(2*term1) #First 'x' value

        x2 = ((-term2)-(Disc**0.5))/(2*term1) #Second 'x' value

        u1 = (-x1)

        u2 = (-x2)

        print("y = ( x +","%.3g"%(u1),") ( x +","%.3g"%(u2),")") #Factors of 'y' equation

        print("\nx =","%.3g"%(x1),"OR x =","%.3g"%(x2)) #Solutions

if module == "expansion": #Expansion

    print("\nExpansion:\n") #Name of Module

    cf1 = inputINTEGER("For the first bracket, please input a coefficient of x: ") #Coefficient in first bracket

    u1 = inputINTEGER("Please input a value to be added/subracted to the x term, in the first bracket: ") #Value added in first bracket

    cf2 = inputINTEGER("For the second bracket, please input a coefficient of x: ") #Coefficient in second bracket

    u2 = inputINTEGER("Please input a value to be added/subracted to the x term, in the second bracket: ") #Value added in second bracket

    print("\ny = (",cf1,"x +",u1,")(",cf2,"x +",u2,")") #'y' expressed as factors

    print("\ny = ",(cf1*cf2),"x^2 +",((u1*cf2)+(u2*cf1)),"x +",(u1*u2)) #Expanded 'y' equation

if module == "polynomial remainder": #Polynomials; Calculation of Remainder

    print("\nPolynomials; Calculation of Remainder:\n") #Name of Module

    #Below are the terms for 'p(x)' equation

    term1 = inputINTEGER("Please input a coefficient of x^4: ") #x^4 term

    term2 = inputINTEGER("Please input a coefficient of x^3: ") #x^3 term

    term3 = inputINTEGER("Please input a coefficient of x^2: ") #x^2 term

    term4 = inputINTEGER("Please input a coefficient of x: ") #x term

    term5 = inputINTEGER("Please input a '+ c' value: ") #c value

    print("\np(x) =",term1,"x^4  + ",term2,"x^3  + ",term3,"x^2  + ",term4,"x  + ",term5,"\n") #'p(x)' equation

    x = float(input("Please input a value of x: ")) #'x' value

    px = (term1*(x**4) + term2*(x**3) + term3*(x**2) + term4*(x) + term5) #'p(x)' value

    print("\nx =", x, "\n") #Output of 'x' value

    print("p(",x,") =", px) #Output of 'p(x)' value

if module == "binomial expansion": #Binomial Expansion

    print("\nBinomial Expansion:\n") #Name of Module

    def factorial(x): #Factorial function
        assert x >= 0
        if x == 0:
            return 1
        return x*factorial(x-1)

    def b(n, k): #Binomial coefficient function
        return int(factorial(n)/(factorial(k)*factorial(n-k)))

    cf = inputINTEGER("Please input a coefficient of x: ") #Coefficent of 'x'

    u = inputINTEGER("Please input a value to be added/subracted to the x term: ") #Value added to 'x' term

    n = inputINTEGER("Please input an index number (power) for the expansion: ") #Bracket power

    print("\ny = (",cf,"x +",u,") ^",n,"\n") #Binomial to be expanded

    if n == 0: #Expansion where n is 0

        print("y =",1)

    if n == 1: #Expansion where n is 1

        print("y =",(cf**n),"x +",u**n)

    if n == 2: #Expansion where n is 2

        print("y =",(cf**n),"x ^",n,"+",b(n, 1)*u*(cf**(n-1)),"x +",u**n)

    if n == 3: #Expansion where n is 3

        print("y =",(cf**n),"x ^",n,"+",b(n, 1)*u*(cf**(n-1)),"x ^",n-1,"+",b(n, 2)*(u**2)*(cf**(n-2)),"x +",u**n)

    if n == 4: #Expansion where n is 4

        print("y =",(cf**n),"x ^",n,"+",b(n, 1)*u*(cf**(n-1)),"x ^",n-1,"+",b(n, 2)*(u**2)*(cf**(n-2)),"x ^",n-2,"+",b(n, 3)*(u**3)*(cf**(n-3)),"x +",u**n)

    if n == 5: #Expansion where n is 5

        print("y =",(cf**n),"x ^",n,"+",b(n, 1)*u*(cf**(n-1)),"x ^",n-1,"+",b(n, 2)*(u**2)*(cf**(n-2)),"x ^",n-2,"+",b(n, 3)*(u**3)*(cf**(n-3)),"x ^",n-3,"+",b(n, 4)*(u**4)*(cf**(n-4)),"x +",u**n)

    if n == -1: #Expansion where n is -1

        print("y = 1 / (",cf**(-n),"x +",u**(-n),")",)

    if n == -2: #Expansion where n is -2

        print("y = 1 / (",cf**(-n),"x ^",(-n),"+",b(-n, 1)*u*(cf**((-n)-1)),"x +",u**(-n),")",)
        
    if n == -3: #Expansion where n is -3

        print("y = 1 / (",cf**(-n),"x ^",(-n),"+",b(-n, 1)*u*(cf**((-n)-1)),"x ^",(-n)-1,"+",b(-n, 2)*(u**2)*(cf**((-n)-2)),"x +",u**(-n),")",)

    if n == -4: #Expansion where n is -4

        print("y = 1 / (",cf**(-n),"x ^",(-n),"+",b(-n, 1)*u*(cf**((-n)-1)),"x ^",(-n)-1,"+",b(-n, 2)*(u**2)*(cf**((-n)-2)),"x ^",(-n)-2,"+",b(-n, 3)*(u**3)*(cf**((-n)-3)),"x +",u**(-n),")",)

    if n == -5: #Expansion where n is -5

        print("y = 1 / (",cf**(-n),"x ^",(-n),"+",b(-n, 1)*u*(cf**((-n)-1)),"x ^",(-n)-1,"+",b(-n, 2)*(u**2)*(cf**((-n)-2)),"x ^",(-n)-2,"+",b(-n, 3)*(u**3)*(cf**((-n)-3)),"x ^",(-n)-3,"+",b(-n, 4)*(u**4)*(cf**((-n)-4)),"x +",u**(-n),")",)


        
if module == "graph transformations": #Graph Transformations

    print("\nGraph Transformations:\n") #Name of Module

    print("The input MUST be in the form y = ( x + a )^2 + b.\n") #Input notice

    #Below are the terms that form the 'y' equation

    cf = inputINTEGER("Please input a coefficient of x: ") #Coefficient of 'x'

    a = inputINTEGER("Please input a value to be added/subracted to the x term: ") #Value added to the 'x' term

    b = inputINTEGER("Please input a '+ c' value: ") #c value

    print("\ny = (",cf,"x +",a,")^2 +",b) #'y' equation

    t = str(input("\nPlease input the type of transformation that you would like to occur (stretch, reflection or translation): ")) #Type of transformation

    if t == "stretch": #Stretch transformation

        u = inputINTEGER("\nPlease input a value by which the equation will be stretched: ") #Value for stretch

        d = str(input("\nPlease input the direction of the stretch (x OR y): ")) #Direction of stretch

        if d == "x": #x direction

            print("\ny is STRETCHED, IN X DIRECTION, BY S.F.",u)

            print("\ny = (","%.3g"%((1/u)*cf),"x +",a,")^2 +",b)

        if d == "y": #y direction

            print("\ny is STRETCHED, IN Y DIRECTION, BY S.F.",u)

            print("\ny =",u,"(",cf,"x +",a,")^2 +",(b*u))

    if t == "reflection": #Reflection transformation

        d = str(input("\nPlease input the axis that y is reflected in (x OR y): ")) #Axis of reflection

        if d == "x": #x axis

            print("\ny is REFLECTED, IN THE X AXIS")

            print("\ny = - (",cf,"x +",a,")^2 +",(-b))

        if d == "y": #y axis

            print("\ny is REFLECTED, IN THE Y AXIS")

            print("\ny = (",(-cf),"x +",a,")^2 +",b)


    if t == "translation": #Translation transformation

        u = inputINTEGER("\nPlease input a value by which the equation will be horizontally translated: ") #Value of horizontal translation

        v = inputINTEGER("Please input a value by which the equation will be vertically translated: ") #Value of vertical translation

        i = (u/cf) #Horizontal translation

        j = v #Vertical translation

        print("\ny is TRANSLATED BY (",u,"i +",v,"j )") #Translation

        print("\ny = (",cf,"x +","%.3g"%(a-i),")^2 +",(b+j))

print("\nThank you for using Decipher Maths!")
