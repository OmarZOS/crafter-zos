import PyPDF4

def create_blank_page(input_path, output_path):
    pdf_writer = PyPDF4.PdfFileWriter()

    # Open the original PDF and extract its first page dimensions
    with open(input_path, "rb") as input_file:
        pdf_reader = PyPDF4.PdfFileReader(input_file)
        first_page = pdf_reader.getPage(0)
        width = first_page.mediaBox.getWidth()
        height = first_page.mediaBox.getHeight()

        # Create a blank page with the same dimensions as the first page
        pdf_writer.addBlankPage(width=width, height=height)

        for page_num in range((pdf_reader.getNumPages())):
            
            page = pdf_reader.getPage(page_num)
            
            pdf_writer.addPage(page)
        # Save the new file
        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)

def create_blank_page_in_end(input_path, output_path):
    pdf_writer = PyPDF4.PdfFileWriter()

    # Open the original PDF and extract its first page dimensions
    with open(input_path, "rb") as input_file:
        pdf_reader = PyPDF4.PdfFileReader(input_file)
        first_page = pdf_reader.getPage(0)
        width = first_page.mediaBox.getWidth()
        height = first_page.mediaBox.getHeight()


        for page_num in range((pdf_reader.getNumPages())):
            
            page = pdf_reader.getPage(page_num)
            
            pdf_writer.addPage(page)
        
        # Create a blank page with the same dimensions as the first page
        pdf_writer.addBlankPage(width=width, height=height)
        
        # Save the new file
        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)


def create_book(input_path, output_path):
    pdf_reader = PyPDF4.PdfFileReader(input_path)
    pdf_writer = PyPDF4.PdfFileWriter()

    # Get the total number of pages in the old file
    total_pages = pdf_reader.getNumPages()



    normal = True
    

    # Rearrange the pages for the book format
    for page_num in range((total_pages + 1) // 2):
        left_page = pdf_reader.getPage(page_num)
        right_page = pdf_reader.getPage(total_pages - 1 - page_num)


        
        # Rotate pages to be in landscape orientation
        # left_page.rotateClockwise(270)
        # right_page.rotateClockwise(270)

        # Create a new blank page with the size to fit both old pages
        new_page = pdf_writer.addBlankPage(
            width=left_page.mediaBox.getWidth()+ right_page.mediaBox.getWidth(),
            height= right_page.mediaBox.getHeight()
        )
        if not normal:
            temp = right_page
            right_page = left_page
            left_page= temp            

        # Add the left and right pages on the new blank page
        new_page.mergeTranslatedPage(left_page, right_page.mediaBox.getWidth(), 0)
        new_page.mergePage(right_page)
        
        
        normal = not normal

    # If there's an odd number of pages, add the last page as is
    if total_pages % 2 != 0:
        last_page = pdf_reader.getPage(total_pages // 2)
        last_page.rotateClockwise(270)
        pdf_writer.addPage(last_page)

    # Save the new file
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    old_file_path = "file.pdf"
    new_file_path = "new_file.pdf"
    new_file2_path = "new_file2.pdf"
    create_blank_page(old_file_path, new_file_path)
    create_book( new_file_path, new_file2_path)

