from rembg import remove 
from PIL import Image 

for i in range(1,20):
    input_path =  r'C:\Users\PNP\Desktop\Nappi\Dataset_manuale\train\frame'+str(i)+'.png'
    output_path = r'C:\Users\PNP\Desktop\Nappi\Dataset_manuale\train\frame'+str(i)+'.png' 

    # Processing the image 
    input = Image.open(input_path) 
    
    # Removing the background from the given Image 
    output = remove(input) 
    
    #Saving the image in the given path 
    output.save(output_path)