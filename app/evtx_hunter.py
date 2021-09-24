import argparse
import os
import vars
import dash
from helpers.evtx_loader import EvtxLoader
from helpers import utils
from graphing import table, histogram
import dash_html_components as html
import dash_core_components as dcc
from datetime import date, datetime


def main():
    logger = utils.setup_logger()
    logger.info("started evtx-hunter")

    vars.PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    vars.TMP_DIR = vars.PROJECT_ROOT_DIR + "/../tmp/"
    vars.EXTERNAL_DIR = vars.PROJECT_ROOT_DIR + "/../external/"
    vars.RULE_DIR = vars.PROJECT_ROOT_DIR + "/../rules/"

    parser = argparse.ArgumentParser(description="Dump a binary EVTX file into XML.")
    parser.add_argument("evtx_folder", type=str,
                        help="Path to the Windows EVTX event log file folder")

    args = parser.parse_args()

    utils.remove_all_tmp_json_files()
    utils.load_event_id_mappings()

    evtxloader = EvtxLoader(args.evtx_folder)
    evtxloader.load_evtx_files()

if __name__ == "__main__":
    main()
