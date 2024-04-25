class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass
def roman_to_int(s):
  roman_map = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  }
  total = 0
  i = 0
  while i < len(s):
    current_value = roman_map[s[i]]
    if i + 1 < len(s) and current_value < roman_map[s[i + 1]]:
      # Subtraction case (special cases)
      total += roman_map[s[i + 1]] - current_value
      i += 2  # Skip two characters (current and next)
    else:
      # Addition case (normal case)
      total += current_value
      i += 1
  return total

# Example usage
roman_numeral = "MCMXCIV"
integer_value = roman_to_int(roman_numeral)
print(f"{roman_numeral} = {integer_value}")