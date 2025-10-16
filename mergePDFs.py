import os
from PyPDF2 import PdfMerger

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a merger object
merger = PdfMerger()

# Loop through all PDF files in the current directory
for filename in sorted(os.listdir(current_dir)):
    if filename.endswith(".pdf") and filename != "merged_output.pdf":
        merger.append(os.path.join(current_dir, filename))

# Write out the merged PDF
output_path = os.path.join(current_dir, "merged_output.pdf")
merger.write(output_path)
merger.close()

print(f"PDFs merged successfully into: {output_path}")