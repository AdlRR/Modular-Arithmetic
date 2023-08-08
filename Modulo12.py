import math

class Modulo12(object):
  """A class to work with integers modulo 12."""

  def __init__(self, n = 0):
    """Initializer. Without arguments it instantiates a 0."""
    self._representative = n % 12

  @property
  def representative(self):
    """Get representative or remainder attribute."""
    return self._representative

  def __repr__(self):
    """Printable String representation, called by function `repr()`, as well as `str()` and `print()`."""
    return str(self._representative) + ' mod 12'

  def __eq__(self, other):
    """Overridden equality operation (==) between instances."""
    return self._representative == other._representative

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
    """Overridden product operation (*) between instances, or between an instance and an integer."""
    if isinstance(other, self.__class__):
      product_of_representatives = self._representative * other._representative
      if isinstance(product_of_representatives, int):
        return self.__class__(product_of_representatives)
      else:
        return self.__class__(math.nan)
    elif isinstance(other, int):
      return self.__class__(self._representative * other)
    else:
      return self.__class__(math.nan)

  def __rmul__(self, other):
    """Overridden reflected product operation (*) between an integer and an instance."""
    return self.__mul__(other)

  def is_invertible(self):
    if isinstance(self._representative, int):
      if (self._representative % 2 == 0) or (self._representative % 3 == 0):
        return False
      else:
        return True
    else:
      return False

  def inverse(self):
    if self.is_invertible():
      # As a consequence of Euler's Theorem, the inverse is the class to the power of phi(12)-1, where phi is the Euler totient function. In this case, phi(12)=4.
      return self.__class__(self._representative ** 3)
    else:
      return self.__class__(math.nan)	
	
  def __truediv__(self, other):
    """Overridden true division operation (/)."""
    return self.__mul__(other.inverse())

  def __rtruediv__(self, other):
    """Overridden reflected true division operation (/)."""
    return self.inverse().__mul__(other)
  
  def divides(self, other):
    if other._representative % math.gcd(self._representative, 12) == 0:
      return True
    else:
      return False

  def is_divided_by(self, other):
    return other.divides(self)

  def multivalued_division_by(self, other):
    """Returns a list with all solutions to the equation other * x = self with unknown x"""
    result_list = []
    # Since there are few elements, we will simply find all divisors by brute force or exhaustive search:
    for i in range(12):
      if other * i == self:
        result_list.append(self.__class__(i))
    return result_list

  def multivalued_division_of(self, other):
    """Returns a list with all solutions to the equation self * x = other with unknown x"""
    return other.multivalued_division_by(self)

  def __pow__(self, other):
    """Overridden power operation (**) between a Modulo12 instance and an integer."""
    def power_modulo_12(base, exponent):
      result = 1
      for i in range(exponent):
        result = result * base % 12
      return result

    n = 0
    
    if isinstance(other, int):
      n = other
    elif isinstance(other, float):
      if other.is_integer():
        n = int(other)
      else:
        return self.__class__(math.nan)
    else:
      raise NotImplementedError()

    if n >= 0:
      return self.__class__(power_modulo_12(self._representative, n))
    else:
      return self.__class__(power_modulo_12(self.inverse()._representative, -n))

  def __abs__(self):
    """Overridden absolute value function (abs)."""
    six = 6
    if self._representative <= six:
      return self
    if self._representative > six:
      return self.__class__(-self._representative)
