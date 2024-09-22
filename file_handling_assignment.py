
try:
    with open("my_file.txt", 'w') as file:
        file.write("Line 1: Hello!\n")
        file.write("Line 2: This is a Python assignment!\n")
        file.write("Line 3: Random numbers: 34985678\n")
    print("File 'my_file.txt' created and written successfully.")

    with open("my_file.txt", 'r') as file:
        print("\nReading 'my_file.txt':")
        content = file.read()
        print(content)

    with open("my_file.txt", 'a') as file:
        file.write("Line 4: Appending text.\n")
        file.write("Line 5: More random numbers: 67890\n")
        file.write("Line 6: End of the file. For now...\n")
    print("\nAdditional lines appended to 'my_file.txt' successfully.")

    with open("my_file.txt", 'r') as file:
        print("\nReading the updated file 'my_file.txt':")
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: Permission denied when trying to access 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operation complete.")
