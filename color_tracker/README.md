## Color Tracker with Python and OpenCV

This CLI app lets you manipulate and track color of an image, and save the manipulated image with ease.

### How to use

- Start by clonning this repository:
  ```basg
    git clone <url> 
  ```
- Navigate to `color_tracker`:
  ```bash
    cd color_tracker
  ```
- Install dependencies:
  ```bash
    make install
  ```
- Run the program:
  ```bash
    ./color_tracker [options]
  ```

**Options:**
- `-i` or `--img`: to specify custom image
- `-o` or `--output`: to specify output directory


### Example:

```bash
  ./color_tracker -i resources/red.jpg -o ./
```


*Photo credit*: 
- [Red car](https://www.pexels.com/photo/red-ferrari-337909/)
- [Blue car](https://www.pexels.com/@mikebirdy/)

Made with love <3