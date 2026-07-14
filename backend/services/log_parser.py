"""
Log Parser Service
Membaca file log (.log, .txt, .csv)
"""

import os
import pandas as pd


class LogParser:

    @staticmethod
    def parse(file_path: str) -> str:

        ext = os.path.splitext(file_path)[1].lower()

        # ==========================
        # LOG / TXT
        # ==========================
        if ext in [".log", ".txt"]:

            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        # ==========================
        # CSV
        # ==========================
        elif ext == ".csv":

            df = pd.read_csv(file_path)

            return df.to_string(index=False)

        else:
            raise ValueError("Format file tidak didukung.")