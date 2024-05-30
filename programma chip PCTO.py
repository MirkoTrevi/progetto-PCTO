import math
import matplotlib.pyplot as plt

a = int(input("larghezza(mm): "))
b = int(input("altezza (mm): "))
r = int(input("raggio (mm): "))
spazio = int(input("spazio tra i chip (mm): "))

chip_inside = []
chip_cut = []

def funzione_chip_nel_wafer(r, a, b, spazio):
    numero_di_chip = 0
    raggio_piccolo = r - math.sqrt(a ** 2 + b ** 2) / 2
    passo_x = a + spazio
    passo_y = b + spazio
    for x in range(-int(raggio_piccolo), int(raggio_piccolo), passo_x):
        for y in range(-int(raggio_piccolo), int(raggio_piccolo), passo_y):
            if (x + a/2) ** 2 + (y + b/2) ** 2 <= raggio_piccolo ** 2:
                numero_di_chip += 1
                chip_inside.append((x, y))
    return numero_di_chip, chip_inside

def funzione_chip_tagliati(r, a, b, spazio):
    numero_chip_tagliati = 0
    raggio_piccolo = r - math.sqrt(a ** 2 + b ** 2) / 2
    raggio_grande = r + math.sqrt(a ** 2 + b ** 2) / 2
    passo_x = a + spazio
    passo_y = b + spazio
    for x in range(-int(raggio_grande), int(raggio_grande) + 1, passo_x):
        for y in range(-int(raggio_grande), int(raggio_grande) + 1, passo_y):
            distanza_rett_centro = (x + a/2) ** 2 + (y + b/2) ** 2
            if raggio_piccolo ** 2 < distanza_rett_centro <= raggio_grande ** 2:
                numero_chip_tagliati += 1
                chip_cut.append((x, y))
    return numero_chip_tagliati, chip_cut

numero_di_chip, chip_inside = funzione_chip_nel_wafer(r, a, b, spazio)
numero_chip_tagliati, chip_cut = funzione_chip_tagliati(r, a, b, spazio)

print("Numero di chip nel wafer:", numero_di_chip)
print("Numero di chip tagliati:", numero_chip_tagliati)

fig, ax = plt.subplots()

wafer = plt.Circle((0, 0), r, color='blue', fill=False)
ax.add_artist(wafer)

for (x, y) in chip_inside:
    rect = plt.Rectangle((x, y), a, b, color='green', alpha=0.4)
    ax.add_artist(rect)

for (x, y) in chip_cut:
    rect = plt.Rectangle((x, y), a, b, color='red', alpha=0.4)
    ax.add_artist(rect)

ax.set_xlim(-r, r)
ax.set_ylim(-r, r)
ax.set_aspect('equal', 'box')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('Grafico dei chip nel wafer')
plt.grid(True)
plt.show()
