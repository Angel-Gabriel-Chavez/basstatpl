import numpy as np
import pandas as pd
import pandas._testing as tm
import basstatpl as bst

ls = [51,51,53,53,53,53,53,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,57,57,57,57,57,57,59]
a = bst.Analysis(ls)

def test_frequency_table():
    expl = {'Xi': {0: 51, 1: 53, 2: 54, 3: 57, 4: 59}, 
            'Fi': {0: 2, 1: 5, 2: 15, 3: 6, 4: 1}, 
            'Fa': {0: 2, 1: 7, 2: 22, 3: 28, 4: 29}, 
            'Fr': {0: 0.06896551724137931, 1: 0.1724137931034483, 2: 0.5172413793103449, 3: 0.20689655172413793, 4: 0.034482758620689655}, 
            'FrP': {0: 6.896551724137931, 1: 17.24137931034483, 2: 51.724137931034484, 3: 20.689655172413794, 4: 3.4482758620689653}, 
            'FG': {0: 24.82758620689655, 1: 62.06896551724138, 2: 186.20689655172416, 3: 74.48275862068965, 4: 12.413793103448276}}

    df = pd.DataFrame(expl)
    tm.assert_frame_equal(a.als.frequency_table, df, check_dtype = False)