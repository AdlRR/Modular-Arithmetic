class Modulo12(object):
  """A class to work with integers modulo 12."""

  def __init__(self, n=0):
    """Initializer. Without arguments it instatiates a 0."""
    self._remainder = n % 12

  def getRemainder(self):
    """Get remainder attribute."""
    return self._remainder

  def __str__(self):
    """Printable String representation."""
    return str(self._remainder) + ' mod 12'

  def __add__(self, other):
    """Overridden sum operation (+) between instances."""
    if isinstance(other, self.__class__):
      return self.__class__(self._remainder + other._remainder)
    else:
      return self.__class__(self._remainder + other)

  def __radd__(self, other):
    """Overridden reflected sum operation (+) between instances."""
    return self.__add__(other)

  def __mul__(self, other):
    """Overridden product operation (*) between instances."""
    if isinstance(other, self.__class__):
      return self.__class__(self._remainder * other._remainder)
    else:
      return self.__class__(self._remainder * other)
