from cryptography.fernet import Fernet

import random






### Generator class


class key_gen_01(object):


    def __init__(self):

        # Init variables
        
        self.x_01 = random.randint(0, 500)
        self.x_02 = 0
        self.a_01 = []
        self.d_01 = {}
        self.TK_01 = 0
        self.TK_02 = 0
        self.TOK_01 = ""



### Runner func

    def func_01(self):

      


        
        # Iterate pseudo-random key generator list 

        for i in range(0, self.x_01):

            self.a_01.append("KEY%d" % i)
            

        # Iterate pseudo-random dict key generator

        for i in range(0, len(self.a_01)):

            self.d_01.update({self.a_01[i]: Fernet.generate_key()})

       # print(self.d_01)

        # Update x_02 to reflect dict len

        self.x_02 = random.randint(0, len(self.d_01))



        # Iterate through dict items and choose a KEY based on psuedo-random number.
            
        for i, item in enumerate(self.d_01, start=0):


            if i == self.x_02:

                self.TK_01 = item
                


        
        #self.TK_02 = Fernet(self.d_01.get(self.TK_01))
      
        #self.TOK_01 = self.TK_02.encrypt(b"Johnson and Johnson")
       
        #print(self.TOK_01)

        




if __name__ == '__main__':

    run = key_gen_01
    run().func_01()
    
                      





    

