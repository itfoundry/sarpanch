#!/usr/bin/python

FAMILY_NAME = 'Sarpanch'

STYLE_NAMES = [
    'Regular',
    'Medium',
    'SemiBold',
    'Bold',
    'ExtraBold',
    'Black',
]

UFOIG_ARGS = [
    # '-kern',
    '-mark',
    # '-hint',
    '-flat',
    '-mkmk',
    '-clas',
    '-indi',
]

MATCH_mI_OFFSETS_DICT = {
    'Regular':   0,
    'Medium':    0,
    'SemiBold':  0,
    'Bold':      0,
    'ExtraBold': 0,
    'Black':     0,
}

MAKEOTF_ARGS = [
    '-r',
    '-shw',
]

OUTPUT_DIR = '/Library/Application Support/Adobe/Fonts'
