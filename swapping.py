def swapFile1():
    data_a=input("Enter the file name")
    
    with open(data_a,'r') as a:
        data1=a.read()
    

    fo=input("Enter the file name")

    with open(fo,'r') as b:
        data2=b.read()
       

    with open(data_a,'w') as a:
        a.write(data2)
   
    with open(fo,'w') as b:    
        b.write(data1)

swapFile1()
       

        