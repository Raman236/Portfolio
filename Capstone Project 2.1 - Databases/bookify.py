# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:00:53 2021

I used this reference to see how to create the table if it doesnt exist
and pass if it does.
REF: https://www.sqlitetutorial.net/sqlite-python/create-tables/

@author: Raman Sewjugath
"""
# import the SQL module
import sqlite3

# connect to or create the database file
db = sqlite3.connect('ebookstore')

# add cursor object to execute sql statements
cursor = db.cursor()


#--------------------------------------#
#    Create the Database and table
#--------------------------------------#

# Variable to hold the create table argument
create_table = '''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    Title TEXT,
                    Author TEXT,
                    Qty INTEGER)'''

# create the table if it does not already exist
cursor.execute(create_table)

# commit changes to teh database
db.commit()



#-----------------------------#
#   BOOKSTORE CLASS
#-----------------------------#

class Bookstore(object):
    
    '''
    Bookstore Class
    '''
    
    # class contsructor
    def __init__(self):
        pass
    
    
    #-----------------------------#
    #   METHOD: ADD BOOKS
    #-----------------------------#
    def add_book(self, b_id, b_title, b_author, b_qty):
        
        '''
        METHOD TO ADD BOOKS TO THE DATABASE
        '''
        # add sql argument to variable
        add_the_book = '''INSERT INTO books (id, Title, Author, Qty)
                        VALUES(?,?,?,?)'''
        
        # execute sql statement
        cursor.execute(add_the_book, (b_id, b_title, b_author, b_qty))
        
        # Save to database
        db.commit()
        
        # Print confirmation
        print("----Book added Successfully----")
        
        # Display the books in the database
        self.display_books()
        
        
        
        
    #-----------------------------#
    #   METHOD: UPDATE BOOKS
    #-----------------------------#
    def update_book(self):        
        
        # Variable to hold the menu string      
        menu = '''\n--SELECT OPTION--\n1. Update Title\n2. Update Author\n3. Update Quantity\n4. Update All\n0. back'''
        print(menu)   
        
        
        # Declare to allow assigning the input to a variable inside the loop
        # the value being assigned won't matter (as long as its greater than 0)
        # since request for an input from the user is made at the start of the loop
        option = 1      
        
        '''
        loop to allow user to go through each option
        '''
        while option != 0:
            
            # user option to select what the ywould like to do
            option = int(input("--UPDATE BOOK--\nEnter Choice: "))
            
            
            '''
            statements to control menu flow
            '''            
            # check if user wants to go back
            if option == 0:
                pass
            
            else:
                
                # request ID of the book which will be updated
                request_id = input("Enter Book ID: ")
                
                # check if the input value is not larger than the options available
                if option > 4:
                    print("*****Invalid Choice****")
                    option = int(input("Enter Choice: "))
                    
                    
                # OPTION 1: Update Title    
                elif option == 1:
                    
                    new_title = input("NEW Title: ")           
                    
                    '''
                    Used an array to pass the arguments through because the execute
                    funtion iterates through characters in text. example if I passed
                    3001 as the id, it will take it as 4 arguments instead of one
                    which is not an issue since wrapping it around square brackets 
                    solved that, however passing 2 or mroe arguments was problematic
                    and the solution was to put them in an array
                    REF: https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
                    '''
                    sql_args = [new_title, request_id]
                    
                    # execute SQL statements via cursor object
                    cursor.execute('''UPDATE books SET Title=? WHERE id=?''', sql_args)
                    
                
                # OPTION 2: Update Author  
                elif option == 2:
                    new_author = input("NEW Author: ")
                    row_update = '''UPDATE books SET Author = ? WHERE id = ?'''
                    
                    sql_args = [new_author, request_id]
                    cursor.execute(row_update, sql_args) 
                    
                    
                # OPTION 3: Update Quantity  
                elif option == 3:
                    new_qty = input("NEW Quantity: ")
                    row_update = '''UPDATE books SET Qty = ? WHERE id = ?'''
                    
                    sql_args = [new_qty, request_id]
                    cursor.execute(row_update, sql_args)
                    
                    
                # OPTION 4: Update All Fields except id  
                elif option == 4:
                    
                    new_title = input("NEW Title: ")
                    new_author = input("NEW Author: ")
                    new_qty = input("NEW Quantity: ")
                    row_update = '''UPDATE books SET Title = ?, Author = ?, Qty = ? WHERE id = ?'''
                    
                    sql_args = [new_title, new_author, new_qty, request_id]
                    cursor.execute(row_update, sql_args)
                
                else:
                    pass
                
                '''
                save changes to the databse and display the row
                '''            
                # save database
                db.commit()
                
                # method called to display the row that was updated
                print("\n=UPDATED SUCCESSFULLY=")
                self.display_row(request_id)
                
                # display the menu again so the user can decide what to do next
                print("\n" + menu)
                
            
            
                  
            
           
            
    #-----------------------------#
    #   METHOD: DELETE BOOKS
    #-----------------------------#
    def del_book(self):
        
        request_id = input("Enter Book ID: ")
        
        # deletes the row based on id
        del_book_row = '''DELETE FROM books WHERE id = ?'''
        cursor.execute(del_book_row, [request_id])
        
        # save changes to teh database
        db.commit()
    
    
    
    #-----------------------------#
    #   METHOD: SEARCH FOR BOOKS
    #-----------------------------#
    def search_books(self):
        
        '''
        I had to do some research on how to use the LIKE clause in Pyhton
        Not as straight forward as I thought.
        # REF: https://www.plus2net.com/python/sqlite-like.php
        '''
        
        search_term_in = input("Search: ")
        
        # In order for the % symbols to be passed as string and not as part of the
        # variable "search_term_in" I had to present it like this:
        search_term = (f'%{search_term_in}%',)     
        
        sql_statement = '''SELECT * FROM books WHERE Title LIKE ? '''        
        cursor.execute(sql_statement, search_term)
        
        print("\nRESULTS:")
        for a_row in cursor:
            print("{} : {} : {} : {}".format(a_row[0], a_row[1], a_row[2], a_row[3]))
    
    
    #----------------------------------#
    #   METHOD: DISPLAY A SINGLE ROW
    #----------------------------------#
    
        '''
        METHOD TO DISPLAY A SINGLE ROW
        '''
        
    def display_row(self, request_id):
        
        row = '''SELECT * FROM books WHERE id = ?'''                
        cursor.execute(row, [request_id])
        
        for a_row in cursor:
            print("{} : {} : {} : {}".format(a_row[0], a_row[1], a_row[2], a_row[3]))
        
    
    #-------------------------------#
    #   METHOD: DISPLAY ALL BOOKS
    #-------------------------------#
    def display_books(self):
        '''
        METHOD TO DISPLAY ALL BOOKS IN THE DATABASE
        '''
        
        print("\n===LIBRARY===")
        
        sql_statement = '''SELECT * FROM books'''
        cursor.execute(sql_statement)
        
        # print out each row to console
        for row in cursor:
            print('{0} : {1} BY {2} : In Stock - {3}'.format(row[0], row[1], row[2], row[3]))
        



#========================= ARGUMENTS BELOW =========================#


'''
Create book objects and Initialize the constructor
'''
book = Bookstore()

#-----------------------------#
#       Create the Menu
#-----------------------------#

welcome = '''\n===================
Welcome to Bookify
===================
'''

menu = '''1. Add Book
2. Update Book
3. Delete Book
4. Search Books
5. display library
6. redisplay menu
0. Exit
'''

print(welcome + menu)



#--------------------------------------#
#       Create the logical loop
#--------------------------------------#

ext = ''

while ext != 'Exit':
    
    # accepts the users choice in a variable
    option = int(input("----Main Menu----\nEnter Choice: "))
    
    # checks if the option selected is within range
    if option > 7:
        print("*****Invalid Choice****")
        option = int(input("Enter Choice: "))
        
        
    # OPTION 1: Calls the add_book() function so user can add a book
    elif option == 1:
        b_id = input("Book ID: ")
        b_title = input("Title: ")
        b_author = input("Author: ")
        b_qty = int(input("Quantity: "))
        
        book.add_book(b_id, b_title, b_author, b_qty)
        
    
    # OPTION 2: Update Book
    elif option == 2:
        book.update_book()
        
    # OPTION 3: Delete book
    elif option == 3:
        book.del_book()
        
    # OPTION 4: call search book function
    elif option == 4:
        book.search_books()
        
    # OPTION 5: display all books
    elif option == 5:
        book.display_books()
        
    # OPTION 6: display menu again
    elif option == 6:
        print(welcome + menu)
    
    # exit the program
    else:
        ext = 'Exit'




# save the database (as a precautionary measure)
db.commit()

# close the database
db.close()