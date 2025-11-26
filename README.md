# GIF Creator

A simple Python script to create animated GIFs from a sequence of images.

## Description

This project provides a straightforward way to combine multiple static images into an animated GIF file. The script automatically resizes all images to match the dimensions of the first image, ensuring consistency in the final animation.

## Features

- Converts multiple images into a single animated GIF
- Automatically resizes images to maintain consistent dimensions
- Customizable frame duration
- Configurable loop settings

## Requirements

- Python 3.x
- imageio
- Pillow (PIL)

## Installation

Install the required dependencies using pip:

```bash
pip install imageio pillow
```

## Usage

1. Place your source images (JPG format) in the same directory as the script
2. Update the `filenames` list in `create_gif.py` with your image filenames
3. Run the script:

```bash
python create_gif.py
```

The script will generate an animated GIF named `cat_running.gif` in the same directory.

## Configuration

You can customize the animation by modifying the following parameters in `create_gif.py`:

- **filenames**: List of input image files
- **duration**: Frame duration in milliseconds (default: 200ms)
- **loop**: Number of times the GIF loops (0 = infinite loop)
- **output filename**: Change the output GIF filename as needed

## Example

```python
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
iio.imwrite('output.gif', images, duration=200, loop=0)
```

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

Himansh Mewada

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.