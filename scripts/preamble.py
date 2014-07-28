import matplotlib
matplotlib.use('pgf')

preamble = {
    'text.usetex': True,
    "pgf.rcfonts": False,
    "text.latex.unicode": True,
    'font.size': 22,
    "pgf.preamble": [
        r"\usepackage[T1]{polski}",
        r"\usepackage{mathspec}",
        r"\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Arno Pro}",
        r"\setmathrm{Arno Pro}",
    ]
}
matplotlib.rcParams.update(preamble)
