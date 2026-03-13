def percorrer_matriz(m, n):
    for i in range(m):
        for j in range(n):
            print(f"Posicao ({i}, {j})")

print("Testando com m=0 e n=0:")
percorrer_matriz(0, 0)

print("Testando com m=2 e n=0:")
percorrer_matriz(2, 0)

print("Testando com m=1 e n=4:")
percorrer_matriz(1, 4)

print("Testando com m=3 e n=3:")
percorrer_matriz(2, 5)