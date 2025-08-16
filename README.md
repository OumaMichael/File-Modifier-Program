# File Modifier Program

A Python program that reads a file, modifies its content, and saves a new version with comprehensive error handling.

## Features 

- Reads any text file
- Adds line numbers and converts text to uppercase (customizable)
- Creates a new modified file
- Handles common file errors gracefully
- Interactive command-line interface

## How It Works 

1. **Input**: User provides:
   - Input filename (must exist)
   - Output filename (default: `output.txt`)

2. **Processing**:
   - Reads input file
   - Modifies content (adds line numbers + uppercase)
   - Writes to new file

3. **Error Handling** Catches:
   - Missing files (`FileNotFoundError`)
   - Permission issues (`PermissionError`)
   - Encoding problems (`UnicodeDecodeError`)
   - Other unexpected errors

## Usage 

1. Run the program:
   ```bash
   python file_modifier.py
   ```