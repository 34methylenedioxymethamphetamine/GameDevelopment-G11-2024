import subprocess

def list_registry_folders_to_file():
    # PowerShell command to list all registry keys
    command = "Get-ChildItem -Path 'Registry::HKEY_LOCAL_MACHINE' -Recurse | Select-Object -ExpandProperty Name"

    # Execute the command and capture the output
    print("running")
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    print("ran")

    # Check if the command was successful
    if result.returncode == 0:
        # Write the output to a file
        with open("regtree.txt", "w") as file:
            file.write(result.stdout)
        print("Registry folders have been saved to regtree.txt.")
    else:
        print("Error:", result.stderr)

if __name__ == "__main__":
    list_registry_folders_to_file()
