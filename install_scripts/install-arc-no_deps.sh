#!/bin/bash

# Script have to be run from project home directory.

package_path="dist"
package_file="*.tar.gz"

install_args="--no-deps"

python -m build
pip install $install_args  $( find $package_path -name $package_file )
