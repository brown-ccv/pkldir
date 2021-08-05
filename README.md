# pkldir

# 1 Overview
This is small utility for encoding and decoding .pdf, .docx, .md, and .txt files in binary form. The use case for this package is to take an input directory and "pickle" its contents, and save them in a new directory. The "pickled" directory's contents can then no longer be easily read by user; instead, a user intending to read the contents of the pickled directory can do so using the `decode()` function from this package. 

The key use case for this package is to encode the contents of a directory with text documents so that they cannot be easily read using standard applications (e.g., MS Word, Adobe Reader, etc.). The encoded text documents _can_ be easily read using this package

# 2 Installation
This package is not currently hosted on PyPI, so doing a local install of this Git repository is the recommended method.

```bash
cd <path/to/this/directory/>
python3 setup.py sdist bdist_wheel
pip3 install <path/to/this/directory/>
```

# 3 Basic Usage 
There are basically only two kinds of usage for this package: 
    
    1. Encoding a directory of text documents
    2. Decodeing and ingesting the contents of previously encoded documents

The encoding portion would typically be done once on a directory of documents. And the decoding portion would be done any time that one wants to work with the content of the encoded documents. 

## 3.1 Encoding
The encoding can be done in a few ways, but the most basic, is simply to use the `pkldir` command after you have installed this package. Here is an example:

```bash
pkldir my_document_dir/
```

The above example creates a new directory called `my_document_dir-pkl`, which now contains a base64-encoded and pickled version of each of the text documents in the original `my_document_dir`.


## 3.2 Decoding
In order to decode a file previously created with the `pkldir` command line script, we need to use the `decode()` function from the `pkldir` package. The example Python script below illustrates this. 


```python
import pkldir 

text = decode('<path/to/myfile.pkl>')
```

In the above example, the `text` object will be a cleartext string containing the contents of the pickled file `myfile.pkl`. The object `text` will be of type `str` and can then be manipulated an explored just like any other Python `str`.