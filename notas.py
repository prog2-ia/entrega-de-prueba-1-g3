def pideNotas(numNotas):
    notas = []
    for i in range(5):
        nota = float(input(f"Introduce la nota {i + 1}: "))
        notas.append(nota)
    return notas

def calculaMedia(notas):
    return sum(notas) / len(notas)

def calculaMaximo(notas):
    return max(notas)

def calculaMinimo(notas):
    return min(notas)

if __name__ == "__main__":
    numNotas = 5
    notas = pideNotas(numNotas)
    print("Las notas introducidas son:")
    for i, nota in enumerate(notas):
        print(f"Nota {i + 1}: {nota}")