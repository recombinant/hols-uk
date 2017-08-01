#!/usr/bin/env python3
# coding: utf-8
#
# Stub file for hols_uk.ics2csv
#
import datetime
from pathlib import Path, PurePath
from typing import Dict, Union


def hols2csv(holidays: dict, csv_path: Union[Path, PurePath]) -> None:
    ...


def import_ics(ics_path: Path) -> Dict[datetime.date, str]:
    ...


def main() -> None:
    ...


if __name__ == '__main__':
    main()
