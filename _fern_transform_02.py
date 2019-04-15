import fern_transform_01
from cryptography.fernet import Fernet
import random
import base64
import sys
#import secrets


##
# By: Kody Dibble
# Use: Takes normal Fernet keys in random amount, chooses 1 and performs
#       changes to it at a BIT level.
#

#   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
  #  the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.

## Notes:


## Function names use a self.u_counter that addresses when the functions were created in memory 
## Use in conjunction with fern_transform_01
## obfuscate class

class obf_01:


    global c
    global u_key
    global u_crypto_dict
    c = fern_transform_01.key_gen_01()
    u_key = c.TK_01
    u_crypto_dict = c.d_01
    c.func_01()
    
    # Init variables

    

    def __init__(self):

        # inits from other .py files

        
        # inits for strings
        #self.c = fern_transform_01.key_gen_01()
        self.u_key = c.TK_01
        self.u_crypto_dict = c.d_01
        self.u_crypto_digest = " "
        self.u_crypto_fern = " "
        self.r_fern = ""
        self.e = ""
        self.u_string = ""
        self.new_string = ""

        # inits for lists
        
        self.u_list = []
        self.u_list_bin = []
        self.u_list_bin_02 = []
        self.u_list_bin_03 = []
        self.u_list_bin_04 = []
        self.stack = []
        self.final_int_list_bin = []
        self.final_char_list_bin = []
        self.final_bin = []
        self.u_check_list = []
        self.new_list = []
        
        # inits for ints
        
        self.u_count = 0
        self.u_count_01 = 0
        self.x = 0
        self.y = 0
        
        # This isn't right...but works.
        self.u_pattern = [3, 6, 9, 'a']
        #self.c.func_01()

      
    # Grab key and associated value

        
    def func_02(self):
       
        # You can do this way easier but it works for now...
        for i in self.u_crypto_dict:

            if self.u_key == i:

                 # Possible error...I can't seem to use the self.crypto_digest to get a value
            
                self.u_crypto_digest = c.d_01.get(i)


                
                self.u_list = list(self.u_crypto_digest)
                self.u_list.reverse()
         
        
     # func_03 goes through list and takes out each based on rand_item
         # then switch that list to binary list and reverse that list
            #
    def func_03(self):


        # Grab a number..either 3, 6, or 9.
        rand_item = self.u_pattern[random.randrange(0, len(self.u_pattern)-1)]


       # Use the u_list to grab every nth term 
        self.u_list_bin = self.u_list[0::rand_item]

        # Switch those terms to binary
    
        for i in self.u_list_bin:

            self.u_list_bin_02.append(bin(i))

        
        self.u_counter = rand_item

        # reverse binary 
        for i in self.u_list_bin_02:

            s = "".join(reversed(i))
            self.u_list_bin_03.append(s)

       
        # drop the binary prefiself.x
        for i in self.u_list_bin_03:

             self.u_list_bin_04.append(i[:-3])


        # return back to ints base 2
        for i in self.u_list_bin_04:

            self.u_counter+=rand_item
            self.u_list.insert(int(i, 2), self.u_counter)


        
       
        return self.u_list
        
    def func_04(self):


        # grab instance of func_03 return
        self.final_int_list_bin = self.func_03()

        # go through range of 32...For some reason these first 32 asciis are not useful for this
        for i in self.final_int_list_bin:
            
                if i not in range(0, 32):

                     # turn the ascii numbers into chrs
                     self.final_char_list_bin.append(chr(i))




        # join the list above
        
        self.u_string = self.u_string.join(self.final_char_list_bin)

        
        # encode your string into utf-8, then encode in base64 urlsafe
        self.u_string = base64.urlsafe_b64encode(self.u_string.encode('UTF-8'))
        

     
        # get size of bytes of encoded string 
        self.x = sys.getsizeof(self.u_string)

       
        # re-create the encoded new string that has been modified as byte list (again)      
        for i in self.u_string:

            
            self.u_count += 1
            self.u_check_list.append(bin(i))

          # string can only be 32 bytes correct here
          
        self.y = self.u_count - 32
      
        check = []

        
         # pop the excess from the list
        for i in range(0, self.y):

            self.u_check_list.pop()


      
   

        # change from binary all the way to chr
        for i in self.u_check_list:

            
            self.new_list.append(chr(int(i, 2)))


        # join list & re-encode the string (???)
        self.new_string = ''.join(self.new_list)
        self.new_string = base64.urlsafe_b64encode(self.new_string.encode('UTF-8'))

        
        # create fernet object
        try:
            
            self.r_fern= ""
            self.r_fern = Fernet(bytes(self.new_string))
        except:
            #self.func_07()
            pass
        
      
    # This is the function that actually takes a string and encrypts it
    def func_05(self, string):

        # encrypt fernet style
        self.e = self.r_fern.encrypt(string)
        return self.e
        #print(self.r_fern.decrypt(self.e).decode("utf-8"))
    
    
    
    def func_06(self, string):
        
        return self.r_fern.decrypt(self.e).decode("utf-8")
    
    def func_08(self):
        
        return self.new_string
    
    
    
    #back up runner
    #def main(self):



     #   self.func_02()
      #  self.func_04()
        #self.func_04()
        
        #run_a.func_03()
        #run_a.func_04()
      
        #self.run_a.func_05(string)
        #self.run_a.func_04()
        #print(run_a.new_string)
       # print(self.func_08())
        


if __name__ == '__main__':

        #global string
       # string = str(input('Enter info: '))
        #string = bytes(string.encode("utf-8"))
         c = fern_transform_01.key_gen_01()
         c.func_01()
        
        
        
         run_a = obf_01()
         
         run_a.func_02()
        # run_a.func_03()
         run_a.func_04()
      #  print(run_a.new_string)
         print(run_a.func_08())
      
        #r = run_a.func_05(string)
        
        #print(run_a.func_06(r))

    