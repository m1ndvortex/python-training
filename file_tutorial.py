# Python File Handling Tutorial
# ===========================

# File handling is a crucial part of programming, allowing you to read from and write to files.
# Python provides simple and powerful tools for working with files of various types.

print("=" * 60)
print("FILE BASICS")
print("=" * 60)

print("\n1. Opening and closing files:")
# The basic syntax for opening a file
file = open("example.txt", "w")  # Open for writing (creates file if it doesn't exist)
file.write("Hello, World!")
file.close()  # Always close files when done

print("File opened, written to, and closed.")

# Better approach using context manager (automatically closes file)
print("\nUsing context manager (with statement):")
with open("example.txt", "w") as file:
    file.write("Hello, World with context manager!")
print("File automatically closed after with block")

print("\n2. File opening modes:")
print("""
Common file modes:
- 'r': Read (default) - opens file for reading
- 'w': Write - creates new file or truncates existing file
- 'a': Append - opens for writing, appending to end of file
- 'x': Exclusive creation - fails if file already exists
- 'b': Binary mode (added to other modes, e.g., 'rb')
- 't': Text mode (default, added to other modes, e.g., 'rt')
- '+': Read and write (added to other modes, e.g., 'r+')
""")

print("\n3. Reading from files:")
# First, create a file with multiple lines
with open("multiline.txt", "w") as file:
    file.write("Line 1: Python file handling is easy.\n")
    file.write("Line 2: You can read and write files.\n")
    file.write("Line 3: This is the last line.")

# Reading entire file at once
print("Reading entire file at once:")
with open("multiline.txt", "r") as file:
    content = file.read()
    print(f"Content:\n{content}")

# Reading line by line
print("\nReading line by line:")
with open("multiline.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

# Reading all lines into a list
print("\nReading all lines into a list:")
with open("multiline.txt", "r") as file:
    lines = file.readlines()
    print(f"Lines list: {lines}")
    print(f"Number of lines: {len(lines)}")

# Iterating through a file
print("\nIterating through file lines:")
with open("multiline.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")

print("\n4. Writing to files:")
# Writing strings
print("Writing strings to a file:")
with open("output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

    # Writing multiple lines at once
    lines = ["Third line\n", "Fourth line\n", "Fifth line"]
    file.writelines(lines)

# Reading back the file we just created
with open("output.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Appending to files
print("\nAppending to a file:")
with open("output.txt", "a") as file:
    file.write("\nThis line is appended to the end of the file.")

# Reading back the file after appending
with open("output.txt", "r") as file:
    content = file.read()
    print(f"File content after append:\n{content}")

print("=" * 60)
print("WORKING WITH FILE PATHS")
print("=" * 60)

import os
import shutil
from pathlib import Path

print("\n1. File path operations:")
# Current working directory
print(f"Current working directory: {os.getcwd()}")

# Joining paths (OS-independent)
data_dir = os.path.join("data", "files")
print(f"Joined path: {data_dir}")

# Creating directories
print("\n2. Creating directories:")
try:
    os.makedirs(data_dir, exist_ok=True)
    print(f"Created directory: {data_dir}")
except OSError as e:
    print(f"Error creating directory: {e}")

# Creating a file in the new directory
file_path = os.path.join(data_dir, "test.txt")
with open(file_path, "w") as file:
    file.write("This is a test file in a subdirectory.")
print(f"Created file: {file_path}")

# File path information
print("\n3. File path information:")
print(f"Full path: {os.path.abspath(file_path)}")
print(f"Directory name: {os.path.dirname(file_path)}")
print(f"File name: {os.path.basename(file_path)}")
name, ext = os.path.splitext(os.path.basename(file_path))
print(f"File name without extension: {name}")
print(f"File extension: {ext}")

# Checking if path exists
print(f"Path exists: {os.path.exists(file_path)}")
print(f"Is file: {os.path.isfile(file_path)}")
print(f"Is directory: {os.path.isdir(file_path)}")

print("\n4. Using pathlib (modern approach):")
# pathlib provides an object-oriented approach to file paths
file_path_obj = Path(file_path)
print(f"Path object: {file_path_obj}")
print(f"Parent directory: {file_path_obj.parent}")
print(f"File name: {file_path_obj.name}")
print(f"Stem (name without extension): {file_path_obj.stem}")
print(f"Suffix (extension): {file_path_obj.suffix}")
print(f"Exists: {file_path_obj.exists()}")
print(f"Is file: {file_path_obj.is_file()}")

# Creating paths with pathlib
new_file = Path(data_dir) / "another_file.txt"
print(f"New path created with pathlib: {new_file}")

# Writing to a file using pathlib
new_file.write_text("This file was created using pathlib.")
print(f"Content of new file: {new_file.read_text()}")

print("=" * 60)
print("ADVANCED FILE OPERATIONS")
print("=" * 60)

print("\n1. Working with binary files:")
# Creating a binary file
with open("binary_data.bin", "wb") as file:
    # Write bytes directly
    file.write(b"Binary data: \x00\x01\x02\x03")

    # Or convert strings to bytes
    file.write("More data".encode('utf-8'))

# Reading from a binary file
with open("binary_data.bin", "rb") as file:
    binary_data = file.read()
    print(f"Binary data (bytes): {binary_data}")
    print(f"Binary data (hex): {binary_data.hex()}")

    # Decoding part of the binary data back to string
    text_part = binary_data[13:].decode('utf-8')
    print(f"Decoded text part: {text_part}")

print("\n2. File seeking and telling:")
# Text file seeking (only absolute positioning)
with open("example.txt", "r") as file:
    # Get current position
    position = file.tell()
    print(f"Initial position: {position}")

    # Read some data
    data = file.read(5)
    print(f"Read data: '{data}'")

    # Get new position
    position = file.tell()
    print(f"New position after reading: {position}")

    # Seek to a specific position (from start)
    file.seek(0)
    print(f"After seeking to start, position: {file.tell()}")

    # Read again from the beginning
    data = file.read(5)
    print(f"Read data after seek: '{data}'")

# Binary file seeking (supports relative positioning)
with open("binary_data.bin", "rb") as file:
    print("\nBinary file seeking:")
    # Seek to position 5 from start
    file.seek(5)
    print(f"After seeking to position 5: {file.tell()}")

    # Read 4 bytes
    data = file.read(4)
    print(f"Read data: {data}")

    # Seek relative to current position
    file.seek(3, 1)  # Move 3 bytes forward from current position
    print(f"After relative seek: {file.tell()}")

    # Seek relative to end of file
    file.seek(-5, 2)  # Move 5 bytes back from end
    print(f"After seeking from end: {file.tell()}")
    data = file.read()
    print(f"Last 5 bytes: {data}")

print("\n3. File metadata and operations:")
file_stats = os.stat("example.txt")
print(f"File size: {file_stats.st_size} bytes")
print(f"Last modified: {os.path.getmtime('example.txt')}")
print(f"Last accessed: {os.path.getatime('example.txt')}")

# Copying files
shutil.copy2("example.txt", "example_copy.txt")
print("File copied from example.txt to example_copy.txt")

# Renaming files
os.rename("example_copy.txt", "renamed_example.txt")
print("File renamed from example_copy.txt to renamed_example.txt")

# Removing files
os.remove("renamed_example.txt")
print("File renamed_example.txt removed")

print("\n4. Working with CSV files:")
import csv

# Writing CSV data
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Name", "Age", "City"])
    # Write data rows
    writer.writerows([
        ["Alice", 25, "New York"],
        ["Bob", 30, "San Francisco"],
        ["Charlie", 35, "Chicago"]
    ])
print("CSV file created with sample data")

# Reading CSV data
print("\nReading CSV file:")
with open("data.csv", "r", newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get header row
    print(f"Header: {header}")

    for row in reader:
        print(f"Row: {row}")

# Using DictReader and DictWriter
print("\nUsing CSV DictReader and DictWriter:")
with open("data_dict.csv", "w", newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows([
        {"Name": "David", "Age": 40, "City": "Boston"},
        {"Name": "Eva", "Age": 45, "City": "Seattle"}
    ])
print("CSV file created using DictWriter")

with open("data_dict.csv", "r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

print("\n5. Working with JSON files:")
import json

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "Data Science", "Machine Learning"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"
    }
}

# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("JSON data written to file")

# Reading JSON from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(f"Loaded JSON data: {loaded_data}")
print(f"Name: {loaded_data['name']}")
print(f"First course: {loaded_data['courses'][0]}")
print(f"City: {loaded_data['address']['city']}")

print("=" * 60)
print("ERROR HANDLING AND BEST PRACTICES")
print("=" * 60)

print("\n1. Error handling with files:")
# Handling file not found
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

# Handling permission errors
try:
    # This would fail if you don't have write permission
    # Using a Windows system directory that typically requires admin rights
    with open("C:\\Windows\\System32\\test.txt", "w") as file:
        file.write("Test")
except PermissionError:
    print("Error: Permission denied")
except FileNotFoundError:
    # In case the directory doesn't exist or path format is wrong
    print("Error: File path not found - but this would normally be a permission error")

# Handling other I/O errors
try:
    with open("some_file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"I/O error occurred: {e}")

print("\n2. Safe file operations:")
def safe_read_file(filename, default=""):
    """Safely read a file with error handling."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error reading {filename}: {e}")
        return default

content = safe_read_file("example.txt", "File could not be read")
print(f"Safely read content: {content[:20]}...")

content = safe_read_file("nonexistent_file.txt", "File could not be read")
print(f"Result for nonexistent file: {content}")

print("\n3. Temporary files:")
import tempfile

# Creating a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp:
    temp_name = temp.name
    temp.write(b"This is temporary data")
    print(f"Temporary file created: {temp_name}")

# Reading from the temporary file
with open(temp_name, "rb") as file:
    temp_data = file.read()
    print(f"Read from temporary file: {temp_data.decode('utf-8')}")

# Clean up
os.remove(temp_name)
print(f"Temporary file removed")

# Creating a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created: {temp_dir}")
    # Create a file in the temporary directory
    temp_file_path = os.path.join(temp_dir, "temp_file.txt")
    with open(temp_file_path, "w") as file:
        file.write("File in temporary directory")
    print(f"Created file in temporary directory")
    # Directory and its contents are automatically removed

print("\n4. File locking for concurrent access:")
try:
    import fcntl
    has_fcntl = True
except ImportError:
    has_fcntl = False
    print("Note: fcntl module not available (Windows systems)")

if has_fcntl:
    print("File locking example (Unix/Linux/Mac):")
    with open("lock_example.txt", "w") as file:
        try:
            # Exclusive lock
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            file.write("This write is protected by a lock")
            print("File locked and written to")
            # Release lock
            fcntl.flock(file, fcntl.LOCK_UN)
            print("File unlocked")
        except IOError:
            print("Another process has locked the file")
else:
    # Windows alternative using msvcrt
    try:
        import msvcrt
        print("File locking example (Windows):")
        with open("lock_example.txt", "w") as file:
            try:
                # Lock file
                msvcrt.locking(file.fileno(), msvcrt.LK_NBLCK, 1)
                file.write("This write is protected by a lock")
                print("File locked and written to")
                # Release lock
                file.seek(0)
                msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
                print("File unlocked")
            except IOError:
                print("Another process has locked the file")
    except ImportError:
        print("Note: File locking example skipped (platform not supported)")

print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

print("\n1. Log file analyzer:")
# Create a sample log file
log_lines = [
    "2023-01-01 12:00:00 INFO: Application started\n",
    "2023-01-01 12:05:10 WARNING: Low memory detected\n",
    "2023-01-01 12:10:15 ERROR: Database connection failed\n",
    "2023-01-01 12:15:20 INFO: Retry database connection\n",
    "2023-01-01 12:15:25 INFO: Database connection established\n",
    "2023-01-01 12:30:00 WARNING: High CPU usage\n",
    "2023-01-01 12:45:00 ERROR: API request timeout\n"
]

with open("application.log", "w") as log_file:
    log_file.writelines(log_lines)

def analyze_log(log_path):
    """Analyze a log file and return statistics."""
    if not os.path.exists(log_path):
        return "Log file not found"

    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_messages = []

    with open(log_path, "r") as log_file:
        for line in log_file:
            if "INFO:" in line:
                stats["INFO"] += 1
            elif "WARNING:" in line:
                stats["WARNING"] += 1
            elif "ERROR:" in line:
                stats["ERROR"] += 1
                error_messages.append(line.strip())

    return {
        "statistics": stats,
        "total_entries": sum(stats.values()),
        "error_messages": error_messages
    }

log_analysis = analyze_log("application.log")
print("Log file analysis:")
print(f"Total log entries: {log_analysis['total_entries']}")
print(f"Statistics: {log_analysis['statistics']}")
print("Error messages:")
for msg in log_analysis['error_messages']:
    print(f"  {msg}")

print("\n2. Config file parser:")
# Create a sample config file
config_content = """
# Sample configuration file
[Database]
host = localhost
port = 5432
username = admin
password = secret

[API]
url = https://api.example.com
timeout = 30
retry_attempts = 3

[Logging]
level = INFO
file = app.log
"""

with open("config.ini", "w") as config_file:
    config_file.write(config_content)

import configparser

def parse_config(config_path):
    """Parse a configuration file and return the configuration."""
    config = configparser.ConfigParser()
    config.read(config_path)

    return config

config = parse_config("config.ini")
print("Configuration file parsed:")
for section in config.sections():
    print(f"\n[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")

print("\n3. File backup utility:")
def backup_file(file_path, backup_dir=None):
    """Create a backup of a file with timestamp."""
    import datetime

    if not os.path.exists(file_path):
        return f"Error: {file_path} does not exist"

    # Get file name and directory
    file_name = os.path.basename(file_path)
    dir_name = backup_dir or os.path.dirname(file_path) or "."

    # Create backup filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.splitext(file_name)[0]}_{timestamp}{os.path.splitext(file_name)[1]}"
    backup_path = os.path.join(dir_name, backup_name)

    # Copy the file
    try:
        shutil.copy2(file_path, backup_path)
        return f"Backup created: {backup_path}"
    except Exception as e:
        return f"Backup failed: {e}"

# Create a test file to backup
with open("important_data.txt", "w") as file:
    file.write("This is important data that needs to be backed up.")

# Create backup
result = backup_file("important_data.txt")
print(result)

print("\n4. File encryption/decryption:")
try:
    from cryptography.fernet import Fernet
    has_cryptography = True
except ImportError:
    has_cryptography = False
    print("Note: cryptography module not available. Install with 'pip install cryptography'")

if has_cryptography:
    def generate_key():
        """Generate an encryption key and save it to a file."""
        key = Fernet.generate_key()
        with open("encryption.key", "wb") as key_file:
            key_file.write(key)
        return key

    def encrypt_file(file_path, key):
        """Encrypt a file using the provided key."""
        f = Fernet(key)

        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(f"{file_path}.encrypted", "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(encrypted_file_path, key):
        """Decrypt a file using the provided key."""
        f = Fernet(key)

        with open(encrypted_file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        # Remove .encrypted extension for the decrypted file
        decrypted_file_path = encrypted_file_path.replace(".encrypted", ".decrypted")

        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_data)

    # Create a file to encrypt
    with open("secret.txt", "w") as file:
        file.write("This is a secret message that should be encrypted.")

    print("File encryption example:")
    # Generate and save key
    key = generate_key()
    print(f"Encryption key generated and saved to encryption.key")

    # Encrypt the file
    encrypt_file("secret.txt", key)
    print(f"File encrypted: secret.txt.encrypted")

    # Decrypt the file
    decrypt_file("secret.txt.encrypted", key)
    print(f"File decrypted: secret.txt.decrypted")

    # Verify decryption worked
    with open("secret.txt.decrypted", "r") as file:
        decrypted_content = file.read()
    print(f"Decrypted content: {decrypted_content}")

print("=" * 60)
print("IMPORTANT NOTES")
print("=" * 60)

print("""
1. Always use the 'with' statement when working with files to ensure they are properly closed.

2. Choose the appropriate file mode ('r', 'w', 'a', 'b', etc.) based on your needs.

3. Handle exceptions when working with files to gracefully manage errors.

4. Use the 'pathlib' module for modern, object-oriented file path handling.

5. For large files, read and write in chunks rather than loading the entire file into memory.

6. Be careful with file permissions, especially when your code runs on different operating systems.

7. Use appropriate encoding (e.g., 'utf-8') when working with text files containing non-ASCII characters.

8. Consider using specialized libraries for specific file formats (csv, json, xml, etc.).

9. Implement proper file locking mechanisms for concurrent access scenarios.

10. Regularly back up important files and implement error recovery strategies.

11. Be mindful of file system differences between operating systems (path separators, line endings, etc.).

12. For configuration files, consider using established formats like JSON, YAML, or INI.
""")

# Clean up created files
cleanup_files = [
    "example.txt", "multiline.txt", "output.txt", "binary_data.bin",
    "data.csv", "data_dict.csv", "data.json", "application.log",
    "config.ini", "important_data.txt", "lock_example.txt"
]

# Also try to clean up backup and encrypted files
import glob
for pattern in ["important_data_*.txt", "secret.txt*", "encryption.key"]:
    cleanup_files.extend(glob.glob(pattern))

print("\nCleaning up files created during this tutorial...")
for file in cleanup_files:
    try:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed: {file}")
    except Exception as e:
        print(f"Could not remove {file}: {e}")

# Try to remove the data directory
try:
    if os.path.exists("data"):
        shutil.rmtree("data")
        print("Removed directory: data")
except Exception as e:
    print(f"Could not remove data directory: {e}")

print("\nThank you for learning about Python file handling!")
