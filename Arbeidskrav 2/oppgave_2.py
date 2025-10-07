# importere bibliotek for å runde opp tall
import math 

# input til beregning
antall_elever = int(input("Skriv inn antall alever: "))

# beregne antall pizzaer
antall_pizza = antall_elever / 4

# output + runde opp tallet for å håndtere desimaltall
print("Det må handles inn", math.ceil(antall_pizza), "pizzaer til festen.")