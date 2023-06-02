from ocpa.objects.log.importer.csv import factory as csv_import_factory
import os
import sys
from ocpa.objects.log.importer.ocel import factory as ocel_import_factory
from ocpa.algo.discovery.ocpn import algorithm as ocpn_discovery_factory
from ocpa.visualization.oc_petri_net import factory as ocpn_vis_factory
import pandas as pd
sys.path.append(".")
from preprocessing import PreprocessCSV, solve_ot_syntaxerror
from token_based_replay import OC_Conformance, OCtokenbasedreplay
from translation import ELtranslate_OCPA2PM4PY,PNtranslate_OCPA2PM4PY

prefix1 = '/Users/jiao.shuai.1998.12.01outlook.com/Downloads/OCEL/csv/'
prefix2 = './sample_logs/csv/'
suffix = '.csv'
ocpafile = ['BPI2017-Final']
ocelstandardfile = ['github_pm4py','o2c','p2p','recruiting','running-example','transfer_order','windows_events']
storedpath = [path+'processed' for path in ocelstandardfile]

#handle ocel standard
for path in ocelstandardfile[1:]:
    print('hi',path)
    ocel = solve_ot_syntaxerror(prefix1+path+suffix,prefix1+path+'processed'+suffix)
    ocpn = ocpn_discovery_factory.apply(ocel, parameters={"debug": False})
    print('OCtokenbased-------',OCtokenbasedreplay(ocpn,ocel))
    print('Im here~~~~~~~~~~~~~')
    print('flattened TBR-------',OC_Conformance(PNtranslate_OCPA2PM4PY(ocpn),ELtranslate_OCPA2PM4PY(ocel)))

#handle BPI
'''ocel = PreprocessCSV(prefix2+ocpafile[0]+suffix,'ELocpa') 
ocpn1 = ocpn_discovery_factory.apply(ocel, parameters={"debug": False})'''