divisiones = (
    "Bocas del Toro",
    "Coclé",
    "Colón",
    "Chiriquí",
    "Darién",
    "Herrera",
    "Los Santos",
    "Panamá",
    "Panamá Oeste",
    "Veraguas",
    "Guna Yala",
    "Ngäbe-Buglé",
    "Emberá-Wounaan"
)

for d in divisiones:
    print(d)

try:
    divisiones[0] = "Otra provincia"
except:
    print("No se puede modificar la tupla")