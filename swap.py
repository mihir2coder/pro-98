def swap():
    file1=input("ENTER YOUR FILE THAT YOU WANT TO TRANSFER-\n")
    file2=input("ENTER THE FILES DESTINATION-\n")

    with open (file1,"r") as a:
        data_a=a.read()

    with open(file2,"w") as b:
        b.write(data_a)

    with open(file2,"r") as b:
        data_b=b.read()
    
    with open(file1,"w") as a:
        a.write(data_b)
        
swap()


