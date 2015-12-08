
rainfile = open("rainfall.txt","r")
outfile = open("rainfallInCM.txt","w")

for aline in rainfile:
    values = aline.split()

    inches = float(values[1])
    cm = 2.54 * inches

    outfile.write(values[0]+" "+str(cm)+"\n")  

rainfile.close()
outfile.close()
