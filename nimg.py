import time 
import img2pdf 
from PIL import Image 
import os 





start = time.time()


basedir='/home/ubuntu111000/project'

print " "


 

bake=raw_input("Enter 'PDF' if you want to make pdf or 'REN' for just renaming: ")

if bake == 'PDF':
	namevar=raw_input("Name for output file: ")
	pdf_path = '/home/ubuntu111000/'+namevar+'.pdf'

######################################################################################################


def main():
	
	if bake=='PDF':
		i=1
	else:
		i=input("Enter The starting digit: ")
	
	var=os.listdir(basedir)
	var.sort(key=lambda f: int(filter(str.isdigit, f)))
	
	
	
	for filename in var:

		
		
		src=basedir+'/'+filename
		dst=basedir+'/'+str(i)+'.jpg'
		os.rename(src,dst)
		i=i+1
	
		
		
		print src,"-->",dst,"\n"
			 

#######################################################################################################

def main2():
	var1=os.listdir(basedir)
	var1.sort(key=lambda f: int(filter(str.isdigit, f)))
	print var1	
	
	myarr=[]
	
		
	for filees in var1:
  			
    		varr=basedir+'/'+filees
     		myarr.append(varr)

	pdf_bytes = img2pdf.convert(myarr) 
	file = open(pdf_path, "wb") 
	file.write(pdf_bytes) 
	file.close()
	

########################################################################################################
 
    	

main()
if bake=='PDF':
	main2()

end=time.time()
print('DATA built IN ',end-start,"seconds\n")
print('No erros!!!') 
