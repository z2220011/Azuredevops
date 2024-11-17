# add.py
import os

def main():
    # 環境変数からaとbを取得
    a = int(os.getenv("A", "0"))
    b = int(os.getenv("B", "0"))
    
    # 足し算
    result = a + b
    print(f"The result of {a} + {b} is: {result}")

if __name__ == "__main__":
    main()
