# Caesar Cipher Encryption

## 📝 Description
This is a simple implementation of the Caesar Cipher encryption algorithm in Python. The program shifts each letter in the input text by one position in the alphabet to create an encrypted message.

## 👩‍💻 Author
Created by [Nagham Sabry](https://github.com/NaghamSabry)

## 🔐 How It Works
The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet. In this implementation:
- Each letter is shifted by *1 position* forward
- 'a' becomes 'b', 'b' becomes 'c', and so on
- 'z' wraps around to 'a'
- 'Z' wraps around to 'A'
- Spaces and non-alphabetic characters remain unchanged

## 💻 Usage

### Running the Program
python
python caesar_cipher.py


### Example

Input: Hello World
Output: Ifmmp Xpsme



Input: xyz
Output: yza


## 🛠 Code Features
- Handles both uppercase and lowercase letters
- Preserves spaces and special characters
- Wraps 'z' to 'a' and 'Z' to 'A'
- Simple and easy to understand implementation

## 📋 Requirements
- Python 3.x

## 🔄 How to Modify the Key
To change the shift value, modify the key variable:
python
key = 1  # Change this to any number for different shift values


## ⚠ Note
This is a basic encryption method and should *not* be used for securing sensitive information. It's primarily for educational purposes and understanding encryption concepts.

## 📚 Learning Resources
- [Caesar Cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- Learn more about cryptography basics

## 🤝 Contributing
Feel free to fork this project and suggest improvements!

## 📄 License
Open source - feel free to use and modify

---

Made with ❤ by [Nagham Sabry](https://github.com/NaghamSabry)
