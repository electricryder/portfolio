# 🔍 Recover — CS50x Week 4

**Goal:** Recover JPEG images from a forensic image of a memory card by reading raw bytes and identifying JPEG file signatures.

---

### 🧠 Key Concepts
- Reading binary files (`fread`, `fopen`, `fwrite`)
- Working with file pointers and 512-byte buffers
- Recognizing JPEG signatures (`0xff 0xd8 0xff 0xe0` or `0xe1`)
- Dynamically naming output files (`000.jpg`, `001.jpg`, …)
- Avoiding memory leaks and closing files properly

---

### 🧩 Example Workflow

./recover card.raw

The program scans `card.raw` and extracts valid JPEGs into the current directory:

000.jpg
001.jpg
002.jpg
...


---

### ⚙️ Compile & Run (CS50 Environment)
```bash
make recover
./recover card.raw

💡 What I Learned

How data is stored on disk, how to handle binary I/O safely in C,
and how recovery tools can identify and extract lost data from raw memory dumps.