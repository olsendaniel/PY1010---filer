import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# DEL A

# lagrer navnet for lettere tilbakekalling senere
file = "support_uke_24.xlsx"

# leser inn data fra excel filen og sjekker output
df = pd.read_excel(file)
print(df)

# Tildele variablene til de ulike kolonnene
u_dag = np.array(df["Ukedag"])
k_slett = np.array(df["Klokkeslett"])
varighet = np.array(df["Varighet"])
score = np.array(df["Tilfredshet"])


# DEL B

# lagre tuppel output i to  variabler og teller sammen antall ulike dager
dager, antall = np.unique(u_dag, return_counts=True)

# sjekke resultat
print(dager)
print(antall)

    # Siden dagene var ikke i rekkefølge lager jeg en egen liste med riktig rekkefølge,
    # og teller alt på nytt

# Sortere dagene manuelt for plotting
dager_rekkefølge = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
antall_sortert = []

for dag in dager_rekkefølge:
    telling = np.sum(u_dag == dag)
    antall_sortert.append(telling)

print(antall_sortert)

# Visualisering av antall dager i søylediagram
def plotting(dager, antall):
    plt.bar(dager, antall)
    plt.xlabel("Dager")
    plt.ylabel("Antall")
    plt.show()

plotting(dager_rekkefølge, antall_sortert)


# DEL C

# finne den korteste og lengste samtaletiden og gi informativ tekst
korteste = min(varighet)
lengste = max(varighet)

# Gi en output i konsollen med informativ tekst om varighet
print("Den korteste samtalen var", korteste, "lang, og den lengste varte", lengste,".")


# DEL D

# konvertere tiden til sekunder for lettere håndtering
delta_tid = pd.to_timedelta(varighet)
print(delta_tid)

sekunder = delta_tid.total_seconds()
print(sekunder)

# summere sekundene og dele på antall observasjoner
total_tid = sum(sekunder)
snitt_tid = total_tid / len(varighet)

print(
    "Gjennomsnitlig tid for en samtale i perioden var:", round(snitt_tid, 2), " sekunder,som tilsvarer:", 
    round(snitt_tid / 60, 2), " minutter."
    )


# DEL E

# beregne delta tiden for kl_slett
kl_slett_td = pd.to_timedelta(k_slett)

# Hente ut timene fra de ulike tidspunktene for henvendelsene
timer = kl_slett_td.components["hours"]

# en liste med navnene som jeg skal bruke i kakediagrammet
bolker_navn = ["kl 08-10", "kl 10-12", "kl 12-14", "kl 14-16"]

# lage en tom liste hvor jeg summerer opp antall observasjoner i bolkene som er definert i lista "grenser"
bolker = []
grenser = [(8,10), (10,12), (12,14), (14,16)]

# løkke for å telle sammen henvendelser i bolkene
for start, slutt in grenser:
    telling = np.sum((timer >= start) & (timer < slutt))
    bolker.append(telling)
    
# bruker samme logikk som over ved å lage tom liste som jeg fyller opp med labels
labels = []

# zippe sammen tuppelsene for å enklere legge de til i kakediagrammet
for navn, antall in zip(bolker_navn, bolker):
    labels.append(f"{navn} ({antall})")

# plotte selve kakediagrammet
plt.pie(bolker, labels=labels)
plt.show()


# DEL F

