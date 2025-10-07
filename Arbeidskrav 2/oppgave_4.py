data = {
    "Norge": ["Olso", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

land = input('Skriv inn et land: ')

# -- oppgave a, b og c i samme blokk --

if land in data:
    hovedstad, innbyggere = data[land]  # pakker ut begge verdiene
    print(f'Hovedstaten i {land} er {hovedstad} med {innbyggere} millioner innbyggere')
else:
    svar = input('Landet finnes ikke i databasen. Vil du legge det til? ').strip().lower()
    if svar in ('ja', 'j', 'yes', 'y'):
        
        # La brukeren legge til flere land
        while True:
            nytt_land = input("Skriv inn land, eller skriv 'stopp' for å avslutte: ")
            
            # Bryte løkka hvis brukeren skriver stopp
            if nytt_land.lower().strip() == 'stopp':
                break
            
            hovedstad = input(f'Skriv inn hovedstad til {nytt_land}: ')
            innbyggere = float(input(f'Skriv inn antall innbyggere (i millioner) i {hovedstad}: '))
            
            # Legge til nytt land i databasen
            data[nytt_land] = [hovedstad, innbyggere]
            print(f'{nytt_land} ble lagt til!')
        
        # Printe ut hele databasen
        print('Her er hele databasen:')
        print(data)
        
    else:
        print("Ha en fin dag videre, eller noe sånt.")
    