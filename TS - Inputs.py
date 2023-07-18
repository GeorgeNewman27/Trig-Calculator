def infans():
  print("")
  print("WARNING")
  print("")
  print("INFINITE SOLUTIONS EXIST")
  print("")
  input("EXE to restart...")
  print("")
  main()

def findangles(sides):
  return

def findthirdangle(angles):
  return

def findsidecos(angles, sides):
  return
  
def main():
  angles = [-1.0, -1.0, -1.0, 0, 0]
  sides =  [-1.0, -1.0, -1.0, 0]
  
  for i in range (3):
    #Get user input as string
    users = input("Input side " + str(i + 1) + " : ")

    #Check to see if the user input anything at all
    if users == "":
      print("No value given for side " + str(i + 1))
    else:
      #Attempt to convert input to a float
      try:
        sides[i] = float(users)
      
      #If entered value is not a number
      except ValueError:
        if (sides[i] != 0):
          sides[i] = -1.0
          raise Exception("Input must be a number")

      #If entered value is a number, check to ensure it is positive
      finally:
        if sides[i] > 0.0:
          sides[3] = sides[3] + 1
          print("Side " + str(i + 1) +  " value accepted as " + str(sides[i]))
          print("Number of sides given: " + str(sides[3]))
        if (sides[i] <= 0.0) & (sides[i] != -1.0):
          raise Exception("Positive Numbers Only")
        
  #If no sides are entered, they can all be multiples of eachother so infinite solutions exist     
  if sides[3] == 0:
    infans()
  #If all sides are entered, all other angles can be found with cosine rule but each angle will only have one solution
  if sides[3] == 3:
    findangles(sides)
    
  for j in range (3):
    #Get user input as string
    usera = input("Input angle " + str(j + 1) + " : ")

    #Check to see if the user input anything at all
    if usera == "":
      print("No value given for angle " + str(j + 1))
    else:
      #Attempt to convert input to a float
      try:
        angles[j] = float(usera)
      
      #If entered value is not a number
      except ValueError:
        if (angles[j] != 0):
          angles[j] = -1.0
          raise Exception("Input must be a number")

      #If entered value is a number, check to ensure it is within bounds
      finally:
        if angles[j] > 0.0:
          angles[3] = angles[3] + 1
          angles[4] = angles[4] + angles[j]
          print("Angle " + str(j + 1) +  " value accepted as " + str(angles[j]))
        if ((angles[j] <= 0.0) & (angles[j] != -1.0 )) | (angles[j] >= 180):
          raise Exception("Angles between 0 and 180 only")

  #If only 1 angle and side are given, there are an infinite number of possible solutions.
  if (angles[3] <= 1) & (sides[3] <= 1):
    infans()
    
  #Ensure that sum of angles are less than 180
  if ((angles[3] == 3 & angles[4] != 180) | (angles[3] < 3 & angles[4] >= 180)):
    raise Exception("Angles must sum to <= 180")
    
  #If 2 angles are provided, because the sum of all angles is known, we can work out the third  
  if angles[3] == 2:
    findthirdangle(angles)

  #If 1 angle and 2 sides are provided, you can use the cosine rule to work out the remaining side
  if (angles[3] == 1) & (sides[3] == 2):
    findsidecos(angles, sides)

  else:
    raise Exception("Could Not Find Compatable Algorithm")
        
main()