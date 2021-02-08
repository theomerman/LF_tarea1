if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
def funcion(iterador):
    contador = 0
    numero = 0
    for i in range(200):
        for j in range(n):
            if iterador == arr[j]:
                contador += 1
                numero = iterador
                break

        if contador == 2:
            break
        iterador -= 1
    return numero

print funcion(100)