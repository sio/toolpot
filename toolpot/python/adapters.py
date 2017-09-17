"""
Helper classes for creating adapters in Python
"""


class CompositionAdapter(object):
    """
    Base class for creating general purpose adapters using composition

    Child classes have to provide _constructor class method that creates
    the underlying object.
    """
    @classmethod
    def _constructor(cls, *a, **kw):
        """This method has to be provided by child classes"""
        raise NotImplementedError

    def __init__(self, *a, **kw):
        """All parameters are passed to _constructor method"""
        self._object = self._constructor(*a, **kw)

    def __getattr__(self, name):
        """If attribute is not present in outer object, try inner one"""
        return getattr(self._object, name)

    def __setattr__(self, name, value):
        """
        All new attributes are set on outer object except for ones that were
        already present in inner object
        """
        if name != "_object" and hasattr(self._object, name):
            return setattr(self._object, name, value)
        else:
            return super().__setattr__(name, value)
