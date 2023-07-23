from setuptools import setup, find_packages

def get_requirements(requirements_file):
    with open(requirements_file) as file:
        lines = [line.rstrip() for line in file]
    return lines


setup(
    name='word-pattern-switcher',
    version='0.1.0',
    author='ZAIDI Amar',
    author_email='osjfvhng16@gmail.com',
    description='This package uses an xlsx file, to insert each row in a .docx document, parameters can change using a .env file.',
    packages=find_packages(),  # Automatically find all packages
    # Add any additional dependencies
    install_requires=["python-docx",
"pandas",
"python-dotenv",
"pyinstaller",
"openpyxl"],
    zip_safe=False,
)