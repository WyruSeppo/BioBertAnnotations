<<<<<<< HEAD
from dataMethods import *

tsv_file_path = "spore_formers_proteinIds"
annotated_df = annotate_tsv(tsv_file_path)
=======
from dataMethods import *

tsv_file_path = "spore_formers_proteinIds"
annotated_df = annotate_tsv(tsv_file_path)
>>>>>>> 49b9adc1 (init)
annotated_df.to_csv('output.txt', sep='\t', index=False)