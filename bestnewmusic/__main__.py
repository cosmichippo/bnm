#!/usr/bin/env python
import sys
import argparse

from .sources import (
    allmusic,
    boomkat,
    forced_exposure,
    midheaven,
    pitchfork,
    resident_advisor,
    wfmu,
)

choices = ["am", "p4k", "ra", "bk", "fe", "mh", "wfmu"]


def main():
    parser = argparse.ArgumentParser(
        description="View recent releases and their reviews from the command line",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "source",
        type=str,
        choices=choices,
        help="""\
- am   : AllMusic Editor's Choice
- p4k  : Pitchfork 8.0+ Albums
- ra   : Resident Advisor Recommends
- bk   : Boomkat Weekly Best Sellers
- mh   : Midheaven Weekly Best Sellers
- fe   : Forced Exposure Weekly Best Sellers
- wfmu : WFMU Weekly Charts""",
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Display items in reverse order (with most recent last)",
    )

    parser.add_argument(
        "-l", "--length", type=int, default=None, help="Number of items to display"
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    source = args.source.lower()
    reverse = args.reverse

    n_items = None
    if args.length:
        n_items = args.length

    if source not in choices:
        vals = ", ".join(["'{}'".format(c) for c in choices])
        parser.error(
            "Unrecognized source '{}'. Valid entries are {}.".format(args.source, vals)
        )
    elif source == "am":
        allmusic(oldest_first=reverse, n_items=n_items)
    elif source == "p4k":
        pitchfork(oldest_first=reverse, n_items=n_items)
    elif source == "ra":
        resident_advisor(oldest_first=reverse, n_items=n_items)
    elif source == "fe":
        forced_exposure(oldest_first=reverse, n_items=n_items)
    elif source == "bk":
        boomkat(oldest_first=reverse, n_items=n_items)
    elif source == "wfmu":
        wfmu(oldest_first=reverse, n_items=n_items)
    elif source == "mh":
        midheaven(oldest_first=reverse, n_items=n_items)


if __name__ == "__main__":
    main()
