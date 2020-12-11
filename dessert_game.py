def dessert():
  # you need:
  # water - so that you can drink
  # food so you can eat 
  # fule so that the car can drive
  # jumper so you are warm at night
  #your plane ticket so that you can get home again
  #----------------------------------------------------------------------------------------
  items = [
  "A: 3 litres of water",
  "B: Shampoo",
  "C: A Spacesuit",
  "D: A shovel",
  "E: jumper",
  "F: Solar panels",
  "G: some seeds ",
  "H: 5 days worth of Fule",
  "I: A 3 day food supply",
  "J: your favorite cuddely toy",
  "K: food for 4 days",
  "L: you plane ticket ",

  ]
  #--------------------------------------------
  print ("what is your name")
  name = input ("my name is ")

  print ("hello " + name + " you are stuck in the middle of the sahara desert you have a vehicle but it will take you 3 days to get to the airport in the car. ")
  print("you can carry 5 items and you")
  for object in items:
    print (object)
#--------------------------------------------
  print("Type the letter of the 5 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D,E")
  user_choice = input ("enter your choice:")
#print (user_choice)

  user_list = list(user_choice.split(','))
#print (user_list)




  if "A" not in user_list:
    print ("without a litre of water a day you will de-hydrate")

  if " E" not in user_list:
    print ("you need to be keep warm, at night in the desert it is very cold. the average night time temoerater in the sahara desert is -3.9°C")

  if "H" not in user_list:
    print ("without solar pannels the rover will not have any power")
  
  if "I" not in user_list:
    print ("without food you will not arive at the base, you will not have enough energy to drive to rover")

  if "L" not in user_list:
    print ("with no plane ticket you can not get home")
  if "A" in user_list:
  
    if "E" in user_list:
    
      if "H" in user_list:
      
        if "I" in user_list:
        
          if "L" in user_list:
          
            print ("congratulations " + name + " you made it home and are now on the news")