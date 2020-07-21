import PyPDF2

def main():
    pdfFile = "simple1.pdf"
    pdfRead =  PyPDF2.PdfFileReader(pdfFile)

    for i in range(pdfRead.getNumPages()):

        page = pdfRead.getPage(i)
        print("Page No " + str(i + pdfRead.getPageNumber(page)))
        pageContent = page.extractText()
        print(pageContent)


if __name__ == "__main__":
    main()