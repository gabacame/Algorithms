import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

array = np.array([5,7,2,1,6,9,3,4,8]) 

def bubble_sort(array):
    steps = [array.copy()]  # Almacenamos la lista original como el primer paso
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
                steps.append(array.copy())  # Almacenamos el estado actual de la lista
    return steps

frames = list(bubble_sort(array.copy()))

def update_fig(frame):
    plt.cla()
    if frame < len(frames):
        plt.bar(range(len(frames[frame])), frames[frame], color='red')
    plt.title("Bubble Sort")

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_fig, frames=len(frames)+1, interval=500, repeat=False)
ani.save('bubble_sort_animation.gif', writer='pillow')
plt.show()


