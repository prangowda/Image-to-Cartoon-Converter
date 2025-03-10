# 🖼️ Image to Cartoon Converter  
🚀 A Python-based tool that converts real images into cartoon-style images using **OpenCV and NumPy**.

---

## 📌 **Features**  
✅ Convert any image into a cartoon-style drawing  
✅ Supports multiple image formats (JPG, PNG, BMP, etc.)  
✅ Works with **command-line** and **GUI mode**  
✅ Simple and easy-to-use interface  

---

## 📷 **Demo**  
### **Original Image:**  
![Original Image](https://via.placeholder.com/250)  

### **Cartoonized Image:**  
![Cartoon Image](https://via.placeholder.com/250)  

---

## 🔧 **Technologies Used**  
- **Python**  
- **OpenCV** (for image processing)  
- **NumPy** (for matrix operations)  
- **Tkinter** (for GUI)  

---

## 📂 **Project Structure**  
```
📦 Cartoonizer
 ┣ 📜 cartoonizer.py          # Main script  
 ┣ 📜 gui.py                  # GUI for easy usage  
 ┣ 📜 sample.jpg              # Sample input image  
 ┣ 📜 requirements.txt        # Dependencies  
 ┣ 📜 README.md               # Documentation  
```

---

## 🛠️ **Installation**  
### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/prangowda/Cartoonizer.git
cd Cartoonizer
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## 🚀 **Usage**  
### **1️⃣ Command Line Mode**  
Convert an image using the command line:  
```bash
python cartoonizer.py --image sample.jpg
```

### **2️⃣ GUI Mode**  
Run the GUI for selecting an image:  
```bash
python gui.py
```

---

## 📜 **Requirements File (requirements.txt)**  
```txt
opencv-python
numpy
tkinter
```

---

## 📌 **How It Works**  
1️⃣ **Read the image** using OpenCV  
2️⃣ **Convert to grayscale**  
3️⃣ **Apply edge detection** using adaptive thresholding  
4️⃣ **Apply bilateral filter** for smoothness  
5️⃣ **Merge the edge mask with a color image**  

---

## 🏆 **Enhancements (Future Updates)**  
✔️ Add live webcam cartoonizing  
✔️ Support for video cartoonization  
✔️ Mobile app integration  

