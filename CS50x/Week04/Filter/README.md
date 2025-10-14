# 🖼 Filter (More) — CS50x Week 4

**Goal:** Extend the image filter program by implementing more advanced operations like edge detection, in addition to grayscale, reflect, and blur.

---

### 🧠 Key Concepts
- Manipulating RGB pixel data through structs (`RGBTRIPLE`)
- Working with 2D arrays to traverse image grids
- Implementing convolution matrices (kernels) for filters like **blur** and **edges**
- Understanding how the **Sobel operator** detects edges using gradients
- Maintaining memory safety and correct pixel averaging

---

### 🧩 Implemented Filters
| Filter | Description |
|---------|--------------|
| **Grayscale** | Converts the image to black and white by averaging RGB values |
| **Reflect** | Flips the image horizontally |
| **Blur** | Averages neighboring pixels to create a smoothing effect |
| **Edges** | Uses the Sobel operator to highlight boundaries in the image |

---

### ⚙️ Compile & Run (CS50 Environment)
```bash
make filter
./filter -e images/courtyard.bmp edges.bmp

Available options:

-g → grayscale

-r → reflect

-b → blur

-e → edges
```

💡 What I Learned

How to process image data at the byte level, apply mathematical operations to pixels, and use convolution to create powerful image effects.
