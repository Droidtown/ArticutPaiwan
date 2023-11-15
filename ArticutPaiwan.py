#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

class ArticutPaiwan:
    def __init__(self):
        self.morphology = []
        self.ActiveVoicePat = re.compile(r"\b(?<!\-)(ti|a)(?!\-)\b")
        self.EntityNounPat = re.compile(r"(?<=ti</FUNC_inner>\s)[^\s]+?\b")

    def _FUNC_inner(self):
        voiceMarkerLIST = [[a.start(), a.end(), a.group(0)] for a in reversed(list(self.ActiveVoicePat.finditer(self.inputSTR)))]
        for v in voiceMarkerLIST:
            self.inputSTR = "{}{}{}".format(self.inputSTR[:v[0]], "<FUNC_inner>{}</FUNC_inner>".format(v[2]), self.inputSTR[v[1]:])

    def _ENTITY_noun(self):
        entityLIST = [[e.start(), e.end(), e.group(0)] for e in reversed(list(self.EntityNounPat.finditer(self.inputSTR)))]
        for e in entityLIST:
            self.inputSTR = "{}{}{}".format(self.inputSTR[:e[0]], "<ENTITY_noun>{}</ENTITY_noun>".format(e[2]), self.inputSTR[e[1]:])

    def parse(self, inputSTR):
        self.inputSTR = inputSTR
        self._FUNC_inner()
        self._ENTITY_noun()

        return self.inputSTR


if __name__ == "__main__":
    inputSTR = "pai mi-gacalj ti yusiv, sa kacu-i azua aljak katua kina, sa vaik a pa-sa israil."
    articutPaiwan = ArticutPaiwan()
    resultSTR = articutPaiwan.parse(inputSTR)
    print(resultSTR)

