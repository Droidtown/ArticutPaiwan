#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

def getPaiwan(inputSTR):
    """
    get Paiwan from inputSTR
    """

    soup = BeautifulSoup(inputSTR, "html.parser")
    rows = soup.find.all("tr")
    for r in range(0, len(rows)):
        if "章" in rows[r] and "節" in rows[r]:
    return None


if __name__ == "__main__":

    fileNameSTR = "./排灣語聖經 馬可福音 約翰福音 以弗所書.html"
    with open(fileNameSTR, encoding="utf-8") as f:
        inputSTR = f.read()

    inputSTR = inputSTR.split("排灣語馬可福音第1章")[1]
    resultSTR = getPaiwan(inputSTR)
    print(resultSTR)

