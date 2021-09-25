#!/usr/bin/env python3

import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()


if __name__ == "main":
    typer.run(main)

