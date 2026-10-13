# Decisions

## 001 - chose uv over conda environment (2026-10-12)
**WHY** Key issue is lockfile, which demands the exact packages for everyone, and there was also a hard coded path to my mac in environment.yml. Conda is a heavy install for a small project, and uv provides one tool for the required environment and packages.
**Rejected** Conda

## 002 - created package layout with src and scripts parent folders (2026-10-12)
**WHY** SRC dir contains code to be imported. Scripts contains files you run to make a map or explore data. The layout separates code that is imported from code that is run.
**Rejected** Unsorted structure.

## 003 - deleted environment.yml and hello.py. (2026-10-12)
**WHY** Environment.yml is linked to conda environment and so is not useful for new package in uv. Hello.py is not a functioning part of the software package.

## 004 - using module-name as 'ben_nevis' in tool.uv.build-backend (2026-10-12)
**WHY** Currently the overall package is called ben_nevis_geospatial while the code to be imported is called ben_nevis. Created a module name in the toml to clarify. Adds some complexity but is preferred as the names are kept distinct.