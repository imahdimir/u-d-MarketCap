"""

    """

from pathlib import Path

from githubdata import GitHubDataRepo as GDR
from mirutil.df import assert_no_duplicated_rows_in_df_cols_subset
from mirutil.df import reorder_df_cols_as_a_class_values
from mirutil.df import save_df_as_prq
from namespace_mahdimir.tse import DMarketCap
from namespace_mahdimir.tse import DNomPriceCol
from namespace_mahdimir.tse import DOutstandingSharesCol

from main import c
from main import fpn
from main import gdu

cnp = DNomPriceCol()
cdo = DOutstandingSharesCol()

def get_all_nominal_prices() :
    """ get all nominal prices """
    gdr = GDR(gdu.nom_price_s)
    df = gdr.read_data()
    df = df.astype('string')
    return df

def keep_relevant_cols_from_nom_prices(df) :
    cols = {
            c.ftic    : None ,
            c.d       : None ,
            c.jd      : None ,
            cnp.nclos : None ,
            }

    df = df[cols.keys()]

    return df

def get_all_outstanding_shares() :
    """ get all outstanding shares """
    gdr = GDR(gdu.os_s)
    df = gdr.read_data()
    df = df.astype('string')
    return df

def cal_market_cap(df) :
    """ calculate market cap """
    df[cnp.nclos] = df[cnp.nclos].astype('float64')

    df[cdo.os] = df[cdo.os].astype('Int64')

    df[c.mktcap] = df[cnp.nclos] * df[cdo.os]
    df[c.mktcap] = df[c.mktcap].astype('Int64')

    return df

def main() :
    pass

    ##

    df = get_all_nominal_prices()

    ##
    df = keep_relevant_cols_from_nom_prices(df)

    ##
    dfo = get_all_outstanding_shares()

    ##
    df = df.merge(dfo , how = 'inner')

    ##
    df = cal_market_cap(df)

    ##
    df = reorder_df_cols_as_a_class_values(df , DMarketCap)

    ##
    df = df.astype('string')

    ##
    df = df.sort_values(by = [c.d , c.ftic] , ascending = [False , True])

    ##
    assert_no_duplicated_rows_in_df_cols_subset(df , [c.ftic , c.d])

    ##
    save_df_as_prq(df , fpn.t0)

    ##

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
