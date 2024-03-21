FILE=mybitmap.py

INPUT_PATH=data/data
INPUT=animals_small.txt
OUTPUT_PATH=results
SORTED=f

CINPUT=${OUTPUT_PATH}/animals_small.txt
COUTPUT_PATH=results
COMPRESSION=WAH
WORD_SIZE=64

run:
	python3 ${FILE} i ${INPUT_PATH}/${INPUT} ${OUTPUT_PATH} ${SORTED}
	python3 ${FILE} c ${CINPUT} ${COUTPUT_PATH} ${COMPRESSION} ${WORD_SIZE}
