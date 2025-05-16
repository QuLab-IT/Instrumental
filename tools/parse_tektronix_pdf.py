from pypdf import PdfReader


def extract_index(pgs):
    for pg in pgs:
        text = pg.extract_text()
        if "Table of Contents" in text:
            print(text)
        input()


if __name__ == "__main__":
    reader = PdfReader("TBS2000-Programmer-077114902.pdf")
    pgs = reader.pages
    extract_index(pgs)
