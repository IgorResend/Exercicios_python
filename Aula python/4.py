def solicitar_voto():
    try:
        voto = int(input("Digite o número do candidato (1-4): "))
        return voto
    except ValueError:
        return 0

def main():
    votos = [0, 0, 0, 0]

    for _ in range(10):
        voto = solicitar_voto()

        match voto:
            case 1:
                votos[0] += 1
            case 2:
                votos[1] += 1
            case 3:
                votos[2] += 1
            case 4:
                votos[3] += 1
            case _:
                print("Voto inválido!")
                
    for i, voto in enumerate(votos):
        print(f"Candidato {i + 1} recebeu {voto} votos.")

if __name__ == "__main__":
    main()
