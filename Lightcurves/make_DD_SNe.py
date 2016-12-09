#!/usr/bin/env python

from __future__ import print_function, division

import numpy as np
import sys
import os
import cPickle

try:
    from lsst.sims.catUtils.utils import SNIaLightCurveGenerator
    from lsst.sims.catUtils.baseCatalogModels import GalaxyTileObj
except:
    print("Could not load lsst.sims")
    print("Did you remember to setup sims with EUPS using:")
    print()
    print("source eups-setups.sh")
    print("setup lsst_sims")
    sys.exit(0)

# Need a database connection via:
# ssh -L 51433:fatboy.phys.washington.edu:1433 gateway.astro.washington.edu

if __name__ == '__main__':

    # Twinkles: RA 53.01, Dec -27.44
    raRange = (60.0, 65.0)
    decRange = (-15.0, -12.0)
    bandpass = ('u', 'g', 'r', 'i', 'z')
    opsimdb_filename = "minion_1016_sqlite.db"

    catalogdb = GalaxyTileObj()
    sn_gen = SNIaLightCurveGenerator(catalogdb, opsimdb_filename)

    sn_pointings = sn_gen.get_pointings(raRange, decRange, bandpass=bandpass)

    sn_lc_dict, sn_truth_dict = sn_gen.light_curves_from_pointings(sn_pointings,
                                                                   lc_per_field=1000)
    print("Number of light curves: ", len(sn_lc_dict.keys()))

    f_out = open("sne_dd_lightcurves.pkl", "w")
    cPickle.dump((sn_lc_dict, sn_truth_dict), f_out)
    f_out.close()


