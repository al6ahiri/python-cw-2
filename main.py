my_name = input('whats is your name ?')
my_age = input('how old you ? ')

print (f'my name is "saud" , im "18" years old'  )

first_number = int (input("number one :"))
second_number = int (input("number two :"))


operation = input(" enter : ")
if operation == '+' :
  print ( first_number + second_number)
elif operation ==  '-' :
  print (first_number - second_number)
elif operation == '*' :
  print (first_number * second_number)
elif operation == '/' :
  print (first_number / second_number)


  bus_capacity = 60
  people_inbus = int(input("how many people are in the bus"))
  empty_seats = bus_capacity - people_inbus

  if bus_capacity>= people_inbus :
    print (f"there is {empty_seats }")
  elif bus_capacity < people_inbus :
    print (f"there is no seatsm")