import fastapi
import string
import random
import os
import json

 

def generate_password(x):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Ensure at least one of each required type
    each_type = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    if x < 3:
        raise ValueError("Password length must be at least 3")

    each_type += random.choices(letters + numbers + symbols, k=x - 3)
    random.shuffle(each_type)

    password = ''.join(each_type)
    print(f"Your generated password is: {password}")
    return password



def generate_pin(x):
    numbers = string.digits
    pin = ''.join(random.choice(numbers) for _ in range(x))
    print(f"Your generated pin is:{pin}")
    return pin



def load_file():
    if os.path.exists("password_logs.json"):
        with open("password_logs.json", "r") as file:
            return json.load(file)
    else:
        return {}




def save_file(data):
    with open("password_logs.json", "w") as file:
        json.dump(data, file, indent=4)




        

        


    




app = fastapi.FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to the crypto wallet password generator!",
        "routes": ["/generate?wallet_name=xyz&length=12", "/save_password" "/view", "/delete/{wallet_name}", "/exit"]
    }


@app.post("/generate")
def generate(length, kind = ""):
    if kind == "password":
        data =  generate_password(length)
        message = ("✅ Your password has been generated!\n"
            f"🔑 Password: {data} \n"
            "💾 Do you want to save it?\n"
            "Click 'save' button to save it or keep generating for more.")
        return message
    elif kind == "pin":
        data =  generate_pin(length)
        message = ("✅ Your pin has been generated!\n"
            f"🔑 Pin: {data} n"
            "💾 Do you want to save it?\n"
            "Click 'save' button to save it or keep generating for more.")
        return message
    else:
        return {"error": "Invalid type. Please choose 'password' or 'pin' with a valid length."}
    
   
  


  
@app.post("/save_password")
def save_password(wallet_name: str, password: str):
    data = load_file()
    data[wallet_name] = password
    save_file(data)
    print(f"Password for {wallet_name} saved successfully!")


@app.get("/view")
def view_password(): 
    data = load_file()
    for wallet, password in data.items():
        print(f"{wallet}: {password}")



@app.delete("/delete/{wallet_name}")
def delete_password(wallet_name):
    data = load_file()
    if wallet_name in data:
        del data[wallet_name]
        save_file(data)
        print(f"Deleted password for {wallet_name}")
    else:
        print(f"No {wallet_name} found")

    
