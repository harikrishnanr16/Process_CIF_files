from gemmi import cif

import pandas as pd
import glob 
import os 

os.makedirs("Sheet_info",exist_ok=True)

for i in glob.glob("/home/hari/Pdb/*.cif"):

    doc = cif.read_file(i)

    block = doc.sole_block()
    # print(block.name)


    d={"Pdb_id":block.name,
        "sheet_id":list(block.find_loop('_struct_sheet_range.sheet_id')),
        "beg_label_comp_id":list(block.find_loop('_struct_sheet_range.id')),
        "beg_label_comp_id":list(block.find_loop('_struct_sheet_range.beg_label_comp_id')),
        "beg_label_asym_id":list(block.find_loop('_struct_sheet_range.beg_label_asym_id')),
        "beg_label_seq_id":list(block.find_loop('_struct_sheet_range.beg_label_seq_id')),
        "_beg_PDB_ins_code":list(block.find_loop('_struct_sheet_range.pdbx_beg_PDB_ins_code')),
        "end_label_comp_id":list(block.find_loop('_struct_sheet_range.end_label_comp_id')),
        "end_label_asym_id":list(block.find_loop('_struct_sheet_range.end_label_asym_id')),
        "end_label_seq_id":list(block.find_loop('_struct_sheet_range.end_label_seq_id')),
        "end_PDB_ins_code":list(block.find_loop('_struct_sheet_range.pdbx_end_PDB_ins_code')),
        "beg_label_comp_id":list(block.find_loop('_struct_sheet_range.beg_auth_comp_id')),
        "beg_auth_asym_id":list(block.find_loop('_struct_sheet_range.beg_auth_asym_id')),
        "beg_auth_seq_id":list(block.find_loop('_struct_sheet_range.beg_auth_seq_id')),
        "end_auth_comp_id":list(block.find_loop('_struct_sheet_range.end_auth_comp_id')),
        "end_auth_asym_id":list(block.find_loop('_struct_sheet_range.end_auth_asym_id')),
        "end_auth_seq_id":list(block.find_loop('_struct_sheet_range.end_auth_seq_id'))
        
        }

    df=pd.DataFrame(d)
    # print(df)
    df.to_csv("/home/hari/Pdb/Sheet_info/"+block.name+"_Sheet_info.txt",sep="\t")
    print(block.name," Done!!!!")

    # print(df)









