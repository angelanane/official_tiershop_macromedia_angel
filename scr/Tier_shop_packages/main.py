# Das importieren der schon gespeicherten json Daten sowie die schon geschiebenen Klassen in drei verschiedenen dateien
import json
from bird import Bird
from cat import Cat
from dog import Dog

# Das aufrufen der bestimmten Json Datei
def load_animals():
    with open("the_animals.json") as file:
        animals_data = json.load(file)

# Das inizialisieren sowie das morphen der drei json Dateien in comprehension Listen
# wandel des Wörterbuches als Argument 

    birds_data = animals_data["birds"]
    birds = [Bird(**bird_data) for bird_data in birds_data]

    cats_data = animals_data["cats"]
    cats = [Cat(**cat_data) for cat_data in cats_data]

    dogs_data = animals_data["dogs"]
    dogs = [Dog(**dog_data) for dog_data in dogs_data]

    return birds, cats, dogs

# Zuweisung der der animal Objekte 
# Durch den f'sttring, eine formatierte wiedergabe
def print_animal_names_ids(animals):
    for animal in animals:
        print(f"Name: {animal.name}, ID: {animal.id}")

# Ist für die suche eines Tieres durch name oder der ID. Nach dem finden des gesuchten Objekts, wwerden all ihrere Atributten zurückkehren     
def search_animal_by_name(animals):
    search_name_or_id = input("Enter the name or ID of the animal you want to search: ")
    
# Erstellung einer leeren liste für das gesuchte Objekt der Tiere
    found_animals = []
# in der Datei animals wird die klasse Animal gesucht

    for animal in animals:
        
# stimmen die ID oder der Name des Tieres mit einander ein bzw es exestiert eine die übereinsteht, dann wurde es gefunden
        if animal.name == search_name_or_id or animal.id == search_name_or_id:
            found_animals.append(animal)

# nach dem es gefunden würde, werden all ihre Attributen zurück gegeben für den Kunden, die schon in dem packet geschrieben würden ist     
    
    if found_animals:
        print(    )
        print(f"Found {len(found_animals)} animals matching '{search_name_or_id}':")
        for animal in found_animals:
            print("Animal Details:")
            print(f"ID: {animal.id}")
            print(f"Name: {animal.name}")
            print(f"Weight: {animal.weight}")
            print(f"Height: {animal.height}")
            print(f"Color: {animal.color}")
            print()  
# gibt es diese ID oder Name nicht dan printet es dies aus.    
    else:
        print(f"No animals found matching '{search_name_or_id}'.")

# Aufruf der main Funktion und vorgeschiebender zugriff auf bird, cat und dog
def main():
    birds, cats, dogs = load_animals()
# Kunde kommt ins spiel, durch den Namen in den input

    customer_name = input("Welcome to the Eden's Creatures animal Shop! We would love to know your name? ") 
    print("______________________________________________________________________________________________________")
    print(f"Thank you so much, {customer_name}, for being a new or another pet parent")
    print("               ")
# Eine leere liste für die gekauften Tiere
    bought_animals = []

    
# Eine Dauerschleife durch die While True um die anwendung der Option wieder zu wählen bis man genug hat 



# Optionen sind: ein Tier kaufen, ein tier suchen (grade für die mitarbeiter) oder verlassen nach oder vor den kauf
    while True:
        print("                    *Please select one of these option and write their number:")
        print("        ")
        print("______________________________________________________________________________________________________")
        print('  -----Tipp: Search first what pet between Dog, Cat and Bird you want, before you buy your new pet-----')
        print("______________________________________________________________________________________________________")
        print(     )
# Hier selektiert der Kunde was er genau von den Laden möchte
        print("1. Buy my new pet")
        print("2. Search for my potential pet by name or ID")
        print("3. I am Finished")
        print(    )
        option_choice = input("Enter your choice (1-3): ")

# Mit der if teilen wir die 3 Optionen mit Anweisungen
# Bei Punkt 1 wählt der Kunde das kaufen eines Tieres mit der 1 und muss wieder wählen welches es sein soll 
        
        if option_choice == "1":
            print("Please select an animal:")
            print("1. My new Dog")
            print("2. My new Cat")
            print("3. My new Bird")
            print()
# Die Eingabe der auswähl von Punkt 1
            animal_choice = input("Enter your choice for your new Pet (1-3): ")
# None ist ein Schlüsselwort um eine Nullvariable oder ein Objekt zu definieren            
            animal = None
    
# Nun die option 1-2-und 3 in 1    
            if animal_choice == "1":
                print("The available Dogs:")
                print()
                print_animal_names_ids(dogs)

                dog_id = input("Enter the ID of your potentialy new dog, that you want to buy: ")
                print()

# Hier wird in der Liste nach einen Hund in dogs gesucht der genau dem hunde id entspricht und wird 'gekauft'.
# Mit der next Funktion wird das nächste Objekt gesucht  
# Ist da keins das übereinstimmt, wird es auf None gesetzt
                animal = next((dog for dog in dogs if dog.id == dog_id), None)

            elif animal_choice == "2":
                print("Available Cats:")
                print()
                print_animal_names_ids(cats)

                cat_id = input("Enter the ID of your potentialy new cat, that you want to buy: ")
                print()
# Hier wird in der Liste nach einer Katze in katze gesucht der genau der Katzten id entspricht.
# Ist da keins das übereinstimmt, wird es auf None gesetzt               
                
                animal = next((cat for cat in cats if cat.id == cat_id), None)

            elif animal_choice == "3":
                print("Available Birds:")
                print()
                print_animal_names_ids(birds)

                bird_id = input("Enter the ID of your potentialy new Bird, that you want to buy: ")
                print()
# Hier wird in der Liste nach einem Vogel in Vogel gesucht der genau dem Vogel id entspricht.
# Ist da keins das übereinstimmt, wird es auf None gesetzt                
                
                animal = next((bird for bird in birds if bird.id == bird_id), None)
# Wird ein tier schon'gekauft' bzw ist in der Liste bought_animals printet es das, da es schon in der Liste eingespeichert würde:
            if animal:
                if animal in bought_animals:
                    print()
                    print("Oh, it seems like this pet has already been bought by you or someone who couldnt wait to be a new pet owner.")
                    print("Please choose another potentially pet, that you may want to buy.")
                    print()
                    continue

                bought_animals.append(animal)
                print(f"Choosen animal: {animal.id}, Name: {animal.name}, Race: {animal.race}, Price: {animal.price} Euro")
                print("  ")

# alles weitere wird als nicht gültig angesehen
            else:
                print("Invalid animal ID. Please try again.")
                continue
# Bei der zweiten werden die gesuchten Tiere je nach Zahl gesucht und durch die Funktion search_animal_by_name() aufgerufen.
# Dies ist in ab Zeile 33-61
        elif option_choice == "2":
            print("Search and find out what your new pet might look like by name or ID:")
            print("1. Search among dogs")
            print("2. Search among cats")
            print("3. Search among birds")
            print()

            animal_type_choice = input("Enter your choice please (1-3): ")
# je nach Option werden alle Attributen aus der Json wiedergegeben
            if animal_type_choice == "1":
                print("Available Dogs:")
                print()
                print_animal_names_ids(dogs)
                print()

                print("Searching among dogs:")
                search_animal_by_name(dogs)

            elif animal_type_choice == "2":
                print("Available Cats:")
                print()
                print_animal_names_ids(cats)
                print()

                print("Searching among cats:")
                search_animal_by_name(cats)

            elif animal_type_choice == "3":
                print("Available Birds:")
                print()
                print_animal_names_ids(birds)
                print()

                print("Searching among birds:")
                search_animal_by_name(birds)

# Alles weitere ist ungültig 
            else:
                print("Invalid animal type choice. Please try again.")

# Nun die lezte Option, was für den Ausgang gedacht ist je nach Kauf oder Suche
        elif option_choice == "3":
            print("Wow, thank you for giving it a new family.")
# Nun zu den Kassenbon            
            receipt = input("Would you like to receive a receipt? (yes/no): ")
# Ist die antwort ja werden die Objekte der liste bought_animals zurück gegeben.             
            if receipt.lower() == "yes":
                print("                           -------------------------------")
                print("                                 Generating receipt...")
                print("                           -------------------------------")
                print()
                print("Your Eden Receipt:")
                print()
# Hier wird das ausgegebene Preis wiedergegeben und müss zuvor auf null gesetzt werden                 
                total_price = 0
# Die Rückgabe der Daten aus der Liste bought_animals
                for animal in bought_animals:
                    print(f"Your new Pet: {animal.id}, Name: {animal.name}, Race: {animal.race}, Price: {animal.price} Euro")
# Der totale Preis ergibt sich durch die Addition der Tierpreise der bought_animal
                    total_price += animal.price

                print(f"Your total Price: {total_price} Euro")
            else:
                print(f"Thank you so much, {customer_name}, for buying or looking from / for Eden's Creatures animal Shop. Hope to see you soon!")

            break
# Somit wird durch die main alles gestartet, und sie können einen neuen Haustier kaufen
if __name__ == "__main__":
    main()
