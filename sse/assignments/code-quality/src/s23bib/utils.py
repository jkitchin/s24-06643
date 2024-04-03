import bibtexparser


def sort_bibtex(bibfile, ascending=True, inplace=False):
    """Sort a bibtex file.

    Parameters
    ----------
    bibfile : string
        for the path to a bibtex file.
    ascending: Boolean
        sort in ascending if True
    inplace : Boolean
        write to file if True else return entries.

    Returns
    -------
    if inplace is True, returns None, or the sorted entries.
    """
    with open(bibfile) as bf:
        bd = bibtexparser.load(bf)
    entries = bd.entries
    entries.sort(key=lambda entry: int(entry["year"]), reverse=not ascending)

    if inplace:
        db = bibtexparser.bibdatabase.BibDatabase
        db.entries = entries
        db.comments = []
        db.strings = {}
        db.preambles = []
        writer = bibtexparser.bwriter.BibTexWriter()
        with open(bibfile, "w") as bibfile:
            bibfile.write(writer.write(db))

    else:
        return entries
