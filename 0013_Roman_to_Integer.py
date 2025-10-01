def roman_to_int(s: str) -> int:
      mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
      latin = 0           
      stack = list(s)      
      
      while len(stack) > 1:
          roman = stack.pop(0)
          translation = mapping[roman]
          if translation >= mapping[stack[0]]:
              latin += translation
          else:
              latin -= translation
      
      return latin + mapping[stack[0]]