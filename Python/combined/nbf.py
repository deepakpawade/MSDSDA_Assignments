import nbformat

# Reading the notebooks
n1 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\assignment_1.ipynb", 4)
n2 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\assignment_2.ipynb", 4)
n31 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\list.ipynb", 4)
n32 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\string.ipynb", 4)
n33 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\tuple.ipynb", 4)
n41 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\dictionary.ipynb", 4)
n42 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\set.ipynb", 4)
n5 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\assignment_5.ipynb", 4)
n6 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\assignment_6.ipynb", 4)
n7 = nbformat.read("D:\MSDataScience\Assignments\MSDSDA_Assignments\Python\combined\\assignment_7.ipynb", 4)



# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=n1.metadata)

# Concatenating the notebooks
final_notebook.cells = n1.cells +n2.cells+n31.cells+n32.cells+n33.cells+n41.cells+n42.cells+n5.cells+n6.cells+n7.cells

# Saving the new notebook 
nbformat.write(final_notebook, 'final_notebook.ipynb')

# nbmerge assignment_1.ipynb assignment_2.ipynb list.ipynb string.ipynb tuple.ipynb dictionary.ipynb set.ipynb assignment_5.ipynb assignment_6.ipynb assignment_7.ipynb