import os
dt = "/tmp/exercicios"
if not os.path.exists(dt):
    os.makedirs(dt)
os.chmod(dt, 0o744)
valor = 0
dir = ""
arq = ""
def mult(vlr, tab):
    res = vlr * tab
    return res
def grava(c, rslt):
    global dir, arq
    dir = "/tmp/exercicios"
    arq = "ex34.txt"
    file = ""
    tipo = ""
    enc = ""
    linha = str(rslt) + "\n"
    if os.path.exists(dir) and os.path.isdir(dir):
        ca = os.path.join(dir, arq)
        tipo = "w"
        if os.path.exists(ca) and c > 0:
            tipo = "a"
        file = open(ca, tipo, encoding="utf-8")
        file.write(linha)
        file.close()
def main():
    global valor
    c = 0
    rslt = 0
    valor = int(input("Digite um número para ver a tabuada: "))
    for c in range(1, 11):
        rslt = mult(valor, c)
        grava(c, rslt)
if __name__ == "__main__":
    main()