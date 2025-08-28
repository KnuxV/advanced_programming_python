# Countries API Exercise - Building a Country Class

## 🎯 Goal: Object-Oriented Data Processing

### Why Create a Class?

**Encapsulation & Abstraction:** Instead of working with messy dictionaries full of nested data, we create a clean `Country` object that's easy to understand and manipulate.

```python
# Instead of this mess:
country_dict['capitalInfo']['latlng'][0]  # Latitude? Longitude? Confusing!

# We get this:
country.capital_lat  # Crystal clear!
```


**Encapsulation & Abstraction:**

The idea is to **hide complexity** and **simplify the interface**.

The API returns a big dictionary with lots of nested data and weird field names. Instead of remembering that the capital's latitude is `data['capitalInfo']['latlng'][0]`, you create a `Country` object where it's simply `country.capital_lat`.

**Encapsulation** = wrapping/hiding complicated technical details  
**Abstraction** = creating a simple, intuitive interface

In practice:
- Instead of manipulating `{'name': {'common': 'France'}, 'capitalInfo': {'latlng': [48.8566, 2.3522]}}` 
- You manipulate a `Country` object with `country.name` and `country.capital_lat`

It's like having a TV remote - you press "volume +", you don't think about the electronic circuits behind it. The `Country` class is your "remote control" for country data. You custom it once to your needs and then you can manipulate the data without thinking about the technicalities.

**Result:** More readable code, fewer errors, easier to use and maintain.
Classes let us transform raw API data into intuitive, reusable objects with useful methods.

## 🌍 The REST Countries API
We'll use this API that provides information about countries.

**Base URL:** `https://restcountries.com/v3.1/`

### Key Endpoints:
- `GET /name/{countryName}` - Search by country name
- `GET /capital/{capitalName}` - Search by capital city

### Quick Test:
```python
import requests

# Get France data
response = requests.get("https://restcountries.com/v3.1/name/france")
france_data = response.json()[0]  # API returns a list, take first result
print(france_data.keys())  # See all available attributes
```

**Important:** Query countries **one by one** to avoid overloading the API when __testing__. Don't use `/all` endpoint until your code works.

## 🏗 Your Task: Build the Country Class

### Step 1: Create the Basic Class

You need to create a `Country` class that simplifies the API data. The API returns complex nested dictionaries - your job is to extract and simplify the useful information.

**Key simplifications to make:**
- `name['common']` → `name` (simple string)
- `capitalInfo['latlng']` → `capital_lat`, `capital_lon` (separate float attributes)
- `capital[0]` → `capital` (first capital as string)
- Keep: `population`, `area`, `region`, `borders`, `landlocked`

```python
class Country:
    def __init__(self, api_data):
        # Extract and simplify the essential data we want
        self.name: str = # TODO: Extract from api_data
        self.code: str = # TODO: Extract country code (cca2)
        self.population: int = # TODO: Extract population
        self.area: float = # TODO: Extract area
        self.region: str = # TODO: Extract region
        self.capital: str = api_data['capital'][0] if api_data.get('capital') else "N/A"
        
        # Simplify capital coordinates
        if 'capitalInfo' in api_data and 'latlng' in api_data['capitalInfo']:
            coords = api_data['capitalInfo']['latlng']
            self.capital_lat: float = coords[0]
            self.capital_lon: float = coords[1]
        else:
            self.capital_lat, self.capital_lon = 0.0, 0.0
        
        # Other useful attributes
        self.borders: list = # TODO: Extract borders list (or empty list if missing)
        self.landlocked: bool = # TODO: Extract landlocked status
        self.languages: list = # TODO: Convert languages dict to list of values
```

### Step 2: Implement `__repr__` Method

**Question:** What is `__repr__` and why do we need it?

`__repr__` defines how your object appears when printed. Without it:
```python
print(france)  # Output: <__main__.Country object at 0x7f8b8c0d5f40> - useless!
```

With `__repr__`:
```python
def __repr__(self):
    # self is the current Country object - use self.attribute_name to access data
    # __repr__ is a special method that controls what is printed
    pass

print(france)  # Output: France (67,391,582 people, 551,695 km²) - useful!
```

Implement a clean `__repr__` that shows the most important country information of your choice.

## 🧮 Methods to Implement

### 1. Capital Distance Calculator

Calculate the distance between two countries' capitals using the **Haversine formula** ([implementation here for example](https://www.geeksforgeeks.org/dsa/haversine-formula-to-find-distance-between-two-points-on-a-sphere/)):

```python
def capital_distance(self, other_country: 'Country'):
   """Calculate distance between capitals in kilometers"""
   # self = this country, other_country = the country to compare with
   # Use self.capital_lat, self.capital_lon and other_country.capital_lat, other_country.capital_lon
   # Apply the Haversine formula provided above
   pass

# We then could compare like so:
france: Country = Country(france_data)
germany: Country = Country(germany_data)
france.capital_distance(germany)  # We call the method of the class Country for the instance france
```

### 2. Population Density

```python
def density(self):
    """Population density (people per km²)"""
    # Implement this - handle division by zero!
    pass
```

### 3. Border Analysis

```python
def are_neighbors(self, other_country):
    """Do these countries share a border?"""
    # Check if other_country's code is in self.borders list
    pass

def common_neighbors(self, other_country) -> list[Country]:
    """Return list of shared neighbor country codes"""
    # Use set intersection between self.borders and other_country.borders
    # then query the API again to retrieve the country that have the codes
    # and return a list of Countries 
    # Example: borders: ['DZA', 'LBY'] and ['DZA', 'NER'] → common: ['DZA']
    pass

france: Country = Country(france_data)
germany: Country = Country(germany_data)
shared_neighbors = france.common_neighbors(germany)  # Returns list of Country objects
for neighbor in shared_neighbors:
   print(neighbor)  # this would print "Belgium (Brussels)", "Luxembourg (Luxembourg)", "Switzerland" (Bern) depening on your implementation of __repr__
```

## ⚖️ Comparison Methods with `__lt__`

**Question:** What is `__lt__` and how does it enable sorting?

`__lt__` (less than) is a special method that tells Python how to compare two objects:  
You can see how to implement it on [geeksforgeeks](https://www.geeksforgeeks.org/python/python-__lt__-magic-method/)

```python
def __lt__(self, other):
    """Define how to compare countries - YOU IMPLEMENT THIS"""
    # Your code here - compare by population
    # What should happen if populations are equal?
    pass

# Once implemented, you can perform sorting and max on your countries:
countries = [france, germany, italy]
sorted_countries = sorted(countries)  # This will sort the countries by population 
biggest_country = max(countries)      # This will return the country with the highest pop (germany)
```

**Your task:** 
1. Implement `__lt__` to compare countries by population
2. **Challenge:** What happens if two countries have the same population? How do you break ties? (Hint: use a second criterion like area, name)

**End use:** This enables automatic sorting and comparison of Country objects using Python's built-in functions like `sorted()`, `max()`, `min()`.


## 📤 Submission

**Fork the repository first**, then push your answers to the course website on a branch named `corrections`:

```bash
git switch -c corrections
git add your-notebook.ipynb
git commit -m "Countries API exercise"
git push origin corrections.
```

**Create a Pull Request:**
Once pushed, go to GitHub and create a Pull Request from your corrections branch to the main repository. This allows for code review and feedback on your implementation.

## 🎯 Learning Objectives

By completing this exercise, you'll understand:
- How to transform raw API data into clean, usable objects
- The power of encapsulation (hiding complexity behind simple interfaces)
- How special methods like `__repr__` and `__lt__` make objects more Pythonic
- Practical API consumption patterns for real-world projects

Good luck! 🚀