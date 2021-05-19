height = int(input("what is your height: ?"))



if height > 120:
  print("you can ride the roller coaster")
  age = int(input("what is your age: ?"))
  if age == 18:
    print("you pay $5.")
  elif age >= 23:
    print("you pay $7.")
  else:
    print("you pay $12")
else:
  print("you cannot ride the roller coaster")