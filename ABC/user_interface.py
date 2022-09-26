import pandas as pd
import PySimpleGUI as sg
from pathlib import Path
from calculations import *
from actions import *
from icecream import ic
from openpyxl import load_workbook
import xlrd
import xlwt
import sys


sg.ChangeLookAndFeel("Black")


if len(sys.argv) == 1:
    fname = sg.popup_get_file(
        'nieuwe heritage file zonder header'
    )
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    # sg.popup('The filename you chose was', fname)
    pad = Path(fname)
    # print("volledig pad:")
    ic(pad.parent)
    # print("naam file met suffix:")
    ic(pad.name)
    # print("naam file:")
    ic(pad.stem)
    ic(pad.parent)

    df = pd.read_csv(pad, delimiter=";", names=["serials"])
    wikkels = len(df) // 1800
    ic(wikkels)
    delerr = wikkels // 3
    ic(df.head())
    ic(delerr)

    # dataframe word verdeelt over een waarde, als de waarde van de uitkomst lijst groter of kleiner is dan...
    # moet of de lijst opgevuld worden, of niet
    # de restwaarde worden opgeruimd

    blok_lengte = delen(lengte_dataframe(df), 3)



    begin_eind_lijst_blokken = lijst_begin_eind_voor_slice(lengte_dataframe(df), blok_lengte)
    ic(len(begin_eind_lijst_blokken))
    keys_for_rol = [f'Rol {number + 1}' for number in range(len(begin_eind_lijst_blokken))]



    # de snelse manier om de dataframe in drie delen kolommen op te splitsen!
    # hier wordt de dataframe netjes in drie(4) dataframes gesplitst.
    list_of_df = [df.loc[i:i + blok_lengte - 1, :].reset_index(drop=True) for i in range(0, len(df), blok_lengte)]
    # Ik gebruik er hier 3 van de 4, dit is een custom job
    dataframes_in_dict = dict(zip(keys_for_rol, list_of_df))

    drie_kollomen = pd.concat(list_of_df[0:2], axis=1)

    generator = drie_kollomen.itertuples(index=True)
    nieuwe_df = []


    begin_eind_comp = []
    columnnames = []
    for key, value in dataframes_in_dict.items():
        columnnames.append(str(key))
        begin_eind_comp.append(value)

    vierk = pd.concat(begin_eind_comp, axis=1)
    vierk.columns=[columnnames]






















