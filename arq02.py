import os
dt = "/tmp/exercicios"
if not os.path.exists(dt):
    os.makedirs(dt)
os.chmod(dt, 0o744)
nome = ""
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
valor_media = 0.0
dir = ""
arq = ""
def med(n1, n2, n3, n4):
    media = float(n1 + n2 + n3 + n4) / 4.0
    return media
def escreveArq(caminho, arquivo, linha_arq):
    file = ""
    tipo = ""
    enc = "utf-8"
    if os.path.exists(caminho) and os.path.isdir(caminho):
        cp = os.path.join(caminho, arquivo)
        tipo = "w"
        if os.path.exists(cp):
            tipo = "a"   
        file = open(cp, tipo, encoding=enc)
        file.write(linha_arq)
        file.close()
def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    dir = "/tmp/exercicios"
    arq = "ex21.txt"
    linha = nm + ";" + str(nt1) + ";" + str(nt2) + ";" + str(nt3) + ";" + str(nt4) + ";" + str(vlr_med) + "\n"
    escreveArq(dir, arq, linha)
def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    valor_media = med(nota1, nota2, nota3, nota4)
    print(f"Média: {valor_media:.1f}")
    if valor_media >= 6.0:
        print("APROVADO")
    elif valor_media >= 3.0:
        print("EXAME")
    else:
        print("RETIDO")
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)
def main():
    c = 0
    for c in range(5):
        print(f"\n--- Aluno {c+1} ---")
        entrada()
if __name__ == "__main__":
    main()