from setuptools import setup, find_packages

hipen_e_dot="-e ."
def get_requirements(file_path):
    """
    This function reads a requirements file and returns a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any comments or empty lines
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    
    if hipen_e_dot in requirements:
        requirements.remove(hipen_e_dot)
    
    return requirements




setup(
    name='MLProject',
    version='0.0.1',
    author='Biprayan',
    author_email='c.biprayan@op.iitg.ac.in',
    # install_requires=[
    #     'numpy',
    #     'pandas',
    #     'scikit-learn',
    #     'matplotlib',
    #     'seaborn',
    #     'scipy',
    #     'tqdm',
    # ],
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
)