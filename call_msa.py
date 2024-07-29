# Calls MUSCLE on the results of the BLAST search.
# A. Vargas Richards, NIAB 29.07.2024

import subprocess, os

def call_msa(results_folder):
    for 