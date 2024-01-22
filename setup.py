import os

if __name__ == "__main__":
  print("Installing dependencies...")
  os.system("pip install -r requirements.txt")
  
  print("Deleting myself...")
  os.remove(__file__)
