with open('shopping.txt', 'a') as shop:
  shop.write('Tomatoes, cucumbers, celery\n')

with open('diary.txt','w') as diary:
  diary.write('Special events for today')

with open('lines.txt') as file_object:
  file_data = file_object.readlines()
print(file_data)

for line in file_data:
  print(line)

with open('mystery.txt') as text_file:
  text_data = text_file.read()
print(text_data)

# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
    fieldnames = ['name', 'type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
    writer.writerow({'name': 'Google', 'type': 'Search'})
