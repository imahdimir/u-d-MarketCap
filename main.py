"""

    """

from pathlib import Path

from giteasy.github_repo import resolve_github_url
from mirutil.dirr import DefaultDirs
from mirutil.run_modules import clean_cache_dirs
from mirutil.run_modules import run_modules_from_dir_in_order
from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu

# namespace     %%%%%%%%%%%%%%%
c = tse_ns.Col()

# class         %%%%%%%%%%%%%%%
class GDU :
    g = tgdu.GitHubDataUrl()

    slf = tgdu.m + 'u-d-MarketCap'
    slf = resolve_github_url(slf)

    nom_price_s = g.nom_price
    os_s = g.os
    mktcap_t = g.mktcap

class Dirs(DefaultDirs) :
    pass

class FPN :
    dyr = Dirs()

    # temp data files
    t0 = dyr.td / 't0.prq'

# class instances   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
gdu = GDU()
dyr = Dirs()
fpn = FPN()

def main() :
    pass

    ##
    run_modules_from_dir_in_order(dyr.md)

    ##
    clean_cache_dirs()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


def test() :
    pass

    ##

    ##

    ##

##
