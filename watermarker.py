import sys

import PyPDF2

in_file = sys.argv[1]
wtr_file = sys.argv[2]

in_filename, in_extension = in_file.split('.')
wtr_filename, wtr_extension = wtr_file.split('.')


with open(in_file, 'rb') as input_file:
    # Read content of the orignal file
    pdf = PyPDF2.PdfFileReader(input_file)

    # Get the total of pages of the original file
    pdf_num_pages = pdf.getNumPages()

    with open(wtr_file, 'rb') as watermark_file:
        # Read content of the watermark file
        watermark = PyPDF2.PdfFileReader(watermark_file)

        # Get the watermark
        page_watermark = watermark.getPage(0)

        # Create pdf writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Merge pdf pages with watermark
        for page in range(pdf_num_pages):
            page_pdf = pdf.getPage(page)
            page_pdf.mergePage(page_watermark)

            # The next lines of code need to be inside the loop
            # in order to add the watermark in all the pages
            # add page
            pdf_writer.addPage(page_pdf)

            # Create output file
            with open(f'{in_filename}-{wtr_filename}.{in_extension}', 'wb') as output_file:
                pdf_writer.write(output_file)
