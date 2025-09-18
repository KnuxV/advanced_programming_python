---
layout: page
title: "Department SQL Class Exercise"
class_number: 3
date: 2025-08-01
difficulty: "Intermediate"
estimated_time: "90 minutes"
topics: ["sql", "python", "data-analysis"]
---

# Department Analytics Practice Exercise

## Context
This exercise uses SQLAlchemy ORM with two database tables representing French administrative data:
- **`Departement`** table: French departments with administrative information
- **`Ville`** table: French cities/communes with population and geographic data

**Prerequisites:** The table classes and database setup can be found in `code-examples/04-class_for_sql/`

---

## Exercises

Answer the following using the two tables (Departement and Ville):

### 1) Top 5 departments by total population

**Objective:** Find departments with the highest total population.

**Calculation:**
```
total_population = sum(population_2012 for all cities in department)
```

**Return:** `department_name`, `department_code`, `total_population`  
**Sort:** By total_population (descending), limit 5

---

### 2) Top 5 most dense departments (population density)

**Objective:** Find departments with the highest population per unit area.

**Calculation:**
```
density = total_population / total_surface
```

Where:
- `total_population = sum(population_2012 for all cities in department)`
- `total_surface = sum(surface for all cities in department)`

**Return:** `department_name`, `department_code`, `density`  
*(optionally include `total_population` and `total_surface` for context)*

**Note:** Handle zero or null surfaces explicitly (exclude or treat as undefined)

---

### 3) Top 5 departments with highest population concentration (HHI)

**Objective:** Measure how concentrated population is within each department using the Herfindahl-Hirschman Index.

**Mathematical Definition:**

For department `Dep` with cities having populations `pop_city`:

**Step 1 - City population share:**
```
share_city = pop_city / pop_department
```

**Step 2 - Herfindahl-Hirschman Index:**
```
HHI(Dep) = sum(share_city² for all cities in Dep)
```

**Step 3 - Scaled version (0-10,000):**
```
HHI_scaled(Dep) = 10,000 × sum(share_city² for all cities in Dep)
```

**Interpretation:**
- HHI = 10,000: Perfect concentration (one city dominates completely)
- HHI → 0: Many cities with equally small individual population shares

**Return:** `department_name`, `department_code`, `HHI_scaled`, `number_of_cities`

**Discussion:** Analyze Paris (department 75) results. Why is its HHI extreme? What does this reveal about population distribution across its cities?

---

## Implementation Tips

1. **Use SQLAlchemy ORM** to join the tables and aggregate data
2. **Handle edge cases** like departments with no cities or zero surface areas
3. **Consider using SQL functions** like `SUM()`, `COUNT()`, and mathematical operations
4. **Test your queries** on a few departments first before running on the full dataset
