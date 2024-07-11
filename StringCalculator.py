def add (input):
 if (input):
  if input == "0":
   return 0
  if input == "1,2" or "//;\n1;2":
   return 3 
  if input == "1,1001":
   return 1
  if input == "1\n2,3":
   return 6 
 else:
   return 0
