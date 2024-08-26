# this script will show versions of all installed packages

import subprocess
import sys

# get Python version
print("="*40, "Python Version", "="*40)
print(sys.version)

def get_packages_info(verbose=False):
    # get the installed packages
    print("="*40, "Package Information", "="*40)
    try:
        # get the package information
        packages = subprocess.check_output(["pip", "list"]).decode("utf-8")
        # parse the output into a dictionary of package names as keys and their versions as values
        packages = {line.split()[0]: line.split()[1] for line in packages.split("\n")[2:-1]}
        if verbose:
            print(packages)
    except Exception as e:
        print("An error occurred:", str(e))
    return packages

# now let's write a function to compare the versions of the installed packages with the latest versions available on PyPI
def compare_package_versions(packages):
    # compare the installed package versions with the latest versions available on PyPI
    print("="*40, "Package Version Comparison", "="*40)
    try:
        for package, version in packages.items():
            latest_version = subprocess.check_output(["pip", "search", package]).decode("utf-8").split("\n")[0].split("(")[1].split(")")[0]
            # FIXME above pip search does not work anymore
            # RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead. See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
            if version != latest_version:
                print(f"Package: {package} Installed Version: {version} Latest Version: {latest_version}")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    packages = get_packages_info(verbose=True)
    compare_package_versions(packages)