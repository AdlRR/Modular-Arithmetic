class Modulo12(object):
  """A class to work with integers modulo 12."""

  _twelve = 12

  def __init__(self, n = 0):
    """Initializer. Without arguments it instantiates a 0."""
    self._representative = n % self._twelve

  @property
  def representative(self):
    """Get representative or remainder attribute."""
    return self._representative

  def __repr__(self):
    """Printable String representation, called by function `repr()`, as well as `str()` and `print()`."""
    return str(self._representative) + f' mod {self._twelve}'

  def __add__(self, other):
    """Overridden sum operation (+) between instances."""
    if isinstance(other, self.__class__):
      return self.__class__(self._representative + other._representative)
    else:
      return self.__class__(self._representative + other)

  def __radd__(self, other):
    """Overridden reflected sum operation (+) between instances."""
    return self.__add__(other)

  def __sub__(self, other):
    """Overridden difference operation (-) between instances."""
    if isinstance(other, self.__class__):
      return self.__class__(self._representative - other._representative)
    else:
      return self.__class__(self._representative - other)

  def __pos__(self):
    """Overriden plus or positive operation (unary + sign)"""
    return self
    
  def __neg__(self):
    """Overriden minus or negative or opposite operation (unary - sign)"""
    return self.__class__(-self._representative)

  def __rsub__(self, other):
    """Overridden reflected difference operation (-) between instances."""
    return self.__neg__().__add__(other)

  def __mul__(self, other):
    """Overridden product operation (*) between instances."""
    if isinstance(other, self.__class__):
      return self.__class__(self._representative * other._representative)
    else:
      return self.__class__(self._representative * other)

  def __pow__(self, other):
    """Overridden power operation (**) between a Modulo12 instance and an integer."""
    if other < 0:
      raise NotImplementedError("Power not implemented for negative exponents")
    else:
      return self.__class__(self._representative ** other)

  def __abs__(self):
    """Overridden absolute value function (abs)."""
    six = 6
    if self._representative <= six:
      return self
    if self._representative > six:
      return self.__class__(-self._representative)
