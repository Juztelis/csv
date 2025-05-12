import csv

def dicCSV():
    with open('csv_python/failas.csv', 'r', encoding='utf-8') as f, \
         open('csv_python/result.csv', 'w', encoding='utf-8', newline='') as result_file:

        reader = csv.DictReader(f)
        writer = csv.writer(result_file)
        writer.writerow(['vardas', 'vidurkis'])

        for row in reader:
            paz = [row['paz1'], row['paz2'], row['paz3'], row['paz4']]
            inte = [int(x) for x in paz]
            avrg = sum(inte) / len(inte)
            vardas = row['vardas']
            writer.writerow([vardas, round(avrg, 2)]) #round suapvalina, tai siuo atveju iki 2 skaiciu po kab.

dicCSV()
