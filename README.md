**Calysto Prolog** 

Because **Calysto Prolog** uses [MetaKernel](https://github.com/Calysto/metakernel/blob/master/README.rst), it has a fully-supported set of "magics"---meta-commands for additional functionality. See all of the [MetaKernel Magics](https://github.com/Calysto/metakernel/blob/master/metakernel/magics/README.md).

## Installation

You can install Calysto Prolog in two steps:

```
pip3 install --upgrade calysto_prolog
```

OR in the system kernel folder with:

```
sudo pip3 install --upgrade calysto_prolog
```

Then, you need to install the kernelspec:

```
python3 -m calysto_prolog install
```

Add `--user` to the above commands to put in your private environment.

## Use

Use Calysto Prolog in the console, qtconsole, or notebook:

```
jupyter console --kernel calysto_prolog
jupyter qtconsole --kernel calysto_prolog
jupyter notebook --kernel calysto_prolog
```

### Example Facts
```
    child(stephanie).
    child(thad).
    mother_child(trude, sally).
 
    father_child(tom, sally).
    father_child(tom, erica).
    father_child(mike, tom).
 
    sibling(X, Y)      :- parent_child(Z, X), parent_child(Z, Y).
 
    parent_child(X, Y) :- father_child(X, Y).
    parent_child(X, Y) :- mother_child(X, Y).
```

### Example Queries
```
    child(NAME)?
    sibling(sally, erica)?
    father_child(Father, Child)?
```

## Requires

* Jupyter
* Python2 or Python3
* metakernel (installed automatically)

