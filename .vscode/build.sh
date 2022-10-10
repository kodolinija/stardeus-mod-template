#!/bin/bash

# Remove unnecessary assemblies
rm -f ./Libraries/*.*

# Remove obj cache
rm -f ./.vscode/obj/*.*

# build dll
dotnet build .vscode