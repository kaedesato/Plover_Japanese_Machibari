KEYS = (
'*-', 'S-', 'T-', 'K-', 'H-', 'I-', 'A-', 'O-', 'k-', 'n-', 't-', 'h-',
'#',
'-*', '-S', '-T', '-K', '-H', '-I', '-A', '-O', '-k', '-n', '-t', '-h',
)

IMPLICIT_HYPHEN_KEYS = ('#')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*-')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Keyboard': {
        '*-' : 'q',
        'S-' : 'a',
        'T-' : 'w',
        'K-' : 's',
        'H-' : 'e',
        'I-' : 'd',
        'A-' : 'c',
        'O-' : 'v',
        'k-' : 'r',
        'n-' : 'f',
        't-' : 't',
        'h-' : 'g',
        '#'  : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        '-*' : 'p',
        '-S' : ';',
        '-T' : 'o',
        '-K' : 'l',
        '-H' : 'i',
        '-I' : 'k',
        '-A' : 'm',
        '-O' : 'n',
        '-k' : 'u',
        '-n' : 'j',
        '-t' : 'y',
        '-h' : 'h',
        'arpeggiate': 'space',
        },
        'Gemini PR': {
        '*-' : 'S1-',
        'S-' : 'S2-',
        'T-' : 'T-',
        'K-' : 'K-',
        'H-' : 'P-',
        'I-' : 'W-',
        'A-' : 'A-',
        'O-' : 'O-',
        'k-' : 'H-',
        'n-' : 'R-',
        't-' : '*1',
        'h-' : '*3',
        '#'  : ('#1', '#2'),
        '-*' : '-T',
        '-S' : '-S',
        '-T' : '-L',
        '-K' : '-G',
        '-H' : '-P',
        '-I' : '-B',
        '-A' : '-U',
        '-O' : '-E',
        '-k' : '-F',
        '-n' : '-R',
        '-t' : '*2',
        '-h' : '*4',
        'no-op' : ('D', 'Z',),
        }
        }


DICTIONARIES_ROOT = 'asset:plover_japanese_machibari:dictionaries'
DEFAULT_DICTIONARIES = ('kana.json')
