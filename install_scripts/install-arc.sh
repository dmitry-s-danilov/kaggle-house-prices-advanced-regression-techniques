#!/bin/bash

# Script have to be run from project home directory.

package_path="dist"
package_file="*.tar.gz"

python -m build
pip install $( find $package_path -name $package_file )
