import math

def print_love():
    for y in range(30, -30, -1):
        for x in range(-30, 30):
            equation = (math.pow(x/10, 2) + math.pow(y/10, 2) - 1) * (math.pow(x/10, 2) + math.pow(y/10, 2) - 1) * (math.pow(x/10, 2) + math.pow(y/10, 2) - 1) - math.pow(x/10, 2) * math.pow(y/10, 3)
            
            # Cek apakah koordinat (x, y) berada dalam bentuk love
            if equation <= 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_love()
