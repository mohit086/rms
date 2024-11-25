# Restaurant Management System

A Command-Line Interface (CLI) application for managing restaurant operations, built with Python and MySQL. The application supports two user roles (**Admin** and **Employee**) and offers the following features:

## Features

1. **Menu Management**:
   - View menu items.
   - Add, update, or remove menu items.

2. **Order Management**:
   - Create new orders.
   - View order details.

3. **Bill Management**:
   - Generate bills for orders.
   - View bill details.
   - Mark bills as paid.

4. **Employee Management** (Admin Only):
   - Add new employees.
   - Update employee details.
   - Remove employees.
   - View a list of all employees.

5. **Authentication**:
   - Role-based access for admins and employees.

---

## Design Patterns Used

- **Model-View-Controller (MVC)**:
  - **Models** (`models` directory): Represents the data structures (e.g., `User`, `Order`, `MenuItem`, `Bill`).
  - **Services** (`services` directory): Contains business logic for interacting with the database.
  - **CLI** (`main.py`): Acts as the controller to handle user inputs and interact with services.

- **Repository Pattern**:
  - `db_connection.py`: Encapsulates database operations, providing an abstraction over direct SQL queries.

- **Factory Pattern**:
  - Used implicitly in the `models` directory for creating instances like `Admin` and `Employee`.

- **Singleton Pattern**:
  - The **database connection** is implemented as a Singleton, ensuring a single connection is reused throughout the application.

---

## Steps to Run the Application

### 1. Prerequisites

Ensure the following software is installed:
- **Python 3.8+**
- **MySQL**
- **MySQL Connector for Python**  
  Install it using pip:  
  ```bash
  pip install mysql-connector-python
---

### 2. Set Up the Database

1. Create a MySQL database named `restaurant`:
```bash
   mysql -u root -p
   CREATE DATABASE restaurant;
```

Use `root` as the username and `admin` as the password.

2. Navigate to the `database` directory and execute the SQL scripts:
```bash
    cd database/
    mysql -u root -p restaurant < database.sql
    mysql -u root -p restaurant < dummy_data.sql
```

### 3. Run the Application

Navigate to the `src` directory and start the application:
```bash
    cd src/
    python3 main.py
```

Follow the on-screen instructions for login and using the CLI.

  1. **Admin Access**
     * **Username**: `admin1`
     * **Password**: `admin123`

  2. **Employee Access**
     * **Username**: `employee1`
     * **Password**: `employee123`

### 4. Run the Unit Tests

Navigate to the root directory of the project and run the following command:
```bash
python3 -m unittest discover -s tests
```

This will discover and run all the unit test files located in the `tests/` directory. Each test file checks the functionality of different parts of the application, including models and services.

## Commands Summary

| Action              | Command                                                       | Directory                  |
|---------------------|---------------------------------------------------------------|----------------------------|
| Create Database     | `CREATE DATABASE restaurant;`                                 | MySQL CLI                  |
| Run `database.sql`  | `mysql -u root -p restaurant < database.sql`                  | `database/`                |
| Run `dummy_data.sql`| `mysql -u root -p restaurant < dummy_data.sql`                | `database/`                |
| Run Application     | `python3 main.py`                                             | `src/`                     |
| Run Tests           | `python3 -m unittest discover -s tests`                       | Project Root (`./`)        |


## Authors
- IMT2022003 Ritish Shrirao
- IMT2022076 Mohit Naik
- IMT2022086 Ananthakrishna K
- IMT2022103 Anurag Ramaswamy