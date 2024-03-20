# comments have the pound symbol to the left of them to show that anything after the symbol can be ignored

# below are the three data types we have used, String, Boolean, Integers
# these data types cannot be used together in opperations which are "> + < -"
# variables hold data variable = data
# Integer is a number
jasons_age = 28 # pound symbols can be used after code whithout breaking the code
drinking_age = 21
handgun_buying_age = drinking_age # variables can be assigned other variables, in this case 21 is assigned to this variable

# String are text or numbers surrounded in quotation marks
jason_first_name = "Jason"
jason_middle_name = "Forress"
jason_last_name = "Rodgers"
6
jason_full_name = jason_first_name + jason_middle_name + jason_last_name #strings can be added together

# booleans are True and False, you can use opperations to create boolean variables
jason_should_drink = False
is_jason_of_age = drinking_age < jasons_age # This would be the boolean True because drinking age is less than jasons age


# this is an "if else" statement. This is used to execute code if the "if" resolves to true, and other code if it is false
if jasons_age > drinking_age: # this is the same as saying "if True:" since jason age is greater than drinking age
    print("") # im going to print nothing here because i dont want to clutter the terminal feel free to add something
else:
    print("") # im going to print nothing here because i dont want to clutter the terminal feel free to add something


# stuff i didnt get into... 
# in the if else statement you can execute any amount of code, here is an example using the other if statement as a base
    
if jasons_age > drinking_age: 
    print("jason can drink")
    print("but he really shouldn't")
else:
    print("jason cannot drink but shouldnt drink anyways")
    print("also you can add a line here too")

# some extra stuff that would be cool if you could understand just from this but totally above what we have gone over:
# "And" you can use and if statment that checks if two things are true by typing and
    
if jasons_age > drinking_age and jason_should_drink: # jason should drink is False and jason is greater than drinking age so that is true however "True and False = False"
    print("jason drinks")
else:
    print("jason does not drink because jason should drink is false even though his age is above the drinking age")

# just like how True and False is False.... True OR False is True.
# here is an example of that
    
jason_is_drinking = jasons_age > drinking_age and jason_should_drink # this is going to be false because True + False = False
jason_buys_handguns = jasons_age > handgun_buying_age # this is True
    
if jason_is_drinking or jason_buys_handguns: # jason should drink is False and jason is greater than drinking age so that is true however "True and False = False"
    print("Jason is 21 because jason is buying handguns. Even though jason is not drinking only one of the two has to be true")
else:
    print("this will only show up if both things are 'False'")  
    














