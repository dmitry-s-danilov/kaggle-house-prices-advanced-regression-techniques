#!/bin/bash

# Script have to be run from project home directory.

package_path="dist"
package_file="*.tar.gz"
package_extras="exploration"

python -m build
pip install $( find $package_path -name $package_file )[$package_extras]
