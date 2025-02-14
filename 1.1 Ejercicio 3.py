import matplotlib.pyplot as plt

def calcular_errores(x, y, valor_real):
    """Calcula errores absoluto, relativo y porcentual"""
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    
    return diferencia, error_abs, error_rel, error_pct

# Lista de valores de prueba
valores = [(1.0000001, 1.0000000, 0.0000001), 
           (1.000000000000001, 1.000000000000000, 0.000000000000001)]

# Listas para almacenar los resultados
casos = []
errores_abs = []
errores_rel = []
errores_pct = []

# Procesar cada conjunto de valores
for idx, (x, y, real) in enumerate(valores, start=1):
    print(f"\nPara x={x}, y={y}:")
    diferencia, error_abs, error_rel, error_pct = calcular_errores(x, y, real)
    
    # Guardar resultados para la gráfica
    casos.append(idx)
    errores_abs.append(error_abs)
    errores_rel.append(error_rel)
    errores_pct.append(error_pct)

# ----- GRAFICAR LOS ERRORES -----
plt.figure(figsize=(8, 5))

plt.plot(casos, errores_abs, marker='o', linestyle='-', label="Error Absoluto", color='blue')
plt.plot(casos, errores_rel, marker='s', linestyle='--', label="Error Relativo", color='green')
plt.plot(casos, errores_pct, marker='^', linestyle='-.', label="Error Porcentual", color='red')

plt.xlabel("Caso de Prueba")
plt.ylabel("Valor del Error")
plt.title("Comparación de Errores")
plt.yscale("log")  # Escala logarítmica para mejor visualización si hay valores pequeños
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Mostrar la gráfica
plt.show()