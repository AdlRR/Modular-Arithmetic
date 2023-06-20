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
    return Modulo12(self._remainder + other._remainder)

  def __mul__(self, other):
    """Overridden product operation (*) between instances."""
    return Modulo12(self._remainder * other._remainder)
