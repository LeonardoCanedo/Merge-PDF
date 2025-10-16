from PyPDF2 import PdfReader, PdfWriter
import os

# Load the PDF
input_path = os.path.join(os.path.dirname(__file__), "merged_output.pdf")
reader = PdfReader(input_path)
writer = PdfWriter()

# Define pages to remove (1-based indexing)
remove_pages = set(range(1, 11)) | set(range(13, 17))

# Loop through all pages and add only the ones not in remove_pages
for i in range(len(reader.pages)):
    if (i + 1) not in remove_pages:
        writer.add_page(reader.pages[i])

# Save the cleaned PDF
output_path = os.path.join(os.path.dirname(__file__), "cleaned_output.pdf")
with open(output_path, "wb") as f:
    writer.write(f)

print(f"Pages removed. Cleaned PDF saved as: {output_path}")