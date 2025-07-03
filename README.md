# CUT&Tag analysis pipeline (works for CUT&Run as well)
## Author: Zhen Y
Modified from https://github.com/fl-yu/CUT-RUNTools-2.0
1. Should install CUT-RUNTools-2.0 through conda first and activate env
e.g.:
source ~/software/miniforge3/bin/activate cutrun
2. run script:
ID=sample1
run_bulkModule.sh ${ID}.json ${ID}

### json file generation python script: CUTRUN_JSON_generator.py
Notes: automatically generate sample json file with specify sample meta information:
usage example:
ID=sample1
python ./CUTRUN_JSON_generator.py bulk-config.hg38.json ./${ID}.json fastq_directory:::/path_to_fastq/sample_id workdir:::/output_folder/${ID} fastq_sequence_length:::150 organism_build:::hg38

then run main script:
run_bulkModule.sh ${ID}.json ${ID}

### json file bulk-config.json
Notes: change organism_build option accordingly (mm10/hg38); experiment_type option can be CUT&Tag or CUT&Run; keep frag_120 to FALSE when running CUT&Tag

