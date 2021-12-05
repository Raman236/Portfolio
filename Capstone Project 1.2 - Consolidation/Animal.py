# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 23:10:37 2021

Dear Kirsten

Thank you so much for all the encouragement!!!! Especially
after task 16. That was one of the hardest tasks, which has not been reviewed
yet. I sent that in on Thursday, 2nd September and still waiting for a response.

I know that is a Very long program, and I was so lost! (Also recovering from COVID-19)
and didint want to fall behind so, tried to do as much as I could. I know I
I did terrible there but waiting for feedback so I can amend.

Your encouragement has definately boosted my morale and so after 11pm I am
still working on this program!!

I took your advice and tried to make the proper amendments

I dont know if you are on discord, so not sure how to send you a message

Thank you again for all the assistance and encouragement!!!!!

@author: Raman Sewjugath
"""
#==========================#
# Animal Class
#==========================#
class Animal(object):
    
    '''
    Animal Class
    '''
    def __init__(self, num_teeth, spots, weight):
        self.num_teeth = num_teeth
        self.spots = spots
        self.weight = weight
        
    def is_animal(self):
        print(self.__str__())
    
    def __str__(self):
        return ("This is an Animal Classification")

#==========================#
# LION Class
#==========================#        
class Lion(Animal):
    '''
    Lion Sub Class which inherits some attributes from the Animal Class
    '''
    def __init__(self, num_teeth, spots, weight, long_body, large_head, short_legs):
        super().__init__(num_teeth, spots, weight)
        self.long_body = long_body
        self.large_head = large_head
        self.short_legs = short_legs
        self.lion = False
        self.lion_result = ""
    
        '''
        is_lion() method checks if the animal is a lion based on body length,
        head size, leg length, returns a boolean value
        '''
    def is_lion(self):
        if (self.spots == False) and (self.long_body == True) and (self.large_head == True) and (self.short_legs == True):            
            return True
        else:
            return False
    
    '''
    lion_type() method fist checks if the Animal is a lion
    then checks what type of lion, male, female or cub
    '''
    def lion_type(self):
                
        if self.is_lion() == True:
            
            # checks if male lion
            if self.weight > 120:
                self.lion_result = "Male Lion"
                print(self.__str__())
                
            # checks if female lion
            elif (80 < self.weight < 120):
                self.lion_result = "Lioness"
                print(self.__str__())
            
            # Must be a cub
            else:
                self.lion_result = "Lion CUB"
                print(self.__str__())
        
        # if is_lion() returns False, this statement is initialized
        else:
            print("- This Animal is NOT a Lion")

    # string method, formats output
    def __str__(self):
        return (f"- This Animal has no spots, {self.num_teeth} teeth," +
                f" weighs {self.weight} Kg, and is a {self.lion_result} type")              
  
        
#==========================#
# Cheetah Class
#==========================#
class Cheetah(Animal):
    
    '''
    Cheetah Class
    '''
    
    def __init__(self, num_teeth, spots, weight, max_speed):
        super().__init__(num_teeth, spots, weight)
        self.max_speed = max_speed
        self.cheetah_attributes = ["Male", "Female", "Cub", "has spots"]
        self.spots_char = ""
        self.cheetah_result = ""
                
    
    # Check if the animal added is a cheetah
    def is_cheetah(self):
        if (self.spots == True):            
            return True
        else:
            return False
    
    # checks the type of cheetah, if the Animal is a cheetah
    def cheetah_type(self):
        
        # Facts from: https://www.krugerpark.co.za/africa_cheetah.html
        if self.is_cheetah() == True:
            
            self.spots_char = self.cheetah_attributes[3]
            
            if (49 < self.weight < 70):
                self.cheetah_result = self.cheetah_attributes[0]
                print(self.__str__())
                
            elif(35 < self.weight < 48):
                self.cheetah_result = self.cheetah_attributes[1]
                print(self.__str__())
            
            else:
                self.cheetah_result = self.cheetah_attributes[2]
                print(self.__str__())        
       
        else:
            print("+ This Animal is Not a Cheetah")

                
    # string method formats output
    def __str__(self):
        return (f"+ This Animal {self.spots_char}, weighs {self.weight} Kg, and" 
                f" is a {self.cheetah_result} reaching speeds of {self.max_speed} km/h")

#=========================================================================#
# Arguments:
#=========================================================================#
# Create the Lion objects within the Animal class and pass
# values to the Lion Class
# num_teeth, spots, weight, long_body, large_head, short_legs
a1 = Lion(30, False, 135, True, True, True) # Male lion
a2 = Lion(24, False, 55, True, True, True)  # Cub
a3 = Lion(29, False, 95, True, True, True)  # Female lion (Lioness)

# Calls the Lion_type method in the Lion class to check
# 1. What type animal it is
# 2. To check what type lion it is
print("LION TYPES:")
a1.lion_type()
a2.lion_type()
a3.lion_type()

print("\nCHEETAH")

# Cheetah object (teeth, spots, weight, max speed)
c1 = Cheetah(30, True, 68, 120)
c2 = Cheetah(30, True, 47, 119)
c3 = Cheetah(30, True, 2, 10)

# Calls the cheetah_type method in the Lion class to check
# 1. What type animal it is
# 2. To check what type cheetah it is
c1.cheetah_type()
c2.cheetah_type()
c3.cheetah_type()










