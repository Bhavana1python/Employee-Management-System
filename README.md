The Employee Management System is a Python-based application developed using Object-Oriented Programming (OOP) concepts.
The application allows users to enter and store employee details such as:
------------------------------------------------------------------------
        Employee Number
        Employee Name
        Employee Salary
        Employee Designation
Employee records are stored permanently using Python's Pickle module. Before saving a new employee, the application checks whether the employee number already exists.
Technologies Used:
-----------------
        Python
        Object-Oriented Programming (OOP)
        Pickle
        File Handling
        Exception Handling
        Lists
Features:
--------
        Add new employee records
        Validate employee number uniqueness
        Store employee records in a file
        Read previously stored employee records
        Store employee objects/data using Pickle serialization
        Add multiple employee records
        Prevent duplicate employee numbers
Application Workflow:
--------------------
                                Start
                                  ↓
                                Enter Employee Number
                                  ↓
                                Check Employee Number
                                  ↓
                                Is Number Unique?
                                  ├── No → Display Error
                                  │
                                  └── Yes
                                        ↓
                                Enter Employee Name
                                        ↓
                                Enter Employee Salary
                                        ↓
                                Enter Employee Designation
                                        ↓
                                Create Employee Record
                                        ↓
                                Save Record Using Pickle
                                        ↓
                                Add Another Employee?
                                        ├── Yes → Continue
                                        └── No  → Exit
