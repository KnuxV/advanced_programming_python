
# Joke Generator Pull Request Exercise

## Team Setup (2 people)
- **Person A**: Repository Owner & Developer
- **Person B**: Contributor & Developer

## Phase 1: Initial Setup (Person A - 5 minutes)

**Create a new GitHub repository:**
- Name: `joke-generator-[your-names]` 
- Make it public, initialize with README

**Create the base `joke_generator.py`:**
```python
import random

# Initial joke collection
jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

def print_random_joke():
    """Print a random joke from the collection."""
    joke = random.choice(jokes)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()
```

**Commit and push to GitHub**

**Share repo URL with Person B**

## Phase 2: Parallel Development - Merge Conflict Time! (10 minutes)

### Person A: Add Dad Jokes Feature
1. **Create branch:** `git switch -c add-dad-jokes`
2. **Your mission:**
   - Add a new list of dad jokes (blagues de papa) in French (go online to find some, or AI whatever)
   - Modify `print_random_joke()` to randomly pick from both programming and dad jokes
   - Test that it works
3. **Commit and push the branch**
4. **Merge the branch back to main**

### Person B: Add Joke Categories Feature  
1. **Fork the original repository**
2. **Clone your fork locally**
3. **Create branch:** `git switch -c add-joke-categories`
4. **Your mission:**
   - Modify `print_random_joke()` to accept a category parameter
   - Add category labels to the output (like `[PROGRAMMATION]`)
   - Update the main section to specify which category you're showing
   - Test that it works
5. **Commit and push the branch**
6. **Create Pull Request**

## Phase 3: Merge Conflict Resolution (10 minutes)

**Person A:**
1. **First merge your own branch** directly:
   ```bash
   git switch main
   git merge add-dad-jokes
   git push origin main
   ```
2. **Now try to merge Person B's PR** - CONFLICT! 💥

**Both people work together to:**
1. **Understand what each version does**
2. **Decide how to combine both features**
3. **Resolve the conflict** to support both dad jokes AND categories
4. **Test the final solution**

**Target result:** A function that can handle both joke collections AND category filtering.

## Phase 4: Next Development Cycle (10 minutes)

Now, that you have made the first merge conflicts, you can try both add more features to the code and merge them again together. or work together on another project.
