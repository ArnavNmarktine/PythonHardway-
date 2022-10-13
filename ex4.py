car =100 
space_in_a_car =4.0
drivers =30 
passengers = 90 
cars_not_drivers  = car -drivers

cars_drivers =drivers 
capool_capacity = cars_drivers  * space_in_a_car

avgrage_passenger_per_car = passengers / cars_drivers 



print("there are",car ,"cars available.")
print("There are only",drivers ,"drivers available.")
print("There will be",cars_not_drivers  ,"empty cars today.")
print("We can transport",capool_capacity,"people today.")
print("We have",passengers  ,"to car pool today")
print("We need to put about",avgrage_passenger_per_car ,"in each car.")

