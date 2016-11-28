def basecounter(string):
  
  #The counting can be contained within a dictionary comprehension; the iterated string "ACTG" can be modified to include things like 
  #missing values if need be
  
  return {x:string.count(x) for x in "ACTG"}


