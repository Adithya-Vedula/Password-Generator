import eel
import random
import string  
from os import chdir
eel.init("web")  
  
# Exposing the random_python function to javascript
@eel.expose    
def generate(length):
    length = length
    if length == '':
        data = 'Enter a number then click the button'
        return data
    small_letters = string.ascii_lowercase
    # Defining a list with all uppercase letters
    big_letters = string.ascii_uppercase  
    nums = [0,1,2,3,4,5,6,7,8,9]
    special_chars = list(string.punctuation)
    all_chars = list(small_letters) + list(big_letters) + list(nums) + list(special_chars)
    """This method is called when the button is clicked"""

    if int(length) <= 0:
        # Print some statements
        data = 'Length of password cannot be zero or less than 0' 
        return data       
#     This is a for loop which goes in length of password 
    password = []
    for i in range(int(length)):
       value = random.choice(all_chars)
       password.append(str(value)) 
      
    new_password = "".join(password)
    # Prints the passwords
    data = 'Password is: '  + str(new_password)
    if int(length) >= 10:
        chdir('output')
        file = open('pwd.txt' , 'w')
        file.write(data)
        data = 'Since Password is greater than or equal to 10 characters,it has been written in a file called "pwd.txt".'
        return data
    else:
        return data            

# Start the index.html file
eel.start("index.html" , port=8000 , mode = 'chrome')