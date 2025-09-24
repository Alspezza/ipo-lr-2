num1 = int(input("Введите количество учеников в классе 1:"))
num2 = int(input("Введите количество учеников в классе 2:"))
num3 = int(input("Введите количество учеников в классе 3:"))

parti1 = (num1 // 2) + (num1 % 2)
parti2 = (num2 // 2) + (num2 % 2) 
parti3 = (num3 // 2) + (num3 % 2)

y = parti1 + parti2 + parti3 

print ("Нужно количество парт:", y )


  
  