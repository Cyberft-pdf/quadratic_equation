import cmath




a = int(input("kvadratický člen: "))

b = int(input("linearní člen: "))

c = int(input("absolutní člen: "))

disk = (b**2) - (4*a*c)


if disk > 0:
    print("Tato kvadratická rovnice nemá řešení")


if disk == 0:
     odpovet = input("Rovnice má 1 řešení, chceš ho znát?:")
     if odpovet == "ano" :
          sol1 = (-b-cmath.sqrt(disk))/(2*a)
          sol2 = (-b+cmath.sqrt(disk))/(2*a)
          
          print(f"dva kořeny jsou {sol1},{sol2}")

#made by cyberft-pdf
