# main.py
from resolver_problema import resolver_optimización
import openpyxl

# Leer los datos del archivo Excel
def leer_datos_excel(ruta):
    libro = openpyxl.load_workbook(ruta)
    hoja = libro.active
    datos = []
    for fila in hoja.iter_rows(min_row=2, max_col=5, values_only=True):
        datos.append(fila)
    return datos

def main():
    # Ruta del archivo Excel
    ruta = "./Excel/problema5.xlsx"
    
    # Leer los datos
    datos = leer_datos_excel(ruta)
    
    # Resolver el problema de optimización
    asignaciones, tiempo_total = resolver_optimización(datos)
    
    # Mostrar resultados
    print(f"Asignaciones:\n {asignaciones}")
    print(f"Tiempo total de asignación: {tiempo_total}")

if __name__ == "__main__":
    main()
