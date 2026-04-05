
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64
def generated_key(password, salt):
 def Encrypt_message(password, message):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    def generate_key(password, salt):
        def encrypt_massege(password, messege):
            salt =get_random_bytes(16)
            key = generate_key(password, salt)
            #.3 initialize the EAX MODE
            cipher = AES.new(key, AES.MODE_EAX)

        # 4. convert text to bytes
        ciphertext, tag = cipher.encrpt_and_digest(message.encode())
        # 5. return as base64
        return{
            "salt": base64.b64encode(salt).decode(),
            "nonce" : base64.b64encode(cipher.nonce).decode(), # Nonce = "Nu"
             "ciphertext": base64.b64encode(ciphertext).decode(),
             "tag": base64.b64encode(tag).decode()
        }
def decrypt_message(password, encrypted_data):

 def decrypt_message(password, encrypted_data):
    #1. convert the Base64 text back into raw computer bytes
    salt = base64.b64decode(encrypted_data)["salt"]
    nonce = base64.b64decode(encrypted_data)["nonce"]
    ciphertext = base64.b64decode(encrypted_data)["ciphertext"]
    tag = base64.b64decode(encrypted_data)["tag"]
    # 2. Re-generate the EXACT same key using the password and the prov
    key = generated_key(password, salt)
    # 3. create the ciypher object using the SAME key and orginal
    cipher = AES.new(key,AES.MODE_EAX, nonce=nonce)
    # 4. Decrypt and verify: this checks if the "tag" matches.
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    # 5. convert bytes back into a readable string
    return decrypt.decode()
# comments

# we store the most recent result
last_encrypted = None

def encrypt():
    """  Triggerwhen the user clicks "Encrypt"""
    global last_encrypted
    #Retrieve data from the GUI input fields
    password = password_entry.get()
    message = messege_entry.get("1.0", tk.END).strip()
    # Basic validation: dont try to encrypt nothing!
    if not password or not meassge:
        messagebox.shwowarning("Input Error", "please enter both password")
        return
    # Run the backend encryption function
    last_encrypted = encrypt_message(password, message)
    # Update UI: Clear old text and show the new encrypted dictionary
    def decrypt():
       try:
            # Attept to decrypt using password currently in the Entry box
            decrypted_msg = decrypt_message(password, last_encrypted)
            # success! show the orginal message
            decrypted_text.delete("1.0", tk.END)
            decrypted_text.insert(tk.END, decrypted_msg)
       except Exception as e:
#this triggers if the password is wrong 

# 3. GUI LAYOUT (Tkinter)

        root = tk.Tk()
        root.title("secure AES-256 Encryptor")
# Row 0: password Input (using show "" to hide characters) 
# Row 0: Password Input (Using show="*" to hide characters)
tk.Label(root, text="Step 1: Enter Password:").grid(row=0, column=0, sticky="w", padx=10)

password_entry = tk.Entry(root, width=50, show="*")
password_entry.grid(row=0, column=1, pady=10, padx=10)

# Row 1: Message Input
tk.Label(root, text="Step 2: Message to Hide:").grid(row=1, column=0, sticky="nw", padx=10)

message_entry = tk.Text(root, height=4, width=50)
message_entry.grid(row=1, column=1, pady=5, padx=10)

# Row 2: Encrypt Action
tk.Button(
    root,
    text="--- ENCRYPT MESSAGE ---",
    command=encrypt,
    bg="#e1e1e1"
).grid(row=2, column=1, sticky="ew")

# Row 3: Output Display (Encrypted)
tk.Label(root, text="Encrypted Metadata:").grid(row=3, column=0, sticky="nw", padx=10)

encrypted_text = tk.Text(root, height=6, width=50, fg="blue")
encrypted_text.grid(row=3, column=1, pady=5, padx=10)

# Row 4: Decrypt Action
tk.Button(
    root,
    text="--- DECRYPT MESSAGE ---",
    command=decrypt,
    bg="#e1e1e1"
).grid(row=4, column=1, sticky="ew")

# Row 5: Result Display (Decrypted)
tk.Label(root, text="Original Message:").grid(row=5, column=0, sticky="nw", padx=10)
decrypt_text = tk. Text(root, height=4,widith=50,fg="green")
decrypt_text. grid(cows=5, column=1, pady=5, padx=10)

# start the application loop
root.mainloop()
