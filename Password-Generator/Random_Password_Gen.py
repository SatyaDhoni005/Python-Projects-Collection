import random
import math

#Define Character Sets
alpha="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
special="!@#$%&*|"

#Taking User Input for Password Length
pass_len=int(input("Enter Password Length:"))

#This List will store the characters of the password
password=[]

#Function to generate part the of password from a given character set
def generate_pass(length , array , is_alpha=False):
    for i in range(length):
        index=random.randint(0,len(array)-1)
        character=array[index]
        #If the Array is Alphabetic, then randomly converts to uppercase 
        if is_alpha:
            case=random.randint(0,1)
            if case==1:
                character=character.upper()
        password.append(character)

#Enforces Minimum Password Length
if pass_len < 8:
    print("Password length must be at least 8 characters")
else:

    #Split Password Length using 50-30-20 Rule
    alpha_len=(pass_len//2)                      #50% Alphabets
    num_len=math.ceil(pass_len*30/100)           #30% Numbers
    special_len=pass_len-(alpha_len+num_len)     #Remaining 20% Special characters


    #Generate Each part of the password
    generate_pass(alpha_len,alpha,True)          #Alphabet Password
    generate_pass(num_len,num)                   #Number Password
    generate_pass(special_len,special)           #Special Character Password

    #Shuffle to mix all character of the password randomly
    random.shuffle(password)

    #Join List into String to form the final password
    gen_password=''.join(password)

    #Display the final password
    print(f"Generated Password: {gen_password}")