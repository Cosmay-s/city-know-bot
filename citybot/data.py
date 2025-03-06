import copy

alphabet_dict = {
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
    dictionary = copy.deepcopy(alphabet_dict)
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            city = line.strip()
            if city:
              dictionary[city[0].lower()].append(city)
    return dictionary