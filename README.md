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

Notes: -M: analysis mode: input or peak. input: inputs are input fastq and only generate input bam file and bigwig track; peak: input files are peaks fastq.
       -a: adapters has 4 options: stranded_illumina or illumina or none or BGI; users can provide their own adapter sequences, if two ends have different adapter seqs, use comma to separate them, e.g., ATGC,GTAC
       -B: TRUE for broadpeak and FALSE for narrow one.
       -P (optional): primary assembly bed file. Only keep primary assembly e.g.:


### QC R script: chipseq_qc.R
Notes: require ChIPQC R package, currently support hg38 only (modify R script with mm10 UCSC TxDb package to adapt mouse data)


