### *README – PR.7 Multi-Utility Toolkit*

*Practical Title:* Modules and Packages in Python  
*Course:* PR.7 Moduler & Packager  
*Language:* Python 3.x  

#### *1. Aim*
To understand and implement Python modules and packages by building a menu-driven Multi-Utility Toolkit that uses built-in modules and a custom module for file operations.

#### *2. Description*
The program is a console-based toolkit with 7 main options. Each option uses a different Python module to perform real-world tasks. The toolkit demonstrates module import, function usage, and package structure.

#### *3. File Structure*
PR7_Project/
│
├── multi_toolkit.py   # Main program with menus
└── project7.py        # Custom module for file operations
#### *4. Modules Used & Functions*
Menu Option | Module Used | Purpose
**1. Datetime and Time Operations** | `datetime`, `time` | Get current date/time, calculate date difference, format dates, stopwatch, countdown timer
**2. Mathematical Operations** | `math` | Factorial, compound interest, trigonometry, area of circle using `math.factorial()`, `math.pi`, `math.sin()`, etc.
**3. Random Data Generation** | `random`, `string` | Generate random numbers, lists, passwords, OTPs using `random.randint()`, `random.choice()`, `string.ascii_letters`
**4. Generate UUID** | `uuid` | Generate unique identifiers using `uuid.uuid4()`
**5. File Operations** | `file_ops.py` | Custom module with functions: `create_file()`, `write_file()`, `read_file()`, `append_file()`
**6. Explore Module Attributes** | `dir` / `__import__` | Dynamically import any module and display its attributes using `dir()`
**7. Exit** | - | Exit the program
#### *5. Key Concepts Demonstrated*
1. *Built-in Modules*: Importing and using `datetime`, `math`, `random`, `uuid` without installation.
2. *Custom Module*: Creating `file_ops.py` and importing it in the main file. This shows how to split code into reusable files.
3. *Dynamic Import*: Using `*import*()` to load a module at runtime and `dir()` to inspect it.
4. *Menu-Driven Programming*: Using `while` loops and `if-elif` to create interactive menus.
5. *Date/Time Handling*: Parsing and formatting dates with `strptime()` and `strftime()`.
6. *Exception Handling*: Basic `try-except` in file reading to handle missing files.

#### *6. How to Run*
1. Place both `multi_toolkit.py` and `project.py` in the same folder.
2. Open terminal/command prompt in that folder.
3. Run:
python multi_toolkit.py
4. Use the menu to test each function.

#### *7. Sample Output*
*Datetime Menu:*
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days
*Random Password:*
Enter password length: 8
Generated Password: Kd8@qzP!
*File Operations:*
Enter file name: example.txt
File created successfully!
#### *8. Learning Outcomes*
After this practical, you will be able to:
- Create and use custom modules in Python.
- Import and use built-in modules effectively.
- Use `dir()` to explore any module’s functions and attributes.
- Apply modules to solve real problems like date calculation, file handling, and random data generation.

