# Python Project Collection

A collection of fun and useful Python scripts for image processing and interactive games.

## Projects Included

### 1. GIF Creator

A simple script to create animated GIFs from a sequence of static images.

**Features:**
- Converts multiple images into a single animated GIF
- Automatically resizes images to maintain consistent dimensions
- Customizable frame duration and loop settings

**Requirements:**
- Python 3.x
- imageio
- Pillow (PIL)

**Installation:**

```bash
pip install imageio pillow
```

**Usage:**

Place your JPG images in the same directory as the script, then update the `filenames` list in `create_gif.py`:

```python
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
```

Run the script:

```bash
python create_gif.py
```

The animated GIF will be saved as `cat_running.gif`.

**Customization:**

Modify these parameters in `create_gif.py`:
- `filenames`: List of input image files
- `duration`: Frame duration in milliseconds (default: 200ms)
- `loop`: Number of times the GIF loops (0 = infinite)
- Output filename: Change the saved filename as needed

---

### 2. Word Guessing Game

An interactive word guessing game where you try to figure out a randomly selected word with a limited number of attempts.

**Features:**
- Draws from a comprehensive English word bank
- Pre-reveals all vowels to help get started
- Tracks attempted letters to prevent duplicates
- 10 attempts to guess the word correctly

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

Follow the on-screen prompts to guess letters. Try to reveal the complete word before your attempts run out!

**Gameplay Tips:**
- Vowels are revealed at the start
- You can't guess the same letter twice
- Each wrong guess costs one attempt
- You have 10 attempts total

---

## License

Both projects are licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

Himansh Mewada

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.