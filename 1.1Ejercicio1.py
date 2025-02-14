import numpy as np
import matplotlib.pyplot as plt

# Inicialización
epsilon = 1.0
iteracion = 0
iteraciones = []
valores_epsilon = []

# Bucle para calcular la precisión de máquina
while 1.0 + epsilon != 1.0:
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon:.2e}")  # Mostrar resultados en consola
    
    iteraciones.append(iteracion)
    valores_epsilon.append(epsilon)

    epsilon /= 2
    iteracion += 1

# Último valor válido de precisión de máquina
epsilon *= 2
print(f"\nPrecisión final de máquina: {epsilon:.2e}")

# Graficar la evolución de epsilon
plt.figure(figsize=(8, 5))
plt.plot(iteraciones, valores_epsilon, marker='o', linestyle='-')
plt.yscale("log")  # Escala logarítmica para mejor visualización
plt.xlabel("Iteraciones")
plt.ylabel("Precisión de máquina (epsilon)")
plt.title("Evolución de la Precisión de Máquina")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
