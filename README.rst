python-xlsx
===========

A small footprint xslx reader that understands shared strings and can process
excel dates.

This fork adds:
    * transparent support for empty cells.
    * fixes row lookups e.g. sheet['6']

Usage
+++++++

::

    book = Workbook('filename or filedescriptor') # Open xlsx file
    for sheet in book:
        print sheet.name
        for row, cells in sheet.rows().iteritems(): # or sheet.cols()
            print row # prints row number
            for cell in cells:
                print cell.id, cell.value, cell.formula

    # or you can access the sheets by their name:

    some_sheet = book['some sheet name']

    # rows, columns, and cells can be accessed directly from sheets

    some_sheet['AA']  # column AA
    some_sheet['6']   # row 6
    some_sheet['AA6'] # cell in column AA row 6

Alternatives
------------

To my knowledge there are other python alternatives:

 * https://bitbucket.org/ericgazoni/openpyxl/
 * https://github.com/leegao/pyXLSX
