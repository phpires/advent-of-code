import sys
import itertools

#file_path = "/content/drive/MyDrive/Colab Notebooks/adventOfCode/input05_test.txt"
file_path = "D:/advent-of-code/dados/input05.txt"

def obter_coordenada(coordenada):
  x1 = int(coordenada.split(" -> ")[0].split(",")[0])
  y1 = int(coordenada.split(" -> ")[0].split(",")[1])
  x2 = int(coordenada.split(" -> ")[1].split(",")[0])
  y2 = int(coordenada.split(" -> ")[1].split(",")[1])
  return ((x1,y1),(x2,y2))

with open(file_path, "r") as file:
  coordenadas = file.readlines()

  #Inicializando dict
  print("[INFO] Inicializando diagrama..")
  pontos_x = []
  pontos_y = []
  diagrama = {}
  resposta = 0
  for coord in coordenadas:
    ((x1,y1), (x2,y2)) = obter_coordenada(coord)
    pontos_x.append(x1)
    pontos_x.append(x2)
    pontos_y.append(y1)
    pontos_y.append(y2)

  for ponto_x in range(0, max(pontos_x)+1):
      for ponto_y in range(0, max(pontos_y)+1):
        diagrama[(ponto_x,ponto_y)] = 0

  print("[INFO] diagrama incializado {}".format(diagrama))
  #Marcando diagrama
  for coord in coordenadas:
    print(">>>>>>>> [INFO] Nova reta <<<<<<<<")

    ((x1,y1),(x2,y2)) = obter_coordenada(coord)
    
    print("[INFO] Analisando a reta ({},{})->({},{})".format(x1,y1,x2,y2))
 
    if (x1 == x2):
      #(0,9) -> (2,9) range(0,2) -> 0, 1 x -> 0 e x -> 1
      ponto_x = x1 #pode por x2 se quiser pq é igual
      if (y1 < y2):
        for ponto_y in range(y1,y2+1):
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
      elif (y1 > y2):
        for ponto_y in range(y2,y1+1):
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
      else:#(x1==x2 e y1==y2)
        ponto_y = y1 #ibidem
        print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
        diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
        print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
    elif (x1 < x2):
      if (y1 == y2):
        ponto_y = y1
        for ponto_x in range(x1,x2+1):
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
      else:
        intervalo = x2 - x1
        for i in range(0, intervalo+1):
          ponto_x = x1 + i
          if (y1 > y2):
            ponto_y= y1 - i
          else:
            ponto_y= y1 + i
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
    elif (x1 > x2):
      if (y1 == y2):
        ponto_y = y1
        for ponto_x in range(x2,x1+1):
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))
      else:
        intervalo = x1 - x2
        for i in range(0, intervalo+1):
          ponto_x = x1 - i
          if (y1 > y2):
            ponto_y= y1 - i
          else:
            ponto_y= y1 + i
          print("[INFO] Marcando o ponto: ({},{})".format(ponto_x,ponto_y))
          diagrama[(ponto_x,ponto_y)] = diagrama[(ponto_x,ponto_y)] + 1
          print("[INFO] Marcações em: ({},{}): {}".format(ponto_x,ponto_y,diagrama[(ponto_x,ponto_y)]))


  for dict_key in diagrama:
    if (diagrama[dict_key] >= 2):
      resposta = resposta + 1

print("[INFO] RESPOSTA: {}".format(resposta))