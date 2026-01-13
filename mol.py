from rdkit import Chem
from rdkit.Chem import AllChem
from ase.io import read, write


mol = Chem.MolFromSmiles('C(C1=CC2C=CC=C(C(CCCCCCCCCCCCCC)C)C=2C=C1)(CCCCCCCCCCCC)C')  # dodecane
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())
Chem.MolToMolFile(mol, '3.mol')
ase_mol = read('3.mol')
ase_mol.write('3.pdb')