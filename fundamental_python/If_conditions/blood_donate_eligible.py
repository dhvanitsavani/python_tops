age = int(input("Enter age : "))

if age >= 18 and age <= 65:
    weight = int(input("Enter weight : "))
    
    if weight >= 50:
        homoglobin = float(input("Enter homoglobin level : "))
        
        if homoglobin >= 12.5:
            print("eligible")
        else:
            print("not eligible")

    else:
        print("not eligible")
        
else:
    print("not eligible")
            
            
