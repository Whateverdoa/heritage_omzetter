"""The actions are anything that depend on when
they are called or how many times they are called.
The actions use arguments or other recources"""

import pandas as pd
from pathlib import Path
from icecream import ic
from .calculations import *


def file_to_dataframe(file_in):
    """Builds a Dataframe from a workable csv or excel file
     on which we can Generate with itertuples"""

    if Path(file_in).suffix == ".csv":
        # extra arg = ";"or ","
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_csv(file_in, ";")

    elif Path(file_in).suffix == ".xlsx":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in, engine='openpyxl')

    elif Path(file_in).suffix == ".xls":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in)

    return file_to_generate_on


# itertuple

def wikkel_aan_file_zetten(dataframe_rol,  wikkel, rolnummer):
    """neem de csv file en zet er een sluitetiket en een wikkel aan inclusief rolnummer"""
    kolomnaamlijst= list(dataframe_rol.columns)
    # kolom naam lijst moet uit de in te lezen file te halen zijn of anders maak zelf file aan

    begin, eind, rol_aantal = begin_eind_dataframe(dataframe_rol)

    # print(dataframe_rol.head(1))


    twee_extra = pd.DataFrame(
        [(f"{begin}", "stans.pdf", "") for x in range(2)],
        columns=kolomnaamlijst,
    )

    wikkel_df = pd.DataFrame(
        [(f"{begin}", "stans.pdf", "") for x in range(wikkel)],
        columns=kolomnaamlijst,
    )

    sluitstuk = pd.DataFrame(
        [(f"{begin}", "stans.pdf", f"{rolnummer} | {begin} - {eind} |  {rol_aantal} etiketten")],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=kolomnaamlijst,
    )

    dataframe_van_rol_met_wikkel = pd.concat([twee_extra, sluitstuk, wikkel_df, dataframe_rol])

    return dataframe_van_rol_met_wikkel
