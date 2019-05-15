import random
#Add from datetime import datetime at the top of the file, so we can work with datetimes to set due dates on borrowed books.

from datetime import datetime
#Create a class called Book.
class Book:
#two class variables: on_shelf and on_loan.
#as empty lists.
    on_shelf = []
    on_loan = []
    on_hold = []

def __init(self, on_shelf, on_loan):


def borrow():

def return_to_library():

def lent_out():

@classmethod
def create():

@classmethod
def current_due_date():
    now = datetime.now()
    # two weeks expressed in seconds  
    two_weeks = 60 * 60 * 24 * 14 
    future_timestamp = now.timestamp() + two_weeks
    return datetime.fromtimestamp(future_timestamp)

@classmethod
def overdue_books():

@classmethod
def browse():








sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0