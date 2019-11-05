def namecount():
    dicti = {}
    name = str(input("enter name: "))
    while name != "q":
        dicti[name] = dicti.get(name, 0) + 1
        name = str(input("enter name: "))
    for key, val in dicti.items():
        print(str(val) + " students named " + str(key))

    
namecount()
