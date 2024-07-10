from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

KIND = "fundation"


THIS_DIR = Path(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "amo-grammar"):
    SRC_DIR = SRC_DIR.parent

CFG_DIR = SRC_DIR / "grammar-n-doc" / "config" / KIND

DOC_DIR = (
    SRC_DIR
    / "grammar-n-doc" / "fr" / "content" / "types" / "new-var" / KIND
)


# --------------- #
# -- LET'S GO! -- #
# --------------- #

for cfgfile in CFG_DIR.glob("*.amo.cfg"):
    print(Path(cfgfile.stem).stem)

for docfile in DOC_DIR.glob("*.txt"):
    print(docfile.stem)
