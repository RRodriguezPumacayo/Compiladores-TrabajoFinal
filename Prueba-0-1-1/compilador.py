import re

def leer_archivo_cpp(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.readlines()

def traducir_linea(linea):
    linea = linea.strip()

    if re.match(r'^\s*(int|float|double|char)\s+', linea):
        linea = re.sub(r'(int|float|double)\s+', '', linea)
        linea = re.sub(r'char\s+', 'str ', linea)
        linea = re.sub(r';$', '', linea)
        return linea

    if re.match(r'^\s*void\s+\w+\s*\(\s*\)\s*{\s*$', linea):
        linea = re.sub(r'void\s+', 'def ', linea)
        linea = re.sub(r'{\s*$', ':', linea)
        return linea
    
    if re.match(r'^\s*}\s*$', linea):
        return ""

    return linea

def escribir_archivo_py(ruta_archivo, lineas):
    with open(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            archivo.write(linea + '\n')

def compilar(ruta_archivo_cpp, ruta_archivo_py):
    lineas_cpp = leer_archivo_cpp(ruta_archivo_cpp)
    lineas_py = [traducir_linea(linea) for linea in lineas_cpp]
    escribir_archivo_py(ruta_archivo_py, lineas_py)

# Uso del compilador
ruta_archivo_cpp = 'prueba.cpp'
ruta_archivo_py = 'codigo.py'
compilar(ruta_archivo_cpp, ruta_archivo_py)
