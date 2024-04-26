import os
from pathlib import Path

SHEET_FOLDER_PATH = Path("/mnt/c/Users/Yannick/2024-04-21 Scan aller Noten")

folder_to_part_strings = {
    "Alt-Horn_Melodie_Es": ["Alt-Horn_Melodie_Es"],
    "Alt-Klarinette_Es": ["Alt-Klarinette_Es"],
    "Alt-Saxophon_1_Es": ["Alt-Saxophon_1_Es", "Alt-Saxophon_Es"],
    "Alt-Saxophon_2_Es": ["Alt-Saxophon_2_Es", "Alt-Saxophon_Es"],
    "Bariton-Saxophon_Es": ["Bariton-Saxophon_Es"],
    "Bariton_B": ["Bariton_B", "Bariton_B_Violin"],
    "Bariton_C": ["Bariton_C"],
    "Bass-Posaune_B": ["Bass-Posaune_B"],
    "Bass-Posaune_C": ["Bass-Posaune_C"],
    "Bass_1_B": ["Bass_1_B", "Bass_B", "Bass_B_Violin"],
    "Bass_1_C": ["Bass_1_C", "Bass_C"],
    "Bass_1_Es": ["Bass_1_Es", "Bass_Es", "Bass_Es_Violin"],
    "Bass_2_B": ["Bass_2_B, Bass_B", "Bass_B_Violin"],
    "Bass_2_C": ["Bass_2_C", "Bass_C"],
    "Partitur": ["Direktion", "Direktion_Di", "Partitur"],
    "Schlagzeug": [
        "Schlagzeug",
        "Becken",
        "GroßeTrommel",
        "GroßeTrommel_Becken",
        "KleineTrommel",
        "Löffel_Solo",
        "Tamburin",
    ],
    "Flügelhorn_1_B": ["Flügelhorn_1-B", "Flügelhorn_1_B"],
    "Flügelhorn_2_B": ["Flügelhorn_2_B", "Flügelhorn_3_B"],
    "Horn_1_Es": ["Horn_1_Es", "Horn_Melodie_1_Es", "Horn_Melodie_Es"],
    "Horn_1_F": ["Horn_1_F", "Horn_Melodie_1_F", "Horn_Melodie_F"],
    "Horn_2_Es": ["Horn_2_Es", "Horn_Melodie_2_Es", "Horn_Melodie_Es"],
    "Horn_2_F": ["Horn_2-F", "Horn_2_F", "Horn_Melodie_2_F", "Horn_Melodie_F"],
    "Horn_3_Es": ["Horn_3_Es"],
    "Horn_3_F": ["Horn_3_F"],
    "Horn_4_Es": ["Horn_4_Es"],
    "Horn_4_F": ["Horn_4_F"],
    "Klarinette_1_B": ["Klarinette_1_B"],
    "Klarinette_2_B": ["Klarinette_23_B", "Klarinette_2_B"],
    "Klarinette_2_Es": ["Klarinette_2_Es"],
    "Klarinette_3_B": ["Klarinette_3_B", "Klarinette_23_B"],
    "Klarinette_Es": ["Klarinette_Es"],
    "Piccolo_C": ["Piccolo_C"],
    "Posaune_1_B": [
        "Posaune_1_B",
        "Posaune_1_B_Violin",
        "Posaune_B",
        "Posaune_Begleitung_1_B",
        "Posaune_Melodie_B",
        "Posuane_1_B",
    ],
    "Posaune_1_C": [
        "Posaune_1_C",
        "Posaune_1_C_Bass",
        "Posaune_Begleitung_1_C",
        "Posaune_C",
        "Posaune_Melodie_C",
    ],
    "Posaune_2_B": [
        "Posaune_2_B",
        "Posaune_2_B_Violin",
        "Posaune_B",
        "Posaune_Begleitung_2_B",
        "Posaune_Melodie_B",
    ],
    "Posaune_2_C": [
        "Posaune_2_C",
        "Posaune_2_C_Bass",
        "Posaune_Begleitung_2_C",
        "Posaune_C",
        "Posaune_Melodie_C",
    ],
    "Posaune_3_B": ["Posaune_3_B", "Posaune_3_B_Violin", "Posaune_Begleitung_3_B"],
    "Posaune_3_C": ["Posaune_3_C", "Posaune_3_C_Bass", "Posaune_Begleitung_3_C"],
    "Sopran-Saxophon_B": ["Sopran-Saxophon_B"],
    "Tenor-Saxophon_1_B": [
        "Tenor-Saxophon_1_B",
        "Tenor-Saxophon_12_B",
        "Tenor-Saxophon_B",
    ],
    "Tenor-Saxophon_2_B": [
        "Tenor-Saxophon_2_B",
        "Tenor-Saxophon_12_B",
        "Tenor-Saxophon_B",
    ],
    "Tenorhorn_1-B": ["Tenorhorn_1-B", "Tenorhorn_1_B", "Tenorhorn_B"],
    "Tenorhorn_1_C": ["Tenorhorn_1_C", "Tenorhorn_C"],
    "Tenorhorn_2_B": ["Tenorhorn_2_B", "Tenorhorn_B"],
    "Tenorhorn_2_C": ["Tenorhorn_2_C", "Tenorhorn_C"],
    "Tenorhorn_3_B": ["Tenorhorn_3_B", "Tenorhon_3_B"],
    "Tenorhorn_3_C": ["Tenorhorn_3_C"],
    "Trompete_1_B": ["Trompete_1_B", "Trompete_B", "Trompete_Solo_B"],
    "Trompete_2_B": ["Trompete_2_B", "Tompete_2_B"],
    "Trompete_3_B": ["Trompete_3_B"],
    "Trompete_4_B": ["Trompete_4_B"],
}

print(os.listdir(SHEET_FOLDER_PATH))
parts = set()

for song in os.listdir(SHEET_FOLDER_PATH):
    suffix = "_" + song + ".pdf"
    for part in os.listdir(SHEET_FOLDER_PATH / song):
        part = part[: -len(suffix)]

        if part == "Tenor-Flügelhorn_B":
            print(song)

        parts.add(part)

print(sorted(list(parts)))
