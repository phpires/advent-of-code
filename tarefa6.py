from collections import Counter

#file_path = "/content/drive/MyDrive/Colab Notebooks/adventOfCode/input06_test.txt"
file_path = "D:/advent-of-code/dados/input06.txt"
total_de_dias_pt01 = 80
total_de_dias_pt02 = 256
parte_atual = 2
with open(file_path, "r") as file:
    
    peixes = file.readlines()
    peixes = [int(x) for x in peixes[0].split(",")]

    if (parte_atual == 1):
        print("Estado inicial: {}".format(peixes))
        for dia in range(total_de_dias_pt01):
            print("Dia {}.".format(dia))
            for idx, peixe in enumerate(peixes):
                if (peixe == 0):
                    peixes[idx] = 6
                    peixes.append(9)
                else:
                    peixes[idx] = peixes[idx] - 1
    else:
        print("Estado inicial: {}".format(peixes))
        v = {x: 0 for x in range(9)}
        peixes = Counter(peixes)
        peixes.update(v)
        #print(peixes.get(3))

        for dia in range(total_de_dias_pt02):
            peixes_6 = peixes[0] + peixes[7]
            peixe_nascido = peixes[0]

            peixes[0] = peixes[1]
            peixes[1] = peixes[2]
            peixes[2] = peixes[3]
            peixes[3] = peixes[4]
            peixes[4] = peixes[5]
            peixes[5] = peixes[6]
            peixes[6] = peixes_6
            peixes[7] = peixes[8]
            peixes[8] = peixe_nascido

    print("[INFO] Total de peixes: {}".format(sum(peixes.values())))

