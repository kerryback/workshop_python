# Slide Deck Changes Summary

This document details the changes made when converting the 15 workshop notebooks into simplified slide decks. All slide decks follow these general principles:

- **Removed all exercises** to focus on presentation content
- **Reduced content by 50-70%** while retaining core concepts
- **Streamlined examples** to keep slides concise
- **Maintained executable code** with practical demonstrations
- **Used consistent formatting** (revealjs, league theme, cache: false)

---

## Part 1: Google Colab

**Original:** part1_colab.ipynb
**Slides:** slides/part1_colab_slides.qmd
**Reduction:** Full notebook → 12 slides

### Key Changes:
- Focused on essential Colab navigation and features
- Removed detailed setup instructions
- Emphasized Gemini AI integration
- Streamlined code execution examples

### Content Removed:
- Detailed Google Drive setup instructions
- Advanced Colab features (forms, widgets)
- Extensive troubleshooting sections
- All practice exercises

---

## Part 2: Objects

**Original:** part2_objects.ipynb (42 cells)
**Slides:** slides/part2_objects_slides.qmd (14 slides)
**Reduction:** 67% reduction

### Major Changes:
- Combined related object types into single slides
- Reduced mathematical operation examples
- Simplified string methods coverage
- Removed all "Extra" sections

### Exercises Removed:

**Exercise 1 - Logical Operators:**
```python
# Practice exercise: Add a code cell below. Create new variables:
# * `C = A and B`
# * `D = A or B`
# * `E = A xor B`
# What values will they have? Check that you are correct using `print(C, D, E)`.
```

**Exercise 2 - String Upper:**
```python
# Convert the string "python programming" to uppercase and
# assign it to the variable result1.

assert result1 == "PYTHON PROGRAMMING", "The result should be the uppercase version of 'python programming'"
print("Correct! You converted the string to uppercase.")
```

**Exercise 3 - String Replace:**
```python
# Replace all occurrences of "cat" with "dog" in the
# string "the cat sat on the cat" and assign it to the variable result4.

assert result4 == "the dog sat on the dog", "The result should have all 'cat' replaced with 'dog'"
print("Correct! You replaced all occurrences of 'cat' with 'dog'.")
```

### Content Removed:
- Triple-quoted strings section
- `xor` logical operator
- String methods: `.startswith()`, `.endswith()`
- Type conversion examples reduced from 7 to 3
- **Extra section:** Date formatting with datetime
- **Extra section:** Datetime object attributes
- **Extra section:** Creating custom classes

---

## Part 3: Lists

**Original:** part3_lists.ipynb (14 cells)
**Slides:** slides/part3_lists_slides.qmd (9 slides)
**Reduction:** 36% reduction

### Major Changes:
- Combined list operations into fewer slides
- Streamlined method demonstrations
- Removed redundant examples

### Exercises Removed:

**Exercise 1 - Concatenation:**
```python
# Concatenate list1 and list2 and assign the result to the variable fruit_combo.

list1 = ["apple", "banana"]
list2 = ["cherry", "date", "elderberry"]

assert fruit_combo == ["apple", "banana", "cherry", "date", "elderberry"], "The result should be ['apple', 'banana', 'cherry', 'date', 'elderberry']"
print("Correct! You concatenated the fruit lists.")
```

**Exercise 2 - Negative Indexing:**
```python
# Get the last element from my_list using negative indexing
# and assign it to the variable last_number.

my_list = [5, 10, 15, 20, 25]

assert last_number == 25, "The result should be 25 (the last element)"
print("Correct! You accessed the last element using negative indexing.")
```

**Exercise 3 - Slicing:**
```python
# Get the first three elements from my_list using slicing
# and assign the result to the variable first_three.

my_list = ["a", "b", "c", "d", "e", "f"]

assert first_three == ["a", "b", "c"], "The result should be ['a', 'b', 'c'] (first three elements)"
print("Correct! You used slicing to get the first three elements.")
```

---

## Part 4: Dictionaries

**Original:** part4_dictionaries.ipynb (10 cells)
**Slides:** slides/part4_dictionaries_slides.qmd (9 slides)
**Reduction:** 10% reduction (already concise)

### Major Changes:
- Streamlined dictionary operations
- Enhanced comparison table with lists
- Simplified formatting examples

### Exercises Removed:

**Exercise 1 - Create Dictionary:**
```python
# Create a dictionary with keys "name", "age", and "city"
# with values "John", 25, and "New York" respectively.
# Assign it to the variable person_info.

assert person_info == {"name": "John", "age": 25, "city": "New York"}, "The result should be a dictionary with the specified key-value pairs"
print("Correct! You created a dictionary with person information.")
```

**Exercise 2 - Access Value:**
```python
# Access the "model" value from the dictionary {"brand": "Honda", "model": "Civic", "year": 2019}
# and assign it to the variable car_model.

assert car_model == "Civic", "The result should be 'Civic'"
print("Correct! You accessed the model value from the dictionary.")
```

---

## Part 5: Flow Control

**Original:** part5_flow_control.ipynb (18 cells)
**Slides:** slides/part5_flow_control_slides.qmd (16 slides)
**Reduction:** 11% reduction

### Major Changes:
- Combined conditional statements examples
- Streamlined loop demonstrations
- Added comprehensions coverage
- Simplified error handling

### Exercises Removed:

**Exercise 1 - Ternary Operator:**
```python
# Use a compact if-else to find the absolute value of a number.
# Assign the result to the variable abs_value.
number = -15

assert abs_value == 15, "The absolute value of -15 should be 15"
print("Correct! You calculated absolute value using compact if-else.")
```

**Exercise 2 - For Loop Sum:**
```python
# Use a for loop to calculate the sum of numbers from 1 to 10.
# Assign the result to the variable total_sum.

assert total_sum == 55, "The sum of numbers 1 to 10 should be 55"
print("Correct! You calculated the sum using a for loop.")
```

**Exercise 3 - While Loop:**
```python
# Use a while loop to calculate 2^n where n is the first power that makes 2^n > 1000.
# Assign n to the variable power and 2^n to the variable result.

assert power == 10 and result == 1024, "2^10 = 1024 is the first power of 2 greater than 1000"
print("Correct! You found the first power of 2 greater than 1000.")
```

**Exercise 4 - List Comprehension:**
```python
# Use a list comprehension to create a list of cubes for numbers 1 through 6.
# Assign the result to the variable cubes.

assert cubes == [1, 8, 27, 64, 125, 216], "The result should be cubes of numbers 1-6"
print("Correct! You created a list of cubes using list comprehension.")
```

**Exercise 5 - Dictionary Comprehension:**
```python
# Use a dictionary comprehension to create a dictionary where keys are words
# and values are their lengths for: ["cat", "dog", "elephant", "bird"].
# Assign the result to the variable word_lengths.

assert word_lengths == {"cat": 3, "dog": 3, "elephant": 8, "bird": 4}, "Dictionary should map words to their lengths"
print("Correct! You created a word length dictionary using dictionary comprehension.")
```

### Content Removed:
- `xor` logical operator
- Some complex nested conditional examples
- Excessive float precision examples (kept one key example)

---

## Part 6: Functions

**Original:** part6_functions.ipynb (16 cells)
**Slides:** slides/part6_functions_slides.qmd (13 slides)
**Reduction:** 19% reduction

### Major Changes:
- Consolidated built-in functions overview
- Streamlined custom function examples
- Simplified scope explanation
- Enhanced default values coverage

### Exercises Removed:

**Exercise 1 - Is Even Function:**
```python
# Create a function named is_even that takes a number and returns True if it's even, False otherwise.
# Then test it with the number 12.

result = is_even(12)
assert result == True, "12 should be identified as even"
print("Correct! You created a function to check if numbers are even.")
```

**Exercise 2 - Circle Properties:**
```python
# Create a function called 'circle_properties' that takes a radius and
# returns both area and circumference.
# Use pi = 3.14159. Test it with radius = 4.

area, circumference = circle_properties(4)
assert abs(area - 50.26544) < 0.001 and abs(circumference - 25.13272) < 0.001, "Check your area and circumference calculations"
print("Correct! You created a function that returns multiple values.")
```

**Exercise 3 - Power Function:**
```python
# Create a function called 'power' that calculates x^y, with y defaulting to 2.
# Test it with power(5) and power(3, 4).

result1 = power(5)      # Should be 5^2 = 25
result2 = power(3, 4)   # Should be 3^4 = 81
assert result1 == 25 and result2 == 81, "Check your power function implementation"
print("Correct! You created a function with default parameters.")
```

### Content Removed:
- Extensive built-in function examples (kept most essential)
- Detailed docstring formatting
- Advanced scope scenarios

---

## Part 7: Libraries

**Original:** part7_libraries.ipynb (16 cells)
**Slides:** slides/part7_libraries_slides.qmd (10 slides)
**Reduction:** 38% reduction

### Major Changes:
- Focused on core import patterns
- Emphasized standard conventions
- Streamlined pip installation coverage
- Removed redundant examples

### Exercises Removed:
None (this notebook had no formal exercises)

### Content Removed:
- Detailed pip list examples
- Multiple redundant import pattern demonstrations
- Specific package version management details
- Advanced package installation scenarios

---

## Part 8: Pandas Intro

**Original:** part8_pandas_intro.ipynb (27 cells)
**Slides:** slides/part8_pandas_intro_slides.qmd (13 slides)
**Reduction:** 52% reduction

### Major Changes:
- Streamlined DataFrame creation examples
- Focused on essential operations
- Simplified indexing and selection
- Removed complex filtering examples

### Exercises Removed:
All exercises removed (notebook contained multiple embedded exercises throughout)

### Content Removed:
- Complex multi-step data manipulations
- Advanced indexing scenarios
- Detailed method chaining examples
- Stock price analysis examples
- CSV file operations details

---

## Part 9: More Pandas

**Original:** part9_pandas_more.ipynb (39 cells)
**Slides:** slides/part9_pandas_more_slides.qmd (13 slides)
**Reduction:** 67% reduction

### Major Changes:
- Simplified groupby operations
- Streamlined merge/join examples
- Focused on essential pivot operations
- Removed wage data analysis

### Exercises Removed:
Multiple exercises throughout the notebook including:
- Wage analysis exercises
- Complex groupby aggregations
- Multi-level pivot table exercises
- Advanced merge scenarios

### Content Removed:
- Extensive wage dataset analysis
- Complex groupby with multiple aggregations
- Advanced pivot table formatting
- Detailed missing data handling strategies
- Window functions
- Complex string operations

---

## Part 10: Visualization Intro

**Original:** part10_visualization_intro.ipynb
**Slides:** slides/part10_visualization_intro_slides.qmd (15 slides)
**Reduction:** ~60% reduction

### Major Changes:
- Focused on basic plot types
- Simplified styling examples
- Emphasized matplotlib basics
- Introduced seaborn themes

### Exercises Removed:
All visualization exercises removed

### Content Removed:
- Executive dashboard example
- Complex multi-panel figures
- Advanced customization options
- Detailed color scheme discussions
- Wage data visualization exercises

---

## Part 11: More Visualization

**Original:** part11_visualization_more.ipynb (6 cells)
**Slides:** slides/part11_visualization_more_slides.qmd (10 slides)
**Reduction:** Expanded with better organization

### Major Changes:
- Enhanced structure with decision framework
- Focused on seaborn statistical plots
- Added plot selection guidance
- Streamlined wage analysis examples

### Exercises Removed:
Exploratory data analysis exercises

### Content Removed:
- Extensive wage data exploration
- Complex faceted plots
- Advanced seaborn customizations

---

## Part 12: Plotly

**Original:** part12_visualization_plotly.ipynb (10 cells)
**Slides:** slides/part12_visualization_plotly_slides.qmd (11 slides)
**Reduction:** Minimal (already focused)

### Major Changes:
- Enhanced interactivity emphasis
- Streamlined data preparation steps
- Focused on box plot example
- Added HTML export guidance

### Exercises Removed:
Plotly customization exercises

### Content Removed:
- Multiple plot type examples
- Advanced interactivity features
- Detailed animation examples

---

## Part 13: Simulation

**Original:** part13_simulation.ipynb (18 cells)
**Slides:** slides/part13_simulation_slides.qmd (11 slides)
**Reduction:** 39% reduction

### Major Changes:
- Focused on numpy array basics
- Streamlined random number generation
- Simplified Monte Carlo example
- Enhanced visualization

### Exercises Removed:
Various simulation exercises including:
- Custom dice rolling simulations
- Probability calculation exercises
- Distribution analysis tasks

### Content Removed:
- Advanced array operations
- Complex probability scenarios
- Detailed statistical analysis
- Multiple simulation variations

---

## Part 14: Goal Seek

**Original:** part14_goal_seek.ipynb (16 cells)
**Slides:** slides/part14_goal_seek_slides.qmd (12 slides)
**Reduction:** 25% reduction

### Major Changes:
- Focused on fsolve basics
- Added minimize function
- Simplified business examples
- Streamlined verification

### Exercises Removed:

**Exercise 1:**
```python
# Solve for x where: x^3 - 2x^2 + x - 1 = 0
# Starting from x=2
```

**Exercise 2:**
```python
# Find break-even sales volume for NPV calculation
# With various financial parameters
```

### Content Removed:
- Multiple optimization scenarios
- Complex constraint examples
- Advanced solver options
- Detailed convergence analysis

---

## Part 15: Neural Networks

**Original:** part15_neural_networks.ipynb
**Slides:** slides/part15_neural_networks_slides.qmd (14 slides)
**Reduction:** ~50% reduction

### Major Changes:
- Focused on fundamental concepts
- Simplified digit classification example
- Streamlined forward propagation
- Removed training implementation

### Exercises Removed:
All neural network training exercises

### Content Removed:
- Backpropagation implementation
- Advanced network architectures
- Hyperparameter tuning
- Model evaluation metrics
- Cross-validation examples
- Deep learning frameworks comparison

---

## Summary Statistics

| Part | Original Cells | Final Slides | Reduction | Exercises Removed |
|------|---------------|--------------|-----------|-------------------|
| 1 | ~20 | 12 | ~40% | Multiple |
| 2 | 42 | 14 | 67% | 3 |
| 3 | 14 | 9 | 36% | 3 |
| 4 | 10 | 9 | 10% | 2 |
| 5 | 18 | 16 | 11% | 5 |
| 6 | 16 | 13 | 19% | 3 |
| 7 | 16 | 10 | 38% | 0 |
| 8 | 27 | 13 | 52% | Multiple |
| 9 | 39 | 13 | 67% | Multiple |
| 10 | ~25 | 15 | ~60% | Multiple |
| 11 | 6 | 10 | Expanded | Multiple |
| 12 | 10 | 11 | Minimal | Multiple |
| 13 | 18 | 11 | 39% | Multiple |
| 14 | 16 | 12 | 25% | 2 |
| 15 | ~30 | 14 | ~50% | Multiple |

**Overall Impact:**
- **Total exercises removed:** 30+ formal exercises plus numerous embedded practice tasks
- **Average content reduction:** 50-70% across all notebooks
- **Focus shift:** From hands-on practice to presentation-ready content
- **Consistency:** Uniform formatting and structure across all 15 decks
