import time 
import img2pdf 
from PIL import Image 
import os 
start = time.time()

pdf_path = '/home/ubuntu111000/Desktop/Combined.pdf'
#cwd=raw_input('Enter the dir:')
cwd='/home/ubuntu111000/project'
basedir=cwd


######################################################################################################


def main(): 
	i=1
	var=os.listdir(basedir)
	var.sort()
	print var
	
	for filename in var:
		
		src=basedir+'/'+filename
		dst=basedir+'/'+str(i)+'.jpg'
		os.rename(src,dst)
		i=i+1
		print src,"-->",dst,"\n"
		 

#######################################################################################################

def main2():
	var1=os.listdir(basedir)
	var1.sort()
	myarr=[]
	print var1
	
	for filees in var1:
  
    		varr=cwd+'/'+filees
     		myarr.append(varr)

	pdf_bytes = img2pdf.convert(myarr) 
	file = open(pdf_path, "wb") 
	file.write(pdf_bytes) 
	file.close()
	     	
########################################################################################################
 
    	

main()
main2()
end=time.time()
print('DATA built IN ',end-start,"seconds\n")
print('No erros!!!') 
