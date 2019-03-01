# Artefact

This Artefact contains the data and scripts to replicate our experiments for the paper

```
Multi-Cost Bounded Trade-off Analysis in MDP
```
by Arnd Hartmanns, Sebastian Junges, Joost-Pieter Katoen, and Tim Quatmann


## Contents

The artefact includes all benchmark models and properties that are mentioned in the paper and include the logfiles obtained by us.
For cost-bounded queries (Tables 1 and 2) these can be found in the subdirectory `cost-bounded/`.
Model files and logs for the quantile queries (Table 3) can be found in the subdirectory `quantiles/`.
We provide scripts to replicate our experiments, i.e., to run the experiments on your machine in the subdirectory `replication/`.


## Installation of Storm

We detail the steps to obtain our implementation. It is integrated into the model checker Storm which can be obtained from Github.
The following set of commands to install Storm has been tested on a fresh installation of Ubuntu 18.04. 
`cd` into the directory in which you want to install Storm and execute
```
sudo apt-get install build-essential git cmake libboost-all-dev libcln-dev libgmp-dev libginac-dev automake doxygen libglpk-dev libhwloc-dev libz3-dev z3 libxerces-c-dev libeigen3-dev

cd ~/
git clone https://github.com/moves-rwth/storm.git
cd storm
git checkout a4e03ff
mkdir build
cd build;
cmake .. -DCMAKE_BUILD_TYPE=Release -DSTORM_DEVELOPER=OFF -DSTORM_LOG_DISABLE_DEBUG=ON -DSTORM_USE_INTELTBB=ON 
make storm-main
```
Installation instructions for other operating systems, including MacOS can be found on:
http://www.stormchecker.org/documentation/installation/installation.html#building-storm-from-source

Make sure to build a sufficiently recent version (e.g., git tag `a4e03ff`) to support all query types, in particular the quantile queries.

You should now be able to run storm:
```
your/path/to/storm/build/bin/storm
```


## Checking a multi-cost bounded property in Storm

The artifact contains all benchmark models and properties as considered in the paper.
The corresponding files are located in the directory ~/storm-root/models/
An exemplary invocation for checking a tradeoff property of the mars rover case study from the paper
looks as follows:

```
your/path/to/storm/build/bin/storm --prism cost-bounded/models/rover/rover.prism --prop 'multi(Pmax=? [F{"value"}>99 done], Pmax=? [F{"time"}<=180,{"energy"}<=100 done])' --sound -tm
```

This computes the tradeoff between (i) the probability for obtaining at least value 100 and (ii) finishing within 180 time units and 100 energy units.
The provided arguments have the following meaning:
* --prism specifies a path to a model description in the PRISM language
* --prop specifies the property under consideration (in PRISM syntax)
* --sound invokes interval iteration (instead of potentially imprecise value iteration)
* -tm prints additional time and memory statistics.

A quantile query can be checked using the following command
```
your/path/to/storm/build/bin/storm --prism quantiles/models/rover/rover.prism --prop 'quantile(min TIME, min ENERGY, Pmax>0.95 [F{"value"}>=50,{"time"}<=TIME,{"energy"}<=ENERGY done])' --sound -tm
```

## Checking other multi-cost bounded properties in Storm

To check other properties, please consider the following. If you just want to reproduce the tables, feel free to skip this section.

A selection of relevant additional options of Storm are:
* --constants specifies unspecified constants occurring in the model description, e.g., --constants X=12,Y=42
* --exact invokes policy iteration over exact arithmethic
* --exportcdf specifies a directory in which the results of the analyzed epochs are exported (the plots from Figure 6 are a visual of this data).
* --engine dd enables the DD engine of Storm (only available for the unfolding approach on single objective queries)
* --help prints all available options of Storm
       
Additional properties for the mars rover can be found in
`cost-bounded/models/rover/properties.props`.
The remaining case studies are similar.

The property can also be read from a file: The following invocation is equivalent to the one mentioned above.

```
your/path/to/storm/build/bin/storm --prism cost-bounded/models/rover/rover.prism --prop cost-bounded/models/rover/properties.props multi1 --constants B1=99,B2=-1,B3=180,B4=100 --sound -tm
```


## Checking other multi-cost bounded properties via their unfolding

Model and property files with prefix 'unfolded_' were used to evaluate the unfolding approach. For example

~/storm-root/bin/storm --prism ~/storm-root/models/rover/unfolded_rover.prism --prop ~/storm-root/models/rover/unfolded_properties.props "multi1" --constants B1=99,B2=-1,B3=180,B4=100 --sound -tm

computes the same tradeoff as before via the unfolding approach.

## Replication of the results from the paper

We provide scripts to replicate the results from Tables 1 to 3.
The file `replication/commands.txt` contains a list of all commands.
The script `replication/run.py` provides a more convenient way to select and execute experiments.
To start the scripts, run
```
cd replication
python run.py
```
The script asks the user to specify
* The path to the main binary of storm
* The benchmarks to execute (each of the displayed benchmark sets corresponds to a column of one of the tables)
* A time limit after which an individual experiment is aborted (since checking the whole benchmark set may take some time, we suggest to choose a small time limit here), and
* A directory to which the outputs of storm should be stored.

It is likely that you will see  errors such as `std::bad_alloc`, which reflect an out-of-memory situation.

