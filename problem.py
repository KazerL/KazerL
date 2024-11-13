def greet( name:str)->str:
    """Return a greeting message."""
    print("Hello, " + name )

def add(a,b):
  return a + b

def main():
  greet("James")
  result = add(5, 10)
  print("The result is", result)

main()
