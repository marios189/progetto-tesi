import csv

def duplicates_deletion(file_input, file_output):
    try:
        with open(file_input, newline='') as input_file:
            reader = csv.reader(input_file)
            righe_uniche = set()

            for riga in reader:
                righe_uniche.add(tuple(riga))

        with open(file_output, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            
            for riga_unica in righe_uniche:
                writer.writerow(riga_unica)

    except FileNotFoundError:
        print(f"Errore: Il file {file_input} non esiste.")

input_file = 'file_input.txt'
output_file = 'file_output.txt'
duplicates_deletion(input_file,output_file)