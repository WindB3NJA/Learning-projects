"""
Proyecto: Busqueda de n de series dentro de archivos
"""
import os, datetime, time, re, math, pathlib

from babel.dates import parse_time

proyect_dir = pathlib.Path(os.getcwd()) / "Mi_Gran_Directorio"

date_today = str(datetime.date.today()).split("-")[::-1]

Nseries_founded = {}

duration = 0

def found_2_me_Nseries(root_dir):
    init = time.time()
    N_series_format = r"N\w{3}-\d{5}"
    for dirs in os.walk(root_dir):
        for file in dirs[2]:
            txt_file = str(pathlib.Path(dirs[0]) / file)
            if re.findall(r".txt$", txt_file) == [".txt"]:
                file_to_read = open(txt_file, "r")
                readed_file = file_to_read.read()
                find_Nseries = re.findall(N_series_format, readed_file)
                if find_Nseries != []:
                    Nseries_founded[file] = str(find_Nseries[0])
                file_to_read.close()
    duration = time.time()-init

print(f"{"-"*52}\nFecha de búsqueda: {date_today[0]}/{date_today[1]}/{date_today[2]}\n")
found_2_me_Nseries(proyect_dir)
print(f"ARCHIVO\t\tNRO. SERIE\n{"-"*6}\t\t{"-"*9}")
for key in Nseries_founded:
    print(f"{key}\t{Nseries_founded[key]}")
print(f"\nNúmeros encontrados: {len(Nseries_founded)}\nDuración de la búsqueda: {math.ceil(duration)} Segundos \n{"-"*52}")