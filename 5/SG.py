#for n in range(1111111110,1111111140):
#    binN = bin(n)[2:]
#    binost = bin(n % 3)[2:].zfill(2)
#    binN = binN+binost
#    tenN = int(binN,2)
#    binost2 = bin(tenN % 5)[2:].zfill(3)
#    binN = binN+binost2
#    print(n,int(binN,2),int(binN,2)//n)
n1 = 1111111110 / 32
n2 = 1444444416 / 32
print(n2-n1)