# 🖼 Filter — CS50x Week 4

**Goal:** Apply image filters such as grayscale, sepia, reflect, and blur to bitmap images by directly manipulating pixel data in C.

---

### 🧠 Key Concepts
- Working with RGB pixel structs (`RGBTRIPLE`)
- Iterating through 2D arrays
- Nested loops and edge-handling for image borders
- Pointer arithmetic and memory safety

---

### 🧩 Example Workflow
./filter -r images/courtyard.bmp reflected.bmp

Outputs a horizontally-reflected version of the input image.  
Other options:
- `-g` → grayscale  
- `-s` → sepia  
- `-b` → blur  

---

### ⚙️ Compile & Run (CS50 Environment)
```bash
make filter
./filter -r images/courtyard.bmp reflected.bmp
```

What I Learned

How digital images are represented in memory, how to manipulate color data at the byte level, and how to implement algorithms that modify 2D arrays efficiently.
