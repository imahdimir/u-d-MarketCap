"""

    """

from pathlib import Path

from githubdata.utils import clone_with_overwrite_a_repo_return_gdr_obj
from githubdata.utils import push_to_github_by_code_url
from githubdata.utils import replace_old_data_with_new_and_iso_jdate_title

from main import fpn
from main import gdu

def main() :
    pass

    ##

    # update 0 data
    gdr = clone_with_overwrite_a_repo_return_gdr_obj(gdu.mktcap_t)

    ##
    replace_old_data_with_new_and_iso_jdate_title(gdr , fpn.t0)

    ##
    push_to_github_by_code_url(gdr , gdu.slf)

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##

    ##
