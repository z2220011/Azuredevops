import os

def main():
    # Azure DevOpsの変数から名前を取得
    name = os.getenv("USER_NAME")
    
    if name:
        print(f"私は {name} です。")
    else:
        print("名前が指定されていません。")

if __name__ == "__main__":
    main()
