def pi_accuracy():
  d = str(float(input("Введите заданную точность d: ")))
  x = d.split(".") 
  b = len(str(x[1]))
  #  y = (len(str(d).split('.')[1])) 
  #это решение ломается 
    # когда берется маленькая дробь, потому что она переводится в строку как "1e-06"


  import math
  print (round(math.pi, (b)))

pi_accuracy()