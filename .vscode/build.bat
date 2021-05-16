echo off

REM remove unnecessary assemblies
DEL .\Libraries\*.*

REM build dll
dotnet build .vscode