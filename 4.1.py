#4.1
from sys import argv

name, hours, stavka, premiya = argv

zp = int(hours) * int(stavka) + int(premiya)
print(f"ZarPlata: {zp}")
