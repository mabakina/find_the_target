\# Find the Target



A cheminformatics tool for identifying experimentally observed targets of a ligand using the ChEMBL database.



The ligand can be provided either as a \*\*ChEMBL ID\*\* or as a \*\*SMILES\*\* string. The tool searches the ChEMBL SQLite database and returns a table containing the identified targets and experimental activity data.



\## Features



\* Search for ligand targets using a \*\*ChEMBL ID\*\*

\* Search for ligand targets using a \*\*SMILES\*\* representation

\* Convert SMILES to a ChEMBL ID using the molecular structure

\* Retrieve experimentally measured activity data from ChEMBL

\* Display target information and activity values in a pandas DataFrame

\* Filter results by target type, such as single-protein targets



\## How It Works



The workflow is:



```text

Ligand (ChEMBL ID or SMILES)

&#x20;             ↓

&#x20;      ChEMBL SQLite database

&#x20;             ↓

&#x20;    Search for experimental

&#x20;       ligand–target data

&#x20;             ↓

&#x20;    Target information +

&#x20;      activity values

&#x20;             ↓

&#x20;       pandas DataFrame

```



When a SMILES string is provided, the molecule is converted to an InChIKey using RDKit. The InChIKey is then used to identify the corresponding compound in the ChEMBL database.



\## Input



The main function is:



```python

find\_the\_target(path, ligand)

```



\### Arguments



\*\*`path`\*\*

Path to the local ChEMBL SQLite database.



\*\*`ligand`\*\*

The ligand can be specified in one of two ways:



\* ChEMBL compound ID, e.g. `CHEMBL25`

\* SMILES string, e.g. `CC(=O)OC1=CC=CC=C1C(=O)O`



\## Output



The function returns a pandas DataFrame containing information about experimentally observed ligand–target interactions.



The output includes:



| Column              | Description                                                   |

| ------------------- | ------------------------------------------------------------- |

| `pref\_name`         | Preferred name of the target                                  |

| `target\_type`       | Type of the target                                            |

| `chembl\_id`         | ChEMBL ID of the target                                       |

| `standard\_type`     | Type of activity measurement, e.g. IC50 or Ki                 |

| `standard\_relation` | Relation between the measured value and the reported activity |

| `standard\_value`    | Measured activity value                                       |

| `standard\_units`    | Units of the activity value                                   |



\## Installation



This project requires \*\*Python 3.11\*\*.



Install the required packages using:



```bash

pip install -r requirements.txt

```



The project was tested with:



\* Python 3.11.15

\* pandas 3.0.3

\* RDKit 2025.09.6



\## ChEMBL Database



The project requires a local \*\*ChEMBL SQLite database\*\*.



The database is not included in this repository because of its size.



Download a ChEMBL database release and provide the path to the SQLite database when calling the function.



For example:



```python

result = find\_the\_target(

&#x20;   "chembl\_36.db",

&#x20;   "CHEMBL25"

)

```



\## Usage



\### Using a ChEMBL ID



```python

from find\_the\_target import find\_the\_target



result = find\_the\_target(

&#x20;   "chembl\_36.db",

&#x20;   "CHEMBL25"

)



print(result.head())

```



\### Using a SMILES string



```python

from find\_the\_target import find\_the\_target



result = find\_the\_target(

&#x20;   "chembl\_36.db",

&#x20;   "CC(=O)OC1=CC=CC=C1C(=O)O"

)



print(result.head())

```



\### Filtering single-protein targets



The returned DataFrame can be further processed using pandas.



For example:



```python

single\_protein\_targets = result\[

&#x20;   result\["target\_type"] == "SINGLE PROTEIN"

]

```



\## Example



A complete usage example is provided in:



`examples/example.ipynb`



The notebook demonstrates:



1\. Searching for targets using a ChEMBL ID

2\. Searching for targets using a SMILES string

3\. Inspecting the types of identified targets

4\. Filtering the results to single-protein targets



\## Project Structure



```text

find\_the\_target/

│

├── src/

│   └── find\_the\_target.py

│

├── examples/

│   └── example.ipynb

│

├── README.md

├── requirements.txt

└── .gitignore

```



\## Related Project



This project solves the inverse problem of ligand selection.



If a target protein is known and the goal is to identify potential ligands for it, see my related project:



\*\*Find the Ligand\*\*



\## License



This project is intended for educational and research purposes.



