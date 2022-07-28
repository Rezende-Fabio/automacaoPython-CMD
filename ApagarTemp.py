import shutil
import os
import warnings
from tkinter import messagebox

lista_de_usuarios = os.listdir("C:\\Users")
repeticoes = len(lista_de_usuarios) + 3

messagebox.showinfo("Info", "Limpeza vai ser Iniciada")

for x in range(repeticoes):
    pasta = "C:\\Temporarios"
    #Cria a pasta caso ela não exista
    if os.path.exists(pasta):
        pass
    else:
        os.makedirs(pasta)

    temp_wind = "C:\\Windows\\Temp"
    lista_arquivos = os.listdir("C:\\Windows\\Temp")

    for arquivo in lista_arquivos: #Lê os arquivos da pasta temporários do Windows
        try:
            arq_para_mover = f"{temp_wind}\\{arquivo}" 
            
            shutil.move(arq_para_mover, pasta)

        except shutil.Error:
            warnings.filterwarnings("ignore")
        except PermissionError:
            warnings.filterwarnings("ignore")

    for usuario in lista_de_usuarios:
        
        if usuario != "All Users" and usuario != "Default User" and usuario != "desktop.ini" and usuario != "Public" and usuario != "Todos os Usuários":
            
            local_por_usuario = f"C:\\Users\\{usuario}\\AppData\\Local\\Temp"
            lista_de_arq_por_usuario = os.listdir(local_por_usuario)

            if len(lista_de_arq_por_usuario) != 0:

                for arquivo in lista_de_arq_por_usuario: #Lê os arquivos da pasta temporários de cada usuário
                    try:
                        arq_para_movero = f"{local_por_usuario}\\{arquivo}"
                        shutil.move(arq_para_movero, pasta)

                    #Ignora os arquivos não é possível apagar no momento
                    except shutil.Error:
                        warnings.filterwarnings("ignore")
                    except PermissionError:
                        warnings.filterwarnings("ignore")
                    except FileNotFoundError:
                        warnings.filterwarnings("ignore")
        else: 
            pass

    shutil.rmtree(pasta, ignore_errors=True, onerror=None)

messagebox.showinfo("Info", "Temporarios Limpos")