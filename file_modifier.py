"""
File Modifier Program
Reads a file, modifies its content, and writes to a new file with error handling.
"""

def modify_content(content):
    """Example modifier: adds line numbers and converts to uppercase"""
    modified_lines = []
    for i, line in enumerate(content.splitlines(), 1):
        modified_lines.append(f"{i}. {line.upper()}")
    return "\n".join(modified_lines)

def process_file(input_path, output_path="output.txt"):
    try:
        # Read input file
        with open(input_path, 'r') as input_file:
            content = input_file.read()
        
        # Modify content
        modified = modify_content(content)
        
        # Write output file
        with open(output_path, 'w') as output_file:
            output_file.write(modified)
            
        print(f"Success! Modified file saved as '{output_path}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_path}'.")
    except UnicodeDecodeError:
        print("Error: Could not decode the file (try a different encoding).")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("=== File Modifier ===")
    input_file = input("Enter filename to process: ").strip()
    output_file = input("Enter output filename (default: output.txt): ").strip() or "output.txt"
    
    process_file(input_file, output_file)