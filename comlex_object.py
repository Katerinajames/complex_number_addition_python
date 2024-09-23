#https://stackoverflow.com/questions/12486828/python-making-a-class-to-use-complex-numbers
#https://www.geeksforgeeks.org/program-to-add-two-complex-numbers/
#https://www.geeksforgeeks.org/program-to-add-two-complex-numbers/
import cmath



class  Complex:
 def __init__(self,real,img):
	  self.real=real
	  self.img=img
 def add(self ,p,p1):  
      # creating temporary variable 
        temp=Complex(0, 0) 
   
        # adding real part of complex numbers 
        temp.real = p.real + p1.real 
   
        # adding Imaginary part of complex numbers 
        temp.img = p.img + p1.img 
   
        # returning the sum 
        return temp;   
	  

print("------------------------") 

p=Complex(2,3)
p1=Complex(2,3)
c3 = Complex(0, 0)
c3 = c3.add(p, p1);
print("Sum of complex number :", c3.real, "+ i"+ str(c3.img)) 



