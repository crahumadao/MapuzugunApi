import re
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent


class Xoy:

    def __init__(self, idx='f0', regex='', wecun=False, cemkeci=1, inaafeyu_verbo=True, wigkazugun='', kineupa=True,
                 rakin=0):
        self.id = idx
        if '^' not in regex:
            regex = '^' + regex
        self.regex = regex
        self._compiled_regex = re.compile(regex)
        self.wecun = wecun
        self.cemkeci = cemkeci
        self.inafeyu_verbo = inaafeyu_verbo
        self.wigkazugun = wigkazugun
        self.kineupa = kineupa
        self.rakin = rakin

    def __str__(self):
        return self.regex

    def __repr__(self):
        return self.regex

    def __eq__(self, kagelu):
        return self.id == kagelu.id and self.regex == kagelu.regex

    def mvli(self, hemvl):
        return self._compiled_regex.match(hemvl) is not None

    def wvzage(self, hemvl):
        match = self._compiled_regex.match(hemvl)
        if match is None:
            return None

        end = match.end()
        return hemvl[:end], hemvl[end:]


verbo_regex = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
               pd.read_csv(DATA_DIR / 'folil.csv', sep=',', header=None).iterrows()]

pre_slots_ineke = [row for row in
                   pd.read_csv(DATA_DIR / 'xoy.csv', header=None, sep=',', quotechar='"').iterrows()]
groups = set([g[1][7] for g in pre_slots_ineke])
slotsIneke = []
for g in groups:
    slotsIneke.append(
        [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
         pre_slots_ineke if row[1][7] == g])

pre_desinencias = [row for row in pd.read_csv(DATA_DIR / 'wechun.csv', usecols=range(8), header=None, sep=',',
                                              quotechar='"').iterrows()]
desinenciasInd = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
                  pre_desinencias if 'dI' in row[1][0]]
transicionInd = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
                 pre_desinencias if 'tI' in row[1][0]]
desinenciasCond = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row
                   in pre_desinencias if 'dC' in row[1][0]]
transicionCond = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
                  pre_desinencias if 'tC' in row[1][0]]
desinenciasImpe = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row
                   in pre_desinencias if 'di' in row[1][0]]
transicionImpe = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row in
                  pre_desinencias if 'ti' in row[1][0]]
otrasDesinencias = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for row
                    in pre_desinencias if 'ti' in row[1][0]]
sustantivosAdjetivos = [Xoy(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]) for
                        row in pd.read_csv(DATA_DIR / 'susadj.csv', header=None, doublequote='"').iterrows()]
