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
$$\text{total\_population} = \sum_{\text{cities in dept}} \text{population\_2012}$$

**Return:** `department_name`, `department_code`, `total_population`  
**Sort:** By total_population (descending), limit 5

---

### 2) Top 5 most dense departments (population density)

**Objective:** Find departments with the highest population per unit area.

**Calculation:**
$$\text{density} = \frac{\text{total\_population}}{\text{total\_surface}}$$

Where:
- $\text{total\_population} = \sum_{\text{cities in dept}} \text{population\_2012}$
- $\text{total\_surface} = \sum_{\text{cities in dept}} \text{surface}$

**Return:** `department_name`, `department_code`, `density`  
*(optionally include `total_population` and `total_surface` for context)*

**Note:** Handle zero or null surfaces explicitly (exclude or treat as undefined)

---

### 3) Top 5 departments with highest population concentration (HHI)

**Objective:** Measure how concentrated population is within each department using the Herfindahl-Hirschman Index.

**Mathematical Definition:**

For department $Dep$ with cities $city \in Dep$ having populations $pop\_city$:

**City population share:**
$$share\_city = \frac{pop\_city}{pop\_dep}$$

**Herfindahl-Hirschman Index:**
$$HHI(Dep) = \sum_{city \in Dep} share\_city^2$$

**Scaled version (0-10,000):**
$$HHI_{\text{scaled}}(Dep) = 10,000 \times \sum_{city \in Dep} share\_city^2$$

**Interpretation:**
- HHI = 10,000: Perfect concentration (one city dominates)
- HHI → 0: Many cities with small individual shares

**Return:** `department_name`, `department_code`, `HHI_scaled`, `number_of_cities`

**Discussion:** Analyze Paris (department 75) results. Why is its HHI extreme? What does this reveal about population distribution across its cities?