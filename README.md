
# AVL and Red-Black Tree Hybrid Implementation with Visualization

## Overview

This project implements a hybrid self-balancing binary search tree combining AVL and Red-Black Tree properties.  
It supports insertion, deletion, searching, and visualizes the tree structure using matplotlib.

---

## Features

- Insert integer keys maintaining AVL height balance and Red-Black color properties  
- Delete keys while keeping the tree balanced  
- Search keys efficiently  
- Visualize the tree with colored nodes (red or black) using matplotlib  
- Save visualizations to PNG files after insertions and deletions  

---

## Requirements

- Python 3.x  
- `matplotlib` for visualization

Install dependencies:

```bash
pip install matplotlib
```

---

## Usage

Run the program:

```bash
python avl_red_black_tree.py
```

Follow the prompts to:  
- Enter comma-separated integers to insert into the tree  
- View the tree visualization saved as `tree_after_insertion.png`  
- Enter comma-separated integers to delete from the tree  
- View the updated tree saved as `tree_after_deletion.png`  

---

## Code Structure

- **AVLRedBlackNode**: Node class with key, color ('R' or 'B'), left/right children, and height  
- **AVLRedBlackTree**: Main tree class implementing insertion, deletion, balancing, rotations, and color flips  
- **plot_tree**: Visualizes the tree with colored nodes and edges  
- **main**: User interaction loop for insertions and deletions with visualization  

---

## Notes

- Root is always black  
- Duplicate insertions are ignored  
- Balancing integrates AVL rotations and Red-Black color flips  
- Visualization shows node keys in colored circles (red or black)  

---

## License

This project is open-source and free to use.

---

## Example

Insert elements: `10,20,30,15,25`  
Delete elements: `20,15`  

Resulting tree visualizations will be saved to PNG files.

---

Feel free to contribute or request features!
