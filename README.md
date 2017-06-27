# analysis_tools
Various io, FITS file-handling, conversion, etc. tools for astronomical analysis work. 

## convert
Time and unit conversions, often just wrapping `astropy` functions in a format I can better remember. 

## fits
Modules for handling FITS files. Many of these can be not only imported, but also executed on the command line.
```
# To move FITS files based on a header key value:
>>> python fetch_fits_by_keyvalue.py '<keyvalue>' '<keyword>' '<fits type>' '<orig_dir/>' '<dest_dir/>'

# To print the key value of a given keyword, 'filter', for example:
>>> python get_keyval.py --f 'example.fits' --kw 'filter'

# To print out the HST dataset name of all FITS files in a directory:
>>> python get_datasetname.py

# To sort your FITS files by a keyword, so that they will be stored in directories named for that keyword:
>>> python sort_fits_by_keyword.py '<keyword>'
```

## io
Miss IDL's `readcol` and `writecol`?  Try `io.readcol` and `io.writecol`.  
You can set the line number (not counting blank lines) that a header begins and the data begins. For funzies, I wrote `nosetests` in the "tests" directory for these functions. 

## jitter
Some plotting and analysis scripts for the `JIF` and `JIT` engineering FITS files for the HST/WFC3 instrument. 

## tables
Ready to burn `astropy.table`?  In `tables.bybass_table` find the functions

* `decompose_table`, which will take an `astropy.table.Table` and convert it to a `collections.OrderedDict`.

* `build_table`, which takes columns and column names and creates an `astropy.table.Table` because I can never remember the `astropy` syntax (and that "names" is really "colnames", ugh).  

* `antitable`, which is actually a decorator wrapping `decompose_table`. For any function returning an `astropy.table.Table`, use the dectorator to convert it to a `collections.OrderedDict`. For funzies. 

```
    @antitable
    out = function_creating_table(args)  # "out" is now an OrderedDict
```

## where
Playing with `np.where`, looking for ways to wrap it to be more IDL-like.  
