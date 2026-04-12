import subprocess
import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent
JAR_PATH = BASE_DIR / "antlr-4.13.2-complete.jar"

def compilar_antlr(caminho_gramatica, diretorio_saida=None):
    if not JAR_PATH.exists():
        print(f"Erro: O arquivo {JAR_PATH.name} não foi encontrado na raiz.", file=sys.stderr)
        sys.exit(1)

    arquivo_g4 = Path(caminho_gramatica).resolve()
    if not arquivo_g4.exists():
        print(f"Erro: Gramática {arquivo_g4} não encontrada.", file=sys.stderr)
        sys.exit(1)

    # Se não passar diretório de saída, gera na mesma pasta do .g4
    pasta_saida = Path(diretorio_saida).resolve() if diretorio_saida else arquivo_g4.parent
    pasta_saida.mkdir(parents=True, exist_ok=True)

    print(f"Compilando: {arquivo_g4.name}...")
    
    comando = [
        "java", "-jar", str(JAR_PATH), 
        "-Dlanguage=Python3", 
        "-o", str(pasta_saida), 
        str(arquivo_g4)
    ]

    resultado = subprocess.run(comando, cwd=BASE_DIR)

    if resultado.returncode == 0:
        print(f"✔ Código gerado com sucesso em: {pasta_saida.relative_to(BASE_DIR)}")
    else:
        print("✖ Falha na compilação do ANTLR.", file=sys.stderr)
        sys.exit(resultado.returncode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compila gramáticas ANTLR4 para Python3.")
    parser.add_argument("gramatica", help="Caminho para o arquivo .g4")
    parser.add_argument("-o", "--out", help="Diretório de saída para os arquivos gerados (opcional)")
    
    args = parser.parse_args()
    compilar_antlr(args.gramatica, args.out)