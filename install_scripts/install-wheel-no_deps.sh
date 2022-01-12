#!/bin/bash

# Script have to be run from project home directory.

package_path="dist"
package_file="*.whl"

build_args="--wheel"
install_args="--force-reinstall --no-deps"

python -m build $build_args
pip install $install_args $( find $package_path -name $package_file )
