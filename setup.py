#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
DYNA ASCII format: read and write support for ObsPy.
ITACA ASCII format: read-only support for ObsPy.

The obspy_dyna package contains methods in order to read and write
seismogram files in the DYNA 1.0 format as defined by INGV Milano

DYNA 1.0 format specifications are available at the following URL:

http://itaca.mi.ingv.it/static_italy_20/doc/Manual_ITACA_beta_version.pdf

For more information visit http://www.obspy.org
and http://itaca.mi.ingv.it

:copyright:
    The ITACA Development Team (itaca@mi.ingv.it)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
import inspect
import os
from setuptools import setup, find_packages


def get_package_data():
    """
    Returns a list of all files needed for the installation.
    """
    filenames = []
    root_dir = os.path.join(os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe()))), "obspy_dyna")
    # Recursively include all files in these folders:
    folders = [os.path.join(root_dir, "tests", "data")]
    for folder in folders:
        for directory, _, files in os.walk(folder):
            for filename in files:
                # Exclude hidden files.
                if filename.startswith("."):
                    continue
                print filename
                filenames.append(os.path.relpath(
                    os.path.join(directory, filename),
                    root_dir))
    return filenames


setup_config = dict(
    name='obspy_dyna',
    version="0.1.0",
    description="DYNA format read/write module for ObsPy",
    author="Emiliano Russo and Rodolfo Puglia",
    author_email="itaca@mi.ingv.it",
    url="http://itaca.mi.ingv.it",
    packages=find_packages(),
    license="GNU General Public License, version 3 (GPLv3)",
    platforms="OS Independent",
    install_requires=["obspy"],
    package_data={
        "obspy_dyna": get_package_data()},
    entry_points={
        "obspy.plugin.waveform": [
            "DYNA = obspy_dyna.core",
            "ITACA = obspy_dyna.core"],
        "obspy.plugin.waveform.DYNA": [
            "isFormat = obspy_dyna.core:isDYNA",
            "readFormat = obspy_dyna.core:readDYNA",
            "writeFormat = obspy_dyna.core:writeDYNA"],
        "obspy.plugin.waveform.ITACA": [
            "isFormat = obspy_dyna.core:isITACA",
            "readFormat = obspy_dyna.core:readITACA"]
    }
)


if __name__ == "__main__":
    setup(**setup_config)
