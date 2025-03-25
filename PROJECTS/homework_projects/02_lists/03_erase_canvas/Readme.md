
# 🎨 Eraser Effect in Pygame

## 🚀 Overview
This project simulates an **eraser effect on a canvas** using **Pygame**.  
The canvas consists of a **grid of blue cells**, and an **eraser (a pink rectangle)** is created.  
When the user **clicks and drags** the eraser, it **removes the blue cells** it touches, creating a **smooth erasing effect**.

---

## 📜 Features
✔ **Interactive Grid-Based Canvas** 🎨  
✔ **Click & Drag Eraser Effect** 🖱️  
✔ **Smooth Performance (60 FPS)** ⚡  
✔ **Uses Pygame for Graphics Rendering** 🕹️  
✔ **Exit via ESC Key or Window Close** ❌  

---

## 🔧 Installation & Setup
### **1️⃣ Install Python**
Ensure you have **Python 3.8+** installed.  
[Download Python](https://www.python.org/downloads/)

### **2️⃣ Install Pygame**
Since this project uses **Pygame**, install it using:
pip install pygame

### **3️⃣ Run the Script**
To start the program, run:
python main.py

## 🎮 How to Use
1️⃣ Click on the window to activate the eraser.
2️⃣ Move your mouse while holding the left-click to erase the blue cells.
3️⃣ Press ESC or close the window to exit.

**🖼️ Example Output**
🎨 Welcome to the Eraser Effect in Pygame! 🎨
🖱️ Click and drag to erase the blue cells.
❌ Press ESC to quit.

## 📌 Code Breakdown
### **1️⃣ Initializing Pygame**
Sets up the Pygame window and canvas size.
Defines the grid (blue cells) and eraser (pink rectangle).

### **2️⃣ Drawing the Grid**
A loop creates 40x40 pixel cells to form the grid.

### **3️⃣ Handling Eraser Movement**
The eraser follows the mouse cursor after clicking.
Any cell touched by the eraser disappears.

### **4️⃣ Event Handling**
The game runs at 60 FPS for a smooth experience.
ESC key or window close stops the game.

## 📜 License
This project is licensed under the MIT License.

## 👨‍💻 Author
Developed by Sahir Ahmed Sheikh 🚀

## ⭐ Support & Contributions
🔹 Found this project useful? Star this repository ⭐
🔹 Want to improve it? Fork & contribute! 🔄