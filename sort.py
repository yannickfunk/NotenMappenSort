import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from PyPDF2 import PdfMerger
from tqdm import tqdm

SHEET_FOLDER_PATH = Path("/mnt/c/Users/Yannick/Noten-Cropped")
OUTPUT_PATH = Path("/mnt/c/Users/Yannick/Notenmappen-Sortiert")

# define which folder contains which parts
FOLDER_TO_PART = {
    "1. Flöte + Piccolo": ["Flöte_1_C", "Flöte_C", "Piccolo_C"],  # 1 mal
    "1. Flöte": ["Flöte_1_C", "Flöte_C"],  # 1 mal
    "2. Flöte": ["Flöte_2_C", "Flöte_C"],  # 2 mal
    "1. Klarinette": ["Klarinette_1_B"],  # 1 mal
    "2. Klarinette": ["Klarinette_23_B", "Klarinette_2_B"],  # 1 mal
    "3. Klarinette": ["Klarinette_23_B", "Klarinette_3_B"],  # 1 mal
    "Es-Klarinette": ["Klarinette_Es", "Klarinette_2_Es"],  # 1 mal
    "1. Alt-Saxophon": ["Alt-Saxophon_1_Es", "Alt-Saxophon_Es"],  # 1 mal
    "2. Alt-Saxophon": ["Alt-Saxophon_2_Es", "Alt-Saxophon_Es"],  # 1 mal
    "Tenor-Saxophon + BariSax": [
        "Tenor-Saxophon_1_B",
        "Tenor-Saxophon_12_B",
        "Tenor-Saxophon_2_B",
        "Tenor-Saxophon_B",
        "Bariton-Saxophon_Es",
    ],  # 1 mal
    "1. Trompete": ["Trompete_1_B", "Trompete_B", "Trompete_Solo_B"],  # 1 mal
    "2. Trompete": ["Trompete_2_B", "Tompete_2_B"],  # 1 mal
    "3. + 4. Trompete": ["Trompete_3_B", "Trompete_4_B"],  # 1 mal
    "Flügelhorn_1_B": ["Flügelhorn_1-B", "Flügelhorn_1_B"],  # 2 mal
    "Flügelhorn_2_B": ["Flügelhorn_2_B", "Flügelhorn_3_B"],  # 2 mal
    "Tenorhorn_1-B": ["Tenorhorn_1-B", "Tenorhorn_1_B", "Tenorhorn_B"],  # 2 mal
    "Tenorhorn_2_B": ["Tenorhorn_2_B", "Tenorhorn_B"],  # 1 mal
    "1. (3.) Horn in F": [
        "Horn_1_F",
        "Horn_Melodie_1_F",
        "Horn_Melodie_F",
        "Horn_3_F",
    ],  # 1 mal
    "2. (4.) Horn in F": [
        "Horn_2-F",
        "Horn_2_F",
        "Horn_Melodie_2_F",
        "Horn_Melodie_F",
        "Horn_4_F",
    ],  # 1 mal
    "1. Posaune": [
        "Posaune_1_C",
        "Posaune_1_C_Bass",
        "Posaune_Begleitung_1_C",
        "Posaune_C",
        "Posaune_Melodie_C",
    ],  # 1 mal
    "2. Posaune": [
        "Posaune_2_C",
        "Posaune_2_C_Bass",
        "Posaune_Begleitung_2_C",
        "Posaune_C",
        "Posaune_Melodie_C",
    ],  # 1 mal
    "3. Posaune": [
        "Posaune_3_C",
        "Posaune_3_C_Bass",
        "Posaune_Begleitung_3_C",
    ],  # 1 mal
    "Bariton in B": ["Bariton_B", "Bariton_B_Violin"],  # 2 mal
    "Bariton_C": ["Bariton_C"],  # 2 mal
    "1. Bass in C": ["Bass_1_C", "Bass_C"],  # 1 mal
    "2. Bass in C": ["Bass_2_C", "Bass_C"],  # 1 mal
    "Bass in B + Eb": [
        "Bass_1_B",
        "Bass_B",
        "Bass_B_Violin",
        "Bass_1_Es",
        "Bass_Es",
        "Bass_Es_Violin",
        "Bass_2_B",
    ],  # 1 mal
    "Partitur": ["Direktion", "Direktion_Di", "Partitur"],  # 1 mal
    "Schlagzeug": [
        "Schlagzeug",
        "Becken",
        "GroßeTrommel",
        "GroßeTrommel_Becken",
        "KleineTrommel",
        "Löffel_Solo",
        "Tamburin",
    ],
}

# make reverse dict for later sorting
_part_to_folder = defaultdict(list)
for _folder, _parts in FOLDER_TO_PART.items():
    for _part in _parts:
        _part_to_folder[_part].append(_folder)
PART_TO_FOLDER: Dict[str, List[str]] = dict(_part_to_folder)


def sort_folders(folders: Dict[str, set[Path]]) -> Dict[str, List[Path]]:
    return {
        folder: sorted(list(pdf_paths), key=lambda x: x.parts[-2])
        for folder, pdf_paths in folders.items()
    }


def merge_pdfs(pdf_paths: List[Path], output_path: Path):
    merger = PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(str(pdf_path))
    merger.write(str(output_path))
    merger.close()


def create_folder_pdfs(folders: Dict[str, List[Path]]):
    # create OUTPUT_PATH if it does not exist
    if not OUTPUT_PATH.exists():
        OUTPUT_PATH.mkdir()

    for folder, pdf_paths in tqdm(folders.items(), desc="Erstellen der Mappen-PDFs:"):
        output_file = OUTPUT_PATH / (folder + ".pdf")
        merge_pdfs(pdf_paths, output_file)


def main():
    folders: Dict[str, set[Path]] = defaultdict(set)  # maps folder title to pdf path

    for song in os.listdir(SHEET_FOLDER_PATH):
        suffix = "_" + song + ".pdf"
        for part in os.listdir(SHEET_FOLDER_PATH / song):
            pdf_path = SHEET_FOLDER_PATH / song / part
            part = part[: -len(suffix)]
            destination_folders = PART_TO_FOLDER[part] if part in PART_TO_FOLDER else []
            for folder in destination_folders:
                folders[folder].add(pdf_path)

    # ensure the songs in each folder are sorted by song name
    sorted_folders = sort_folders(folders)

    # create the pdfs for each folder
    create_folder_pdfs(sorted_folders)


if __name__ == "__main__":
    main()
