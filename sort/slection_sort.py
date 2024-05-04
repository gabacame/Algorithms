import matplotlib.pyplot as plt
import matplotlib.animation as animation

array = [5, 7, 2, 1, 6, 9, 3, 4, 8]

def selection_sort(array):
    sorted_array = []
    while bool(array):
        v_min = min(array)
        sorted_array.append(v_min)
        array.remove(v_min)
        yield array.copy(), sorted_array[:]  # Generar una copia de ambas listas en cada iteración

# Inicializar la figura
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

def update_fig(frame):
    axs[0].clear()
    axs[1].clear()
    try:
        original, sorted_step = next(steps)
        axs[0].bar(range(len(original)), original, color='lightcoral')
        axs[0].set_title("Original")
        axs[1].bar(range(len(sorted_step)), sorted_step, color='skyblue')
        axs[1].set_title("Sorted")
    except StopIteration:
        ani.event_source.stop()  # Detener la animación cuando se terminen los pasos

# Generar los pasos de ordenamiento
steps = selection_sort(array.copy())

# Crear la animación
ani = animation.FuncAnimation(fig, update_fig, interval=1000)

# Mostrar y guardar la animación como un archivo GIF
ani.save('selection_sort_animation.gif', writer='pillow')

plt.show()

