import os
from langchain_core.tools import tool

@tool
def save_to_file(content: str, filename: str) -> str:
    """Saves content to the given filename in the 'output' folder. Appends if the file already exists."""

     # 1. Define and create the output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) # Automatically creates the folder

    # 2. Construct the safe file path
    file_path = os.path.join(output_dir, filename)

    # 3. Write the content, append if the file already exists
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content.strip() + "\n\n")

    return f"Successfully saved to {filename}"