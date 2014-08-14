

from dragonfly import *; #CompoundRule,MappingRule,Key,IntegerRef,Grammer; 
 
release = Key("shift:up, ctrl:up")
	
	
class KeystrokeRule(MappingRule):


	mapping  = {  
     "[<n>] up":                         Key("up:%(n)d"),
     "[<n>] down":                       Key("down:%(n)d"),
 	"[<n>] left":                       Key("left:%(n)d"),
     "[<n>] right":                      Key("right:%(n)d"),
	"[<n>] page up":                    Key("pgup:%(n)d"),
     "[<n>] page down":                  Key("pgdown:%(n)d"),
     "<n> up (page | pages)":            Key("pgup:%(n)d"),
     "<n> down (page | pages)":          Key("pgdown:%(n)d"),
     "<n> left (word | words)":          Key("c-left:%(n)d"),
     "<n> right (word | words)":         Key("c-right:%(n)d"),
     "home":                             Key("home"),
     "end":                              Key("end"),
     "doc home":                         Key("c-home"),
     "doc end":                          Key("c-end"),
	 
#	"soot": 						Key("escape"),
#	"[<n>] joot":                      release + Key("space:%(n)d"),
	"[<n>] slap":                      release + Key("enter:%(n)d"),
     "[<n>] tab":                        Key("tab:%(n)d"),
     "[<n>] dij":                     release + Key("del/3:%(n)d"),  
     "ditch [<n> | this] (line|lines)": release + Key("home, s-down:%(n)d, del"),
     "[<n>] boot":                  release + Key("backspace:%(n)d"),
     "pop up":                           release + Key("apps"),

     "pinj":                            release + Key("c-v"),
     "duplicate <n>":                    release + Key("c-c, c-v:%(n)d"),
     "copy":                             release + Key("c-c"),
     "cut":                              release + Key("c-x"),
     "select all":                       release + Key("c-a"),
#   "[hold] appsj":                     Key("apps:down"),
#	"appsup":                     Key("apps:up,"),
     "[hold] shiff":                     Key("shift:down"),
     "shiffup":                    Key("shift:up"),
     "[hold] cont":                   Key("ctrl:down"),
     "contup":                  Key("ctrl:up"),
     "[hold] alt":                   Key("alt"),
     "altup":                  Key("alt:up"),
     "release [all]":                    release,
     "tux":                 		  Key("c-b"),

#     "say <text>":                       release + Text("%(text)s"),
     "mimic <text>":                     release + Mimic(extra="text"),

     "efyek":				 Key("f1"), 
     "efdo":				 Key("f2"), 
     "efse":				 Key("f3"), 
     "efchar":				 Key("f4"), 
     "efpanj":				 Key("f5"), 
     "efshish":				 Key("f6"), 
     "efhaf":				 Key("f7"), 
     "efhash":				 Key("f8"), 
     "efnoh":				 Key("f9"), 
     "efdah":				 Key("f10"), 
     "efyazdah":			 Key("f11"), 
     "efdavazdah":			 Key("f12"), 
     "efsizdah":			 Key("f13"), 
     "efcharda":			 Key("f14"), 
     "efpoonza":			 Key("f15") 
  
    }
	extras= [
                IntegerRef("n", 1, 100),
			   Dictation("text"),
                Dictation("text2"),
              ]
	defaults = {
                "n": 1,
                } 
				
keystroke = RuleRef(rule=KeystrokeRule(), name='keystroke')
#----------------------------------------------------------				
class LetterRule(MappingRule):
    exported = True
    mapping = {
        'ach': Key('a', static=True),
        'beegh': Key('b', static=True),
	    'kaj': Key('c', static=True),
        'daf': Key('d', static=True),
        'ish': Key('e', static=True),
        'fick': Key('f', static=True),
        'goeff': Key('g', static=True),
        'hoos': Key('h', static=True),
        'jack': Key('j', static=True),
        'kif': Key('k', static=True),
        'laam': Key('l', static=True),
        'meem': Key('m', static=True),
        'non': Key('n', static=True),
        'paf': Key('p', static=True),
        'queue': Key('q', static=True), #queue
        'rij': Key('r', static=True), 
        'saad': Key('s', static=True),
        'tinj': Key('t', static=True),
        'vazz': Key('v', static=True),
        'wek': Key('w', static=True), #doubleu
        'ex': Key('x', static=True), # ex
        'waay': Key('y', static=True), #waay
        'zed': Key('z', static=True),
		'esh': Key('e', static=True),
         'you': Key('u', static=True), #you
		'osh': Key('o', static=True),
		'ice': Key('i', static=True),
		
		
        'zero': Key('0'),
        'one': Key('1'),
        'two': Key('2'),
        'three': Key('3'),
        'four': Key('4'),
        'five': Key('5'),
        'six': Key('6'),
        'seven': Key('7'),
        'eight': Key('8'),
        'nine': Key('9'),

       'joot': Key('space'),
       'soot': Key("win:up, alt:up, escape"),

	
        'tab': Key('tab'),

        'amphi': Key('ampersand'),
        'quote': Key('apostrophe'),
        '[single] quote': Key('squote'),
        'saar': Key('asterisk'),
        'at': Key('at'),
        'bash': Key('backslash'),
        'tick': Key('backtick'),
        'bar': Key('bar'),
        'cart': Key('caret'),
        'coln': Key('colon'),
        'cooch': Key('comma'),
        'dollar': Key('dollar'),
        '(dot|period)': Key('dot'),
        'duote': Key('dquote'),
        'moss': Key('equal'),
        'bang': Key('exclamation'),
        'sharp': Key('hash'),
        'hyph': Key('hyphen'),
        'mice': Key('minus'),
        'pers': Key('percent'),
        'plus': Key('plus'),
        'qest': Key('question'),
        # Getting Invalid key name: 'semicolon'
        #'semic': Key('semicolon'),
        'sash': Key('slash'),

        'tilde': Key('tilde'),
        'zore': Key('underscore'),
        #'escape':Key('escape'),
        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'laip': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'raip': Key('rparen'),
    }

letter = RuleRef(rule=LetterRule(), name='letter')
letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

def executeLetter(letter):
    letter.execute()

def executeLetterSequence(letter_sequence):
    for letter in letter_sequence:
        letter.execute()

 #---------------------------------------------------------------------------
 # NormalMode
class VimKeystrokeRule(MappingRule):

    exported = False

    mapping = {
        "bala [<n>]": Key("k:%(n)d"),
        "poiin [<n>]": Key("j:%(n)d"),
        "chap [<n>]": Key("h:%(n)d"),
        "ross [<n>]": Key("l:%(n)d"),
    }
    extras   = [
        letter,
        letter_sequence,
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }
                 
#---------------------------- formating stuff ---------------------------
# Format: some_words
def format_score(dictation):          # Function name must start with 
	text = str(dictation)             # Get written-form of dictated text.
	words=[word.lower() for word in text.split(" ")]; 
	formatted_text = "_".join(words)  # Put underscores between words 
	Text(formatted_text).execute()


# Format: Some Words 
def format_title(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text(" ".join(words)).execute()

def format_jake(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text(" ".join(words)).execute()
	
	# Format: SomeWords 
def format_studley(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text("".join(words)).execute()
	
# Format: somewords
def format_one_word(dictation):
    text = str(dictation)
    words=[word.lower() for word in text.split(" ")]; 
    Text("".join(words)).execute()# Format: somewords
	
# Format: SOMEWORDS 
def format_upper_one_word(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    Text("".join(words)).execute()
	
def format_dotword(dictation):
    text = str(dictation)
    words=[word.lower() for word in text.split(" ")]; 
    Text(".".join(words)).execute()

def format_upper_score(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    print words
    Text("_".join(words)).execute()
	
def format_jive(dictation):
    text = str(dictation)
    words=[word.lower() for word in text.split(" ")]; 
    Text("-".join(words)).execute()

# Format: someWords
def format_java_method(dictation):
    text = str(dictation)
    words = text.split(" ")
    print words[0].lower()
    Text(words[0].lower() + "".join(w.capitalize() for w in words[1:])).execute()
	
# _ - ' ' '' '.'
# score hyphen jout nothing dot
# z h j n d

# ac_bc Ac_Bc AC_BC    ac_Bc
# kochik title bozorg camel
# k t b c 
class FormatRule(MappingRule): 
	mapping  = {
	"zake <dictation>":  Function(format_score),   # some_other_words
    "say <dictation>": Function(format_jake),  # some of the words
	"hake <dictation>":  Function(format_jive),   # some-other-words
	"dake <dictation>":  Function(format_dotword),   # some.other.words
    "jait <dictation>": Function(format_title),  # Some Of The Words
   "nate <dictation>": Function(format_studley),  # SomeOfTheWords
    "nake  <dictation>": Function(format_one_word),  # someotherwords
    "nabe <dictation>": Function(format_upper_one_word), # SOMEOTHERWORDS
    "zabe <dictation>": Function(format_upper_score), # SOME_OTHER_WORDS
	"nace <dictation>": Function(format_java_method) #  someOtherWords
	}
	extras   = [Dictation("dictation")]

#------------------------ shortened stuff - -------------------
avaz=False
class WindowsKeyRule1(CompoundRule):
	spec     = "woonj"
	extras = []
	def _process_recognition(self, node, extras):
		global avaz
		if avaz==False:
			Key("win:down").execute()
			Key("tab").execute()
			avaz=True
		else:
			Key("win:up").execute()
			avaz=False

class WindowsKeyRule3(CompoundRule):
	spec     = "wanj"
	extras = []
	def _process_recognition(self, node, extras):
		Key("alt:down").execute()
		Key("tab").execute()

			
class WindowsKeyRule2(CompoundRule):
	spec     = "winj <letterOrKeystroke>"
	extras = [Alternative(children=[keystroke,letter],name='letterOrKeystroke')]
	def _process_recognition(self, node, extras):
		Key("win:down").execute()
		ksr = extras["letterOrKeystroke"]
		ksr.execute()
		Key("win:up").execute()


#------------------------- repeating formatting and keystrokes---------------------------------
alternatives = []
alternatives.append(keystroke)
alternatives.append(RuleRef(rule=FormatRule()))
alternatives.append(letter)
alternatives.append(RuleRef(rule=VimKeystrokeRule()))


single_action = Alternative(alternatives)
sequence = Repetition(single_action, min=1, max=16, name="sequence")
	
class RepeatRule(CompoundRule):
    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,                 # Sequence of actions defined above.
                IntegerRef("n", 1, 100),  # Times to repeat the sequence.
               ]
    defaults = {
                "n": 1,                   # Default repeat count.
               }

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]   # A sequence of actions.
        count = extras["n"]             # An integer repeat count.
        for i in range(count):
            for action in sequence:
                action.execute()
        release.execute()
#-------------------------------------------------------------------

#---------------------------------------------------------------------------

gvim_other_rule = MappingRule(
    name = "gvim_tabulators",
    mapping = {
	    # window navigation commands
        "window left": Key("c-w,h"),
        "window right": Key("c-w,l"),
        "window up": Key("c-w,k"),
        "window down": Key("c-w,j"),

        # window creation commands
        "window split": Key("c-w,s"),
        "window vertical split": Key("c-w,v"),
        # tabulator navigation commands
        "tabulator next": Key("g,t"),
        "tabulator previous": Key("g,T")

        },
    extras = [
        ]
)


gvim_navigation_rule = MappingRule(
    name = "gvim_navigation",
    mapping = {
        "go first line": Key("g,g"),
        "go last line": Key("G"),
        "go old": Key("c-o"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "go <line>": Key("colon") + Text("%(line)s\n"),

        # searching
        "search <text>": Key("slash") + Text("%(text)s\n"),
        "search this": Key("asterisk"),
        "back search <text>": Key("question") + Text("%(text)s\n"),

        },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line", 1, 10000)
        ]
)


#---------------------------------------------------------------------------


#-----------


	
class NormalEnabler(CompoundRule):
    spec = "vim"                 
    def _process_recognition(self, node, extras):  
        vimGrammar.disable()
        print "vim enabled"

class VimEnabler(CompoundRule):
    spec = "vim"          
    def _process_recognition(self, node, extras):  
        normalGrammar.disable()
        vimGrammar.enable()
        print "vim disabled"    
		
#vimGrammar = Grammar("vim grammar")        
#vimGrammar.add_rule(NormalEnabler())
#vimGrammar.load()

# not_gvim_context = ~AppContext(executable="vim" ) &  ~AppContext(title="vim")  
# normalGrammar =  Grammar("normal grammar", context=not_gvim_context)   
normalGrammar =  Grammar("normal grammar")   
normalGrammar.add_rule(RepeatRule())   
normalGrammar.add_rule(gvim_other_rule)
normalGrammar.add_rule(gvim_navigation_rule) 
normalGrammar.add_rule(WindowsKeyRule1())
normalGrammar.add_rule(WindowsKeyRule2())
# normalGrammar.add_rule(WindowsKeyRule3())

#normalGrammar.add_rule(InsertModeEnabler())   
#normalGrammar.add_rule(InsertModeCommands())   
#normalGrammar.add_rule(ExModeEnabler())   
#normalGrammar.add_rule(KeystrokeRule()) 
#normalGrammar.add_rule(VimEnabler())
normalGrammar.load()                                   
print "grammer loaded"

def unload():
# global vimGrammar
#  if vimGrammar: vimGrammar.unload()
#  vimGrammar = None
  global normalGrammar
  if normalGrammar: normalGrammar.unload()
  normalGrammar = None
