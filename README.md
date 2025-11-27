# Python Project Collection

A collection of fun and useful Python scripts for image processing, machine learning, and interactive games.

## 📚 Projects Included

### 1. GIF Creator

Transform a series of static images into a smooth, animated GIF with automatic resizing and customizable playback settings.

**Features:**
- Converts multiple images into a single animated GIF
- Automatically resizes all images to consistent dimensions for seamless animation
- Customizable frame duration and loop settings
- Simple and straightforward implementation

**Requirements:**
- Python 3.x
- imageio
- Pillow (PIL)

**Installation:**

```bash
pip install imageio pillow
```

**Usage:**

1. Place your JPG images in the same directory as the script
2. Update the `filenames` list in `create_gif.py` to match your image names:

```python
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
```

3. Run the script:

```bash
python create_gif.py
```

The animated GIF will be saved as `cat_running.gif` in your project folder.

**Customization:**

Modify these parameters in `create_gif.py`:
- `filenames`: List of input image files to include in the GIF
- `duration`: Frame duration in milliseconds (default: 200ms per frame)
- `loop`: Number of times the GIF loops (0 = infinite looping)
- Output filename: Change `'cat_running.gif'` to your desired output name

---

### 2. Word Guessing Game

An engaging interactive game where you try to deduce a randomly selected word by guessing individual letters before running out of attempts.

**Features:**
- Draws from a comprehensive English word bank (web2 dictionary)
- Vowels are pre-revealed to help you get started
- Prevents duplicate letter guesses with tracking
- 10 attempts to guess the word correctly
- Real-time feedback on each guess

**Requirements:**
- Python 3.x
- english-words

**Installation:**

```bash
pip install english-words
```

**Usage:**

```bash
python word_guessing_game.py
```

Follow the on-screen prompts to guess letters one at a time. Try to reveal the complete word before your 10 attempts run out!

**Gameplay Tips:**
- All vowels are automatically revealed at the start
- You cannot guess the same letter twice—the game will remind you if you try
- Each incorrect guess costs one attempt
- You have exactly 10 attempts to identify the word
- Enter one letter at a time for each guess

---

### 3. Home Price Prediction via Linear Regression

A machine learning project that demonstrates linear regression to predict house prices based on house size.

**Features:**
- Loads housing data from a CSV file
- Visualizes the relationship between house size and price
- Trains a linear regression model on the data
- Generates predictions on test data
- Displays both actual and predicted prices on a comparative plot

**Requirements:**
- Python 3.x
- numpy
- pandas
- matplotlib
- scikit-learn

**Installation:**

```bash
pip install numpy pandas matplotlib scikit-learn
```

**Usage:**

1. Prepare a CSV file named `home_dataset.csv` with columns `HouseSize` and `HousePrice`
2. Place the CSV file in the same directory as the script
3. Run the script:

```bash
python home_price_via_linear_regression.py
```

The script will display two plots:
- A scatter plot showing the relationship between house size and price
- A comparison plot showing actual prices vs. predictions from the trained model

---

## 🚀 Getting Started

1. Clone or download this repository
2. Navigate to the project directory
3. Install the required dependencies for the projects you want to use (see individual project instructions above)
4. Run the desired script with Python

---

## 📝 License

All projects in this collection are licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for full details.

---

## 👤 Author

Himansh Mewada

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve any of these projects:

1. Fork the repository
2. Create a feature branch for your changes
3. Submit a pull request with a clear description of your improvements

Feel free to submit issues or suggestions for enhancements as well.

---

## 📞 Support

If you encounter any issues or have questions about these projects, please open an issue in the repository or contact the author.