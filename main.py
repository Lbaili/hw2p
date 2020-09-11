# Author: Chang Li cxl5844@psu.edu
# Collaborator:axa6066@psu.edu
# Collaborator:tmd5681@psu.edu
# Section: 1
# Breakout: 14

def getGradePoint(g):
  if g == "A" : 
    a = 4.0
  elif g == "A-" : 
    a = 3.67
  elif g == "B+" : 
    a = 3.33
  elif g == "B" : 
    a = 3.0
  elif g == "B-" : 
    a = 2.67
  elif g == "C+" : 
    a = 2.33
  elif g == "C" : 
    a = 2.0
  elif g == "D" : 
    a = 1.0
  else: 
    a = 0.0
  return a

if __name__ =="__main__":
  b1 = input("Enter your course 1 letter grade: ")
  c1 = float(input("Enter your course 1 credit: "))
  a1 = getGradePoint(b1)
  print(f"Grade point for course 1 is: {a1}")
  b2 = input("Enter your course 2 letter grade: ")
  c2 = float(input("Enter your course 2 credit: "))
  a2 = getGradePoint(b2)
  print(f"Grade point for course 2 is: {a2}")
  b3 = input("Enter your course 3 letter grade: ")
  c3 = float(input("Enter your course 3 credit: "))
  a3 = getGradePoint(b3)
  print(f"Grade point for course 3 is: {a3}")
  GPA = (a1 * c1 + a2 * c2 +a3 * c3)
  GPA /= (c1 + c2 + c3)
  print(f"Your GPA is: {GPA} ")