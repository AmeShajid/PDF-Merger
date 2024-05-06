

#Import Libraries: Import necessary libraries (PyPDF2, sys, os) for PDF manipulation, system operations, and file handling.
import PyPDF2 
import sys
import os

# Create a PdfMerger object named merger to merge multiple PDF files into a single PDF.
merger = PyPDF2.PdfMerger()

# Use a try-except block to handle any exceptions that may occur during PDF merging. This ensures graceful error handling.
try:
    # Loop through files in the current directory
    #Iterate through the files in the current directory using os.listdir(os.curdir).
    for file in os.listdir(os.curdir):
        # Check if the file ends with ".pdf"
        #Check if the file ends with ".pdf" using file.endswith(".pdf"). This filters out non-PDF files.
        if file.endswith(".pdf"):
            print(file)
            # Open the PDF file in binary read mode ('rb')
            #Open the PDF file in binary read mode ('rb') using open(file, 'rb').
            with open(file, 'rb') as pdf_file:
                # Read the PDF and append it to the merger
                # Read the PDF file and append it to the merger object using merger.append(pdf_file).
                merger.append(pdf_file)

    # Write the merged PDF to a file
    #After appending all PDF files, write the merged PDF to a file named "combinedDocs.pdf" using merger.write(output_file).
    with open("combinedDocs.pdf", "wb") as output_file:
        merger.write(output_file)

    # Print a success message
    #Print a success message if the PDF merging process completes without errors.
    print("Merged PDF successfully created.")

except Exception as e:
    # Print an error message if an exception occurs
    #f an exception occurs during the PDF merging process, print an error message along with the exception details.
    print("Error occurred during PDF merging:", e)

finally:#we are using the finally because we want to make sure that the merger object is closed properly to release any allocated resources.
    # Close the merger to release resources
    #Use a finally block to ensure that the merger object is closed properly to release any allocated resources. This is done using merger.close().
    merger.close()



