
cities = {
  "а": [],
  "б": [],
  "в": [],
  "г": [],
  "д": [],
  "е": [],
  "ё": [],
  "ж": [],
  "з": [],
  "и": [],
  "й": [],
  "к": [],
  "л": [],
  "м": [],
  "н": [],
  "о": [],
  "п": [],
  "р": [],
  "с": [],
  "т": [],
  "у": [],
  "ф": [],
  "х": [],
  "ц": [],
  "ч": [],
  "ш": [],
  "щ": [],
  "ы": [],
  "э": [],
  "ю": [],
  "я": [],
}



    
def load_cities(file):
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            city = line.strip()
            if city:
                 cities[city[0].lower()].append(city)


load_cities('cities-russia.txt')
print(cities)
