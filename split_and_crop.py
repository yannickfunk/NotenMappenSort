import os
from pathlib import Path

from PyPDF2 import PageObject, PaperSize, PdfReader, PdfWriter, Transformation

SHEET_FOLDER_PATH = Path("/mnt/c/Users/Yannick/2024-04-21 Scan aller Noten")
OUTPUT_PATH = Path("/mnt/c/Users/Yannick/Noten-Cropped")

SINGLE_PAGE_DOUBLE_SHEETS = [
    "Blas'_Musik_in_die_Welt!",
    "Euphoria",
    "Im_Eilschritt_nach_Sankt_Peter",
    "Kaiserin_Sissi",
    "Salemonia",
    "Schunkelparade_Nr.2",
    "Stelldichein_in_Oberkrain",
    "Unsere_Reise_Woodstock",
    "Von_Freund_zu_Freund_Woodstock",
    "Florentiner_Marsch",
]


def split_single_page_to_double_page(reader: PdfReader) -> PdfWriter:
    # get first page
    source_page = reader.pages[0]
    source_page.scale_to(PaperSize.A4.width * 2, PaperSize.A4.height)

    # create two blank pages
    first_page = PageObject.create_blank_page(
        width=PaperSize.A4.width, height=PaperSize.A4.height
    )
    second_page = PageObject.create_blank_page(
        width=PaperSize.A4.width, height=PaperSize.A4.height
    )

    # write left half of source page to first page
    first_page.merge_page(source_page)

    # write right half of source page to second page
    source_page.add_transformation(Transformation().translate(-PaperSize.A4.width, 0))
    second_page.merge_page(source_page)

    # create writer and write pages
    writer = PdfWriter()
    writer.add_page(first_page)
    writer.add_page(second_page)

    return writer


for song in os.listdir(SHEET_FOLDER_PATH):
    # create folder for song if it doesn't exist
    if not (OUTPUT_PATH / song).exists():
        os.mkdir(OUTPUT_PATH / song)

    for part in os.listdir(SHEET_FOLDER_PATH / song):
        pdf_path = SHEET_FOLDER_PATH / song / part
        reader = PdfReader(pdf_path)

        if song in SINGLE_PAGE_DOUBLE_SHEETS:
            writer = split_single_page_to_double_page(reader)
        else:
            writer = PdfWriter()
            for page in reader.pages:
                _, _, width, heigth = page.cropbox
                if width > heigth:
                    page.rotate(-90)
                    page.scale_to(PaperSize.A4.height, PaperSize.A4.width)
                else:
                    page.scale_to(PaperSize.A4.width, PaperSize.A4.height)
                writer.add_page(page)

        with open(OUTPUT_PATH / song / part, "wb") as f:
            writer.write(f)
