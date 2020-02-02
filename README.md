# py_metaprogramming

Inspired by David Beazley'S tutorial [Python 3 Metaprogramming](http://dabeaz.com/py3meta/
) presented at PyCon'13, March 14, 2013. Santa Clara, California. 

## Considerations
(Class) Decorator vs Metaclass:
How much functionality will the Metaclass have?
Relocate special needs from metaclass to decorator


## Use Case

### Debug

#### Problem
While debugging, `print` or `logging` function everywhere.

#### Solution
Use decorator to debug func and class decorator to debug all instance method.

### Signature

#### Problem
Boilerplate code to assign attribute while init a class.

#### Solution
Use `Signature` from the standard library `inspect` to build signature for function. 
