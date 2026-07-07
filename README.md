# 🔐 Password Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OOP-Design-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

<p align="center">
A simple and extensible password generator built with Python using Object-Oriented Programming principles.
</p>


## 🚀 About The Project

**Password Generator** is a Python project designed to create secure random passwords using different generation strategies.

This project demonstrates important Object-Oriented Programming concepts:

- ✅ Abstract Classes
- ✅ Inheritance
- ✅ Polymorphism
- ✅ Encapsulation
- ✅ Clean Code Structure

The architecture is designed so new password generation methods can be added easily without changing the existing code.


---

# ✨ Features

## 🔢 Numeric Password Generator

Generates passwords containing only numbers.

Example:

```
58392017
```

---

## 🔤 Letters Password Generator

Generates passwords containing uppercase and lowercase letters.

Example:

```
aZxQmLpR
```

---

## 🔐 Mixed Password Generator

Generates stronger passwords using:

- Uppercase letters
- Lowercase letters
- Numbers

Example:

```
a7Kp92Lm
```


---

# 🏗 Project Architecture

The project uses an abstract class as the foundation for all password generators.

```
PasswordGeneratorAbstraction
              |
              |
 ┌────────────┼────────────┐
 |            |            |
Numeric     Letters      Mixed
Generator   Generator   Generator
```

The base class defines a common interface:

```python
class PasswordGeneratorAbstraction(ABC):

    @abstractmethod
    def generator(self,length=8):
        pass
```

Each generator implements its own password creation logic.


---

# 📂 Project Structure

```
password-generator/
│
├── password_generator.py
│
└── README.md
```


---

# ⚙️ Installation

Clone this repository:

```bash
git clone https://github.com/hamid3112/password-generator.git
```

Navigate to the project folder:

```bash
cd password-generator
```

Run the application:

```bash
python password_generator.py
```


---

# 💻 Usage

Create a password generator object:

```python
generator = MixedPasswordGenerator()

password = generator.generator()

print(password)
```

Example output:

```
8Fk29LmP
```


You can also customize password length:

```python
password = generator.generator(16)
```

Example output:

```
A7kP92LmX81qZ3wF
```


---

# 🧠 Concepts Used

| Concept | Description |
|---|---|
| Abstract Class | Defines a common structure for all generators |
| Inheritance | Different generators extend the base class |
| Polymorphism | Each generator provides its own implementation |
| Encapsulation | Password generation logic is separated from usage |


---

# 🔮 Future Improvements

Possible future upgrades:

- [ ] Add password strength checker
- [ ] Add graphical user interface (GUI)
- [ ] Add command-line options
- [ ] Add password saving system
- [ ] Add customizable password rules
- [ ] Use cryptographically secure password generation


---

# 🔒 Security Note

This project currently uses Python's `random` module for generating passwords.

For real-world security applications, the `secrets` module is recommended because it is designed for cryptographic purposes.

Example:

```python
import secrets

password = "".join(
    secrets.choice(characters)
    for _ in range(length)
)
```


---

# 👨‍💻 Author

**Hamidreza Miri**

Python Developer | AI & Software Enthusiast

GitHub:

https://github.com/hamid3112


---

⭐ If you find this project useful, consider giving it a star!
