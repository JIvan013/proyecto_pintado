# resolver_problema.py
import pulp

def resolver_optimización(datos):
    """
    Resuelve el problema de asignación de máquinas a papeles para minimizar el tiempo total.
    """
    # Número de máquinas y papeles
    n_maquinas = len(datos)
    n_papeles = 3  # Sabemos que hay 3 papeles

    # Crear el problema de optimización lineal
    prob = pulp.LpProblem("Problema_de_Asignacion", pulp.LpMinimize)

    # Crear las variables de decisión (x_ij)
    x = pulp.LpVariable.dicts("Asignacion", (range(n_maquinas), range(n_papeles)), cat="Binary")

    # Función objetivo: minimizar el tiempo total
    prob += pulp.lpSum(
        datos[i][j+2] * x[i][j]  # Asegúrate de que los índices son correctos para acceder a los tiempos
        for i in range(n_maquinas) 
        for j in range(n_papeles) 
        if datos[i][j+2] != "M"  # Asegúrate de que el valor es un número válido y no "M"
    ), "Tiempo_Total"

    # Restricción: cada máquina debe ser asignada a un solo papel
    for i in range(n_maquinas):
        prob += pulp.lpSum(x[i][j] for j in range(n_papeles)) == 1, f"Restriccion_maquina_{i}"

    # Restricción: cada papel debe ser asignado a una sola máquina
    for j in range(n_papeles):
        prob += pulp.lpSum(x[i][j] for i in range(n_maquinas)) == 1, f"Restriccion_papel_{j}"

    # Resolver el problema
    prob.solve()

    # Verifica el estado de la solución
    print(f"Estado de la solución: {pulp.LpStatus[prob.status]}")

    # Imprimir la solución
    if pulp.LpStatus[prob.status] == "Optimal":
        asignaciones = []
        tiempo_total = 0
        for i in range(n_maquinas):
            for j in range(n_papeles):
                if pulp.value(x[i][j]) == 1:
                    asignaciones.append(f"Máquina {i+1} asignada al Papel {j+1}")
                    tiempo_total += datos[i][j+2]
        return asignaciones, tiempo_total
    else:
        return "No se encontró una solución óptima"