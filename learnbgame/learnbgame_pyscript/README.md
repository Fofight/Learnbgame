# 待解决的问题：pdf转txt的python实现。



Other libraries
=====================

Pure Python
-----------

-  [reportlab](http://www.reportlab.org/)__

    如果您想以编程方式生成任意PDF，reportlab是必备软件。

-  [pyPdf](https://github.com/mstamy2/PyPDF2)__

    pyPdf is, in some ways, very full-featured. It can do decompression
    and decryption and seems to know a lot about items inside at least
    some kinds of PDF files. In comparison, pdfrw knows less about
    specific PDF file features (such as metadata), but focuses on trying
    to have a more Pythonic API for mapping the PDF file container
    syntax to Python, and (IMO) has a simpler and better PDF file
    parser.  The Form XObject capability of pdfrw means that, in many
    cases, it does not actually need to decompress objects -- they
    can be left compressed.

-  [pdftools](http://www.boddie.org.uk/david/Projects/Python/pdftools/index.html)__

    pdftools feels large and I fell asleep trying to figure out how it
    all fit together, but many others have done useful things with it.

-  [pagecatcher](http://www.reportlab.com/docs/pagecatcher-ds.pdf)__

    My understanding is that pagecatcher would have done exactly what I
    wanted when I built pdfrw. But I was on a zero budget, so I've never
    had the pleasure of experiencing pagecatcher. I do, however, use and
    like `reportlab <http://www.reportlab.org/>`__ (open source, from
    the people who make pagecatcher) so I'm sure pagecatcher is great,
    better documented and much more full-featured than pdfrw.
    
-   [pdfrw](https://github.com/pmaupin/pdfrw)__

    pdfrw is a pure Python library that reads and writes PDFs

-   [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/index.html)__

    This looks like a useful, actively-developed program. It is quite
    large, but then, it is trying to actively comprehend a full PDF
    document. From the website:

    "PDFMiner is a suite of programs that help extracting and analyzing
    text data of PDF documents. Unlike other PDF-related tools, it
    allows to obtain the exact location of texts in a page, as well as
    other extra information such as font information or ruled lines. It
    includes a PDF converter that can transform PDF files into other
    text formats (such as HTML). It has an extensible PDF parser that
    can be used for other purposes instead of text analysis."

non-pure-Python libraries
-------------------------

-  [pyPoppler](https://launchpad.net/poppler-python/)__ can read PDF
   files.
-  [pycairo](http://www.cairographics.org/pycairo/)__ can write PDF
   files.
-  [PyMuPDF](https://github.com/rk700/PyMuPDF)_ high performance rendering
   of PDF, (Open)XPS, CBZ and EPUB

Other tools
-----------

-  [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)__ is a wonderful command
   line tool for basic PDF manipulation. It complements pdfrw extremely
   well, supporting many operations such as decryption and decompression
   that pdfrw cannot do.
-  [MuPDF](http://www.mupdf.com/)_ is a free top performance PDF, (Open)XPS, CBZ and EPUB rendering library
   that also comes with some command line tools. One of those, ``mutool``, has big overlaps with pdftk's - 
   except it is up to 10 times faster.

Related Projects
----------------


 * <a href="http://www.foolabs.com/xpdf/">xpdf</a>
 * <a href="http://pdfbox.apache.org/">pdfbox</a>
 * <a href="http://mupdf.com/">mupdf</a>
 * <a href="https://github.com/pdfminer/pdfminer.six">pdfminer.six</a>

