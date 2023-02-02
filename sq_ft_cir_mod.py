
def calculator():
    option = int(input("Press 1 if you wish to measure the square footage of a room. \nPress 2 to measure the circumference of a circle: "))
    if option == 1:
        leng = input("enter length: ")
        wid = input("enter width: ")
        sq_ft = int(leng) * int(wid)
        print("Total Square feet is: ")
        print(sq_ft)
        
    if option == 2:
        dia = input("enter diameter: ")
        cir = int(dia) * 3.14
        print("Circumference is "  )
        print(cir)
