# Metadata for humans

Metadata extract metadata from files, without having to deal with exotic library compilation, complex API or multiple libraries. Give Metadata a file and it will return a dictionnary with your precious metadata.

    >>> import metadata
    >>> metadata = metadata.extract(file)
    >>> metadata.get('creation_date')
    datetime.datetime(2010, 9, 28, 7, 51, 8)
    >>> metadata.get('title')
    ...

## Features

Extract metadata from almost any kind of files : video, music and other.

## Installation

To install metadata, use pip :

	$ pip install metadata

## Acknowledgement

Metadata uses [hachoir](http://hachoir.org) behind the scenes.
