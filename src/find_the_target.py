import sqlite3 
import pandas as pd
from rdkit import Chem
def db_search(path, ligand_id):
    conn = sqlite3.connect(path) 
    query = f""" 
    SELECT DISTINCT
        td.pref_name,
        td.target_type,
        td.chembl_id,
        act.standard_type,
        act.standard_relation,
        act.standard_value,
        act.standard_units
    FROM molecule_dictionary md
    JOIN activities act ON md.molregno = act.molregno
    JOIN assays ass ON act.assay_id = ass.assay_id
    JOIN target_dictionary td ON ass.tid = td.tid
    WHERE md.chembl_id = ?
    AND act.standard_value IS NOT NULL
    AND act.standard_units = 'nM'
    """ 
    df = pd.DataFrame(pd.read_sql_query(query, conn, params=(ligand_id,))) 
    conn.close()
    return df
def convert(path, smiles):
    mol = Chem.MolFromSmiles(smiles) 
    inchikey = Chem.MolToInchiKey(mol) 
    conn = sqlite3.connect(path) 
    query = f""" 
    SELECT
        md.chembl_id,
        cs.standard_inchi_key
    FROM compound_structures cs
    JOIN molecule_dictionary md ON cs.molregno = md.molregno
    WHERE cs.standard_inchi_key = ?;
    """
    result = conn.execute(query, (inchikey,)).fetchone()
    if result is None:
        conn.close()
        raise ValueError("Molecule was not found in the ChEMBL database.")
    conn.close()
    return result[0]
def find_the_target(path, ligand):
    if "CHEMBL" not in ligand:
        ligand = convert(path, ligand)
    df = db_search(path, ligand)
    return df