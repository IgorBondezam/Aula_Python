import os
import shutil

caminho_original= "C:\\Users\\Igor\\Desktop\\Nova pasta (2)\\"
caminhoNovo = "C:\\Users\\Igor\\Desktop\\Videoooo2\\"


try:
    os.mkdir(caminhoNovo)
except FileExistsError as e:
    print(f"Pasta {caminhoNovo} já existe.")



for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminhoNovo, file)

        print(old_file_path)

        shutil.copy(old_file_path, new_file_path)

        print(f"Arquivo {file} copiado com sucesso.")

        os.rename(caminhoNovo + file, caminhoNovo + "abobooooora.bat")



certificar = input("Deseja apagar o arquivo criado? ")
if certificar == "s":
    os.remove(caminhoNovo + "abobooooora.bat")
    print("Arquivo excluido com sucesso.")