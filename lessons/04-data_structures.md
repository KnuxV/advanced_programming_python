# Python Data Structures & Programming Paradigms

## Introduction: Why Data Structure Choice Matters

In data analysis and economics applications, choosing the right data structure can mean the difference between code that runs in seconds versus hours. This session covers Python's core data structures and introduces object-oriented programming concepts that will fundamentally change how you organize and think about your code.

## Part 1: Core Data Structures

### Understanding Mutability: A Fundamental Concept

Before diving into specific data structures, it's crucial to understand the difference between mutable and immutable objects in Python. This distinction affects how your data behaves, how it can be used, and what operations are allowed.

**Immutable objects** cannot be changed after creation. When you perform an operation that seems to modify an immutable object, Python actually creates a new object with the modified value. Numbers, strings, and tuples are immutable. This immutability provides safety: you can pass immutable objects to functions without worrying that the function will change your original data. It also means immutable objects can be used as dictionary keys or stored in sets, since their value won't change unexpectedly. The downside is that any "modification" requires creating a new object, which can be memory-intensive for large data structures.

**Mutable objects** can be modified in place after creation. Lists, dictionaries, and sets are mutable. This allows for efficient modifications since you're changing the existing object rather than creating a new one. However, this flexibility comes with responsibility: when you pass a mutable object to a function, that function can modify your original data. Mutable objects cannot be used as dictionary keys because their value could change, breaking the dictionary's internal organization.

### The Big Four: Lists, Tuples, Dicts, Sets

Python provides four fundamental built-in data structures, each optimized for different use cases:

#### Lists: Ordered, Mutable Sequences
```python
# Lists: Use when you need ordered, changeable data
prices = [100.5, 99.2, 101.3, 98.7]
prices.append(102.1)  # Can modify - adds to the same list object
prices[0] = 100.0     # Can change elements in place
```
**When to use:** Sequential data, when order matters, when you need to modify contents

#### Tuples: Ordered, Immutable Sequences
```python
# Tuples: Use for fixed data that shouldn't change
coordinates = (40.7128, -74.0060)  # NYC latitude, longitude
date_range = ('2024-01-01', '2024-12-31')
# coordinates[0] = 41  # This would raise an error - tuples are immutable!

# If you need to "change" a tuple, you create a new one
new_coordinates = (41.0, coordinates[1])  # Creates entirely new tuple
```
**When to use:** Data that shouldn't change, function returns with multiple values, dictionary keys

#### Dictionaries: Key-Value Mappings
```python
# Dicts: Use for lookups and associations
stock_prices = {
    'AAPL': 150.25,
    'GOOGL': 2750.80,
    'MSFT': 305.15
}
price = stock_prices['AAPL']  # Direct lookup by key
stock_prices['TSLA'] = 890.50  # Can add new entries (mutable)
```
**When to use:** Fast lookups, representing structured data, when you need to access by name/ID

#### Sets: Unique, Unordered Collections
```python
# Sets: Use for unique values and membership testing
traded_symbols = {'AAPL', 'GOOGL', 'MSFT', 'AAPL'}  # Duplicates automatically removed
print(traded_symbols)  # {'AAPL', 'GOOGL', 'MSFT'}

# Fast membership testing
if 'AAPL' in traded_symbols:  # Very fast check
    print("Apple was traded")
```
**When to use:** Removing duplicates, fast membership testing, set operations (union, intersection)

### Data Structure Decision Tree

```
Do I need to preserve order?
├─ NO → Do I need unique values only?
│       ├─ YES → Use SET
│       └─ NO → Do I need key-value pairs?
│               ├─ YES → Use DICT
│               └─ NO → Use LIST (or consider SET for performance)
└─ YES → Can the data be modified after creation?
         ├─ YES → Use LIST
         └─ NO → Use TUPLE
```

### Understanding Performance: Big O Notation

When we talk about performance, we use Big O notation to describe how the time to complete an operation grows as the size of the data increases. Think of it as answering the question: "If I double my data size, how much slower does this operation become?"

**O(1) - Constant Time:** The operation takes the same amount of time regardless of data size. Whether you have 10 items or 10 million items, the operation is equally fast. This is the gold standard for performance. Dictionary lookups and set membership tests achieve this through a technique called hashing.

**O(n) - Linear Time:** The time grows proportionally with the size of the data. If you double your data, the operation takes twice as long. Searching through a list is O(n) because in the worst case, you might need to check every single element to find what you're looking for.

**O(n²) - Quadratic Time:** The time grows with the square of the data size. If you double your data, the operation takes four times as long. Nested loops often create O(n²) complexity. This becomes problematic very quickly with large datasets.

### How Hash Tables Enable O(1) Lookups

Dictionaries and sets achieve their impressive O(1) lookup performance through a clever technique called hashing. Understanding this helps explain both their power and their limitations.

When you store a value in a dictionary or set, Python applies a hash function to convert the key into a number. This number determines where in memory to store the value. Think of it like a library where instead of searching through every book, the call number tells you exactly which shelf to check. When you later want to retrieve that value, Python applies the same hash function to your search key, immediately knowing where to look.

This is why dictionary lookups are so fast: instead of checking every key (like searching through a list), Python computes the hash and jumps directly to the right location. It's also why dictionary keys must be immutable - if a key could change after being stored, its hash would change, and Python would look in the wrong place.

Sometimes two different keys produce the same hash value, called a collision. Python handles this by storing multiple items at the same hash location and doing a small linear search among them. Good hash functions minimize collisions, but even with collisions, the average lookup remains O(1) because collisions are rare and affect only a small number of items.

More details: [here](https://medium.com/@kozanakyel/the-core-of-python-dict-built-in-functions-understanding-hashing-and-collision-resolution-f546c7072fa8)

### Performance Characteristics

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Access by index | O(1) | N/A | N/A |
| Access by key | N/A | O(1) | O(1) |
| Search for value | O(n) | O(1) | O(1) |
| Insert at end | O(1)* | O(1) | O(1) |
| Insert at beginning | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

*Amortized time complexity (occasionally O(n) when the list needs to resize)

### Collections Library: Specialized Tools for Common Patterns

While Python's built-in data structures are powerful, the `collections` module provides specialized structures that elegantly solve common programming patterns. These aren't just convenient - they're optimized implementations that are faster and cleaner than building the same functionality yourself.

#### Counter: Frequency Analysis Made Simple
```python
from collections import Counter

# Without Counter, counting requires manual bookkeeping
transactions = ['buy', 'sell', 'buy', 'buy', 'hold', 'sell']

# The tedious manual way:
freq_manual = {}
for t in transactions:
    if t in freq_manual:
        freq_manual[t] += 1
    else:
        freq_manual[t] = 1

# With Counter - clean and efficient:
freq = Counter(transactions)
print(freq)  # Counter({'buy': 3, 'sell': 2, 'hold': 1})
print(freq.most_common(2))  # [('buy', 3), ('sell', 2)]
```

Counter is invaluable for any frequency analysis: word counts in text analysis, transaction type distributions, or analyzing patterns in time series data. It provides methods like `most_common()` that would require sorting and slicing if done manually.

#### defaultdict: Eliminating Key Existence Checks
```python
from collections import defaultdict

# Without defaultdict, grouping requires constant checking:
trades_manual = {}
trades = [
    ('2024-01-01', 'AAPL', 100),
    ('2024-01-01', 'GOOGL', 50),
    ('2024-01-02', 'AAPL', 150)
]

# The manual way - always checking if key exists:
for date, symbol, volume in trades:
    if date not in trades_manual:
        trades_manual[date] = []
    trades_manual[date].append((symbol, volume))

# With defaultdict - no checking needed:
trades_by_date = defaultdict(list)
for date, symbol, volume in trades:
    trades_by_date[date].append((symbol, volume))
```

defaultdict shines when building nested structures, accumulating values, or grouping data. It eliminates the repetitive "if key not in dict" pattern, making code both faster and more readable.

#### namedtuple: Self-Documenting Data Structures
```python
from collections import namedtuple

# Without namedtuple - using regular tuples:
trade_tuple = ('AAPL', 150.50, 100)
# What does trade_tuple[1] mean? Price? Quantity? You have to remember!

# With namedtuple - self-documenting:
Trade = namedtuple('Trade', ['symbol', 'price', 'quantity'])
trade = Trade('AAPL', 150.50, 100)
print(trade.price)     # Clear what this means
print(trade.quantity)  # No magic index numbers
```

namedtuples provide the memory efficiency of tuples with the readability of classes. They're perfect for simple data records where you want clear, named access to fields without the overhead of a full class.

**Helpful Resources:**
- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity)
- [Collections Module Guide](https://docs.python.org/3/library/collections.html)

## Part 2: Object-Oriented Programming in Python

### Why Classes? Moving Beyond Simple Data Structures

Up until now, you've likely been organizing data using lists, dictionaries, and tuples. This works well for simple data, but as your programs grow more complex, you'll find yourself repeatedly writing similar code to manipulate these structures. Classes solve this problem by bundling data and the functions that operate on that data into a single, reusable unit.

Consider tracking stock portfolios. With just dictionaries and lists, you might have separate functions for buying stocks, selling them, calculating returns, and checking balances. Each function needs to know the exact structure of your data, and if you change that structure, you need to update every function. Classes let you encapsulate all of this complexity in one place, making your code more organized, reusable, and easier to maintain.

The truth is, you've been using classes all along. Every time you call `"hello".upper()` or `[1, 2, 3].append(4)`, you're using methods of the string and list classes. Python's entire object model is built on classes - integers, strings, lists, even functions are all objects created from classes.

### Understanding Classes: Attributes and Methods

A class is like a blueprint that defines two things: **attributes** (data) and **methods** (functions that operate on that data). When you create an object from a class (called instantiation), you get an instance that has its own set of attributes but shares the same methods with all other instances of that class.

```python
class Portfolio:
    """A class to manage a stock portfolio"""
    
    # The __init__ method: The Constructor
    # This special method runs automatically when you create a new Portfolio
    # 'self' refers to the instance being created
    def __init__(self, initial_cash):
        # Attributes: Data stored in the instance
        self.cash = initial_cash          # How much cash we have
        self.holdings = {}                 # Dictionary of stock holdings
        self.transaction_history = []      # List of all transactions
    
    # Methods: Functions that operate on the instance's data
    def buy(self, symbol, quantity, price):
        """Buy stocks if we have enough cash"""
        cost = quantity * price
        if cost <= self.cash:
            self.cash -= cost
            # Update holdings (or add if new symbol)
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            # Record the transaction
            self.transaction_history.append(
                f"Bought {quantity} {symbol} at ${price}"
            )
            return True
        return False
    
    def sell(self, symbol, quantity, price):
        """Sell stocks if we have them"""
        if symbol in self.holdings and self.holdings[symbol] >= quantity:
            self.holdings[symbol] -= quantity
            self.cash += quantity * price
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transaction_history.append(
                f"Sold {quantity} {symbol} at ${price}"
            )
            return True
        return False
    
    def get_value(self, current_prices):
        """Calculate total portfolio value"""
        total = self.cash
        for symbol, quantity in self.holdings.items():
            if symbol in current_prices:
                total += quantity * current_prices[symbol]
        return total
    
    # Special method for string representation
    def __repr__(self):
        return f"Portfolio(cash=${self.cash:.2f}, holdings={self.holdings})"

# Using the class - Creating instances
my_portfolio = Portfolio(initial_cash=10000)  # Create instance with $10,000
my_portfolio.buy(symbol='AAPL', quantity=10, price=150)  # Call methods on the instance
my_portfolio.buy(symbol='GOOGL', quantity=5, price=2800)

# Accessing attributes directly
print(f"Remaining cash: ${my_portfolio.cash:.2f}")
print(f"Holdings: {my_portfolio.holdings}")

# Using methods
current_prices = {'AAPL': 155, 'GOOGL': 2850}
print(f"Total value: ${my_portfolio.get_value(current_prices):.2f}")
```

### The __init__ Method: Object Construction

The `__init__` method is special - it's called a constructor because it constructs new instances of your class. When you write `Portfolio(10000)`, Python creates a new empty Portfolio object and then calls `__init__` with that object as `self` and 10000 as `initial_cash`.

The `self` parameter is how an instance keeps track of its own data. Every method in a class must have `self` as its first parameter (Python passes it automatically). Inside methods, you use `self.attribute_name` to access or modify the instance's attributes. This is how each Portfolio instance can have its own separate cash amount and holdings.

### Why Classes Beat Simple Data Structures

Without classes, managing complex data relationships becomes error-prone:

```python
# Without classes - using dictionaries
portfolio1 = {'cash': 10000, 'holdings': {}}
portfolio2 = {'cash': 5000, 'holdings': {}}

def buy_stock(portfolio, symbol, quantity, price):
    cost = quantity * price
    if cost <= portfolio['cash']:  # Need to remember structure
        portfolio['cash'] -= cost
        if symbol in portfolio['holdings']:
            portfolio['holdings'][symbol] += quantity
        else:
            portfolio['holdings'][symbol] = quantity

# Easy to make mistakes - what if someone passes wrong dictionary structure?
# No validation, no encapsulation, functions scattered everywhere
```

Classes provide structure, validation, and keep related functionality together. They make your code more maintainable and help prevent bugs by ensuring data is always in a valid state.

### Dataclasses: The Modern Python Approach

While traditional classes are powerful, they often require writing repetitive boilerplate code. Python 3.7 introduced dataclasses, which automatically generate common methods like `__init__`, `__repr__`, and `__eq__`. They're perfect for classes that primarily store data with some light methods.

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Trade:
    """A single trade transaction"""
    # Define attributes with type hints
    symbol: str
    quantity: int
    price: float
    timestamp: datetime = datetime.now()  # Default value
    fee: Optional[float] = None  # Optional with default None
    
    # Dataclasses can still have regular methods
    def total_cost(self):
        """Calculate total cost including fees"""
        base_cost = self.quantity * self.price
        return base_cost + (self.fee or 0)
    
    def __post_init__(self):
        """Called after __init__ - useful for validation"""
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.price < 0:
            raise ValueError("Price cannot be negative")

# Using dataclass - much cleaner!
trade = Trade('AAPL', 100, 155.50, fee=9.99)
print(trade)  # Automatically nice string representation
print(f"Total cost: ${trade.total_cost():,.2f}")

# Comparing trades - automatically implements equality
trade2 = Trade('AAPL', 100, 155.50, fee=9.99)
print(trade == trade2)  # True - compares all fields
```

Dataclasses dramatically reduce the amount of code you write while providing type hints, automatic string representation, equality comparison, and more. They're becoming the standard way to create data-holding classes in modern Python.

### Enums: When You Need Named Constants

Sometimes you need to represent a fixed set of values - like trade types (BUY, SELL, HOLD), market states (OPEN, CLOSED, HOLIDAY), or order statuses. Using strings for these is error-prone (typos like "BUUY" cause bugs). Enums provide a type-safe way to define and use named constants.

```python
from enum import Enum, auto

class TradeType(Enum):
    """Types of trades - fixed set of values"""
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"

class MarketState(Enum):
    """Market states using auto() for automatic values"""
    OPEN = auto()      # Automatically assigns 1
    CLOSED = auto()    # Automatically assigns 2
    HOLIDAY = auto()   # Automatically assigns 3

@dataclass
class Order:
    """Combining enums with dataclasses"""
    symbol: str
    quantity: int
    trade_type: TradeType  # Must be a TradeType enum value
    
    def execute(self, price):
        """Execute the order based on type"""
        if self.trade_type == TradeType.BUY:
            return f"Buying {self.quantity} {self.symbol} at ${price}"
        elif self.trade_type == TradeType.SELL:
            return f"Selling {self.quantity} {self.symbol} at ${price}"
        else:
            return f"Holding {self.symbol}"

# Using enums - type safe and clear
order = Order('AAPL', 100, TradeType.BUY)
print(order.execute(150))

# Enums prevent typos and invalid values
# order = Order('AAPL', 100, 'BYU')  # This would cause an error!

# You can iterate over enum values
print("Available trade types:")
for trade_type in TradeType:
    print(f"  - {trade_type.name}: {trade_type.value}")

# Check market state
current_state = MarketState.OPEN
if current_state == MarketState.OPEN:
    print("Market is open for trading")
```

Enums make your code more robust by ensuring only valid values are used. They're self-documenting (the valid options are clear from the enum definition), provide IDE autocomplete support, and prevent the subtle bugs that come from typos in string constants.

## Summary

Understanding Python's data structures and object-oriented programming opens up new ways to organize and think about your code:

1. **Mutability matters**: Immutable objects (tuples, strings) provide safety but require creating new objects for changes. Mutable objects (lists, dicts) allow in-place modifications but require careful handling.

2. **Performance is predictable**: Dictionary and set lookups are O(1) thanks to hash tables, while list searches are O(n). Choose your data structure based on your access patterns.

3. **Collections solve common patterns**: Counter for frequencies, defaultdict for grouping, namedtuple for simple records - these tools make your code cleaner and faster.

4. **Classes organize complexity**: By bundling data with the methods that operate on it, classes make complex programs manageable and reusable.

5. **Modern Python provides shortcuts**: Dataclasses eliminate boilerplate while providing useful features. Enums ensure type safety for fixed sets of values.

The key insight is that these aren't just programming concepts - they're tools for modeling the complex data relationships you encounter in economics and data analysis. A Portfolio isn't just a dictionary with some functions; it's an object with specific behaviors and constraints. A Trade isn't just a tuple of values; it's a structured record with validation and methods. This shift in thinking - from data and functions to objects with behavior - is what makes object-oriented programming so powerful for building larger, more maintainable systems.

**Helpful Resources:**
- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
- [Enum Documentation](https://docs.python.org/3/library/enum.html)
- [Real Python OOP Guide](https://realpython.com/python3-object-oriented-programming/)