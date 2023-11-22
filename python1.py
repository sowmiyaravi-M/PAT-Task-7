from datetime import datetime

def text_file_with_timestamp():
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(filename)

    print(f"File '{filename}' created successfully with the current timestamp.")

# Call the function to create the text file
text_file_with_timestamp()
