import pandas as pd
from .data import basis_lijst
from .actions import *
from .calculations import  *

test_lijst = basis_lijst()

de_test_lijst = pd.DataFrame(test_lijst(1, 100, 5))
de_test_lijst['pdf'] = 'leeg.pdf'
de_test_lijst['omschrijving'] = ''

def test_wikkel_aan_file_zetten():

    test = wikkel_aan_file_zetten(de_test_lijst, 1, "Rol 1")
    print(test.head(10))

    assert test.iloc[5, 1] == 'leeg.pdf'