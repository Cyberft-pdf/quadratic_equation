import cmath




a = int(input("quadratic term: "))

b = int(input("linear term: "))

c = int(input("absolute term: "))

disk = (b**2) - (4*a*c)


if disk < 0:
    print("This quadratic equation has no solution")

if disk >0:
    sol1 = (-b-cmath.sqrt(disk))/(2*a)
    sol2 = (-b+cmath.sqrt(disk))/(2*a)

    print(f"result: {sol1},{sol2}")


if disk == 0:
     odpovet = input("The equation has 1 solution, do you want to know it?:")
     if odpovet == "yes":
          sol3 = (-b)/(2*a)
          
          print(f"result: {sol3}")

#made by cyberft-pdf
