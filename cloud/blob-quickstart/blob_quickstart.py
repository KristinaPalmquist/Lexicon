import os, uuid, sys, glob
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

load_dotenv()
connection_string = os.getenv("AZURE_CONNECTION_STRING")

def is_valid_container_name(name):
    """Validate Azure container name rules"""
    import re
    
    if len(name) < 3 or len(name) > 63:
        return False
    
    if name.startswith('-') or name.endswith('-'):
        return False
    
    if '--' in name:
        return False
    
    if not re.match(r'^[a-z0-9-]+$', name):
        return False
    
    return True

def get_or_create_container(blob_service_client):
    """Get existing container or create new one"""
    containers = list(blob_service_client.list_containers())
    
    if containers:
        print("\nExisting containers:")
        for i, container in enumerate(containers):
            print(f"{i+1}. {container.name}")
        print(f"{len(containers)+1}. Create new container")
        
        try:
            choice = input(f"\nChoose container (1-{len(containers)+1}): ")
            choice_num = int(choice)
            
            if choice_num <= len(containers):
                container_name = containers[choice_num-1].name
                print(f"Using existing container: {container_name}")
                return container_name
            else:
                # Create new container
                return create_new_container(blob_service_client)
        except:
            print("Invalid choice, creating new container...")
            return create_new_container(blob_service_client)
    else:
        # No containers exist, create first one
        print("No existing containers found.")
        return create_new_container(blob_service_client)

def create_new_container(blob_service_client):
    """Create a new container with user-specified name"""
    print("\n=== CREATE NEW CONTAINER ===")
    
    while True:
        container_name = input("Enter container name (3-63 chars, lowercase, no spaces): ").strip().lower()
        
        if not container_name:
            # Use default if user doesn't provide name
            container_name = "quickstart-" + str(uuid.uuid4())[:8]
            print(f"Using default name: {container_name}")
            break
        
        # Replace spaces with hyphens
        container_name = container_name.replace(' ', '-')
        
        # Validate container name
        if not is_valid_container_name(container_name):
            print("❌ Invalid container name. Rules:")
            print("   - 3-63 characters long")
            print("   - Only lowercase letters, numbers, and hyphens")
            print("   - Cannot start or end with hyphen")
            print("   - Cannot have consecutive hyphens")
            continue
        
        # Check if container already exists
        try:
            if blob_service_client.get_container_client(container_name).exists():
                print(f"❌ Container '{container_name}' already exists. Choose a different name.")
                continue
        except:
            pass
        
        break
    
    try:
        blob_service_client.create_container(container_name)
        print(f"✅ Created container: {container_name}")
        return container_name
    except Exception as e:
        print(f"❌ Failed to create container: {e}")
        # Fallback to default name
        fallback_name = "quickstart-" + str(uuid.uuid4())[:8]
        blob_service_client.create_container(fallback_name)
        print(f"Created fallback container: {fallback_name}")
        return fallback_name


def upload_file(blob_service_client, container_name):
    """Upload files from data folder to Azure"""
    print("\n=== UPLOAD FILE ===")
    
    # List files in data folder
    data_files = glob.glob("./data/*.*")
    
    if not data_files:
        print("No files found in ./data/ folder.")
        print("Use option 3 to create files first.")
        return
    
    print("Files available in ./data/ folder:")
    for i, file in enumerate(data_files):
        file_size = os.path.getsize(file)
        print(f"{i+1}. {os.path.basename(file)} ({file_size} bytes)")
    
    try:
        choice = input(f"\nChoose file to upload (1-{len(data_files)}): ")
        selected_file = data_files[int(choice)-1]
        filename = os.path.basename(selected_file)
        
        # Upload to Azure
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        
        print(f"\nUploading '{filename}' to Azure...")
        with open(selected_file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print("✅ Upload successful!")
        
    except (ValueError, IndexError):
        print("Invalid choice.")
    except Exception as e:
        print(f"Upload failed: {e}")

def download_file(blob_service_client, container_name):
    """Download files from Azure Blob Storage"""
    print("\n=== DOWNLOAD FILE ===")
    
    container_client = blob_service_client.get_container_client(container_name)
    blobs = list(container_client.list_blobs())
    
    if not blobs:
        print("No files found in Azure Blob Storage.")
        print("Use option 1 to upload files first.")
        return
    
    print("Files available in Azure Blob Storage:")
    for i, blob in enumerate(blobs):
        print(f"{i+1}. {blob.name} ({blob.size} bytes)")
    
    try:
        choice = input(f"\nChoose file to download (1-{len(blobs)}): ")
        selected_blob = blobs[int(choice)-1]
        
        # Download file
        os.makedirs("./downloads", exist_ok=True)
        download_path = os.path.join("./downloads", selected_blob.name)
        
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=selected_blob.name)
        
        print(f"\nDownloading '{selected_blob.name}'...")
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        
        print(f"✅ Download successful! File saved to: {download_path}")
        
        # Always show content for text files
        try:
            with open(download_path, 'r') as f:
                content = f.read()
                print(f"\n--- Content of {selected_blob.name} ---")
                print(content)
                print("--- End of file ---")
        except:
            print("Could not display content (binary file)")
                
    except (ValueError, IndexError):
        print("Invalid choice.")
    except Exception as e:
        print(f"Download failed: {e}")

def create_file():
    """Create a new file in data folder"""
    print("\n=== CREATE FILE ===")
    
    # Get filename from user
    filename = input("Enter filename (with extension, e.g., 'myfile.txt'): ")
    if not filename:
        filename = "newfile.txt"
        
    print(f"\nEnter content for '{filename}' (press Enter twice to finish):")
    lines = []
    empty_line_count = 0
    
    while True:
        line = input()
        if line == "":
            empty_line_count += 1
            if empty_line_count >= 2:
                break
        else:
            empty_line_count = 0
        lines.append(line)
    
    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()
        
    content = '\n'.join(lines)
    
    # Create file in data folder
    os.makedirs("./data", exist_ok=True)
    file_path = os.path.join("./data", filename)
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        
        print(f"✅ File '{filename}' created successfully in ./data/ folder!")
        print(f"File path: {file_path}")
        
    except Exception as e:
        print(f"Failed to create file: {e}")


def main():
    try:
        print("🗄️  Azure Blob Storage Manager")
        print("=" * 35)
        
        # Initialize Azure connection once, but container selection happens each time
        blob_service_client = None
        
        while True:
            # Show menu
            print("\nWhat would you like to do?")
            print("1. 📤 Upload a file (from ./data/ folder to Azure)")
            print("2. 📥 Download a file (from Azure to ./downloads/ folder)")
            print("3. 📝 Create a new file (in ./data/ folder)")
            print("4. 🚪 Exit")
            
            choice = input("\nChoose option (1, 2, 3, or 4): ")
            
            if choice == "4":
                print("👋 Goodbye!")
                break
            elif choice not in ["1", "2", "3"]:
                print("❌ Invalid choice. Please choose 1, 2, 3, or 4.")
                continue
            
            if choice == "3":
                # Create file doesn't need Azure connection
                create_file()
            else:
                # Upload and Download need Azure connection
                if blob_service_client is None:
                    print("\nConnecting to Azure...")
                    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
                
                # Ask for container selection each time
                container_name = get_or_create_container(blob_service_client)
                
                if choice == "1":
                    upload_file(blob_service_client, container_name)
                elif choice == "2":
                    download_file(blob_service_client, container_name)
            
            # Optional: Ask if user wants to continue
            print("\n" + "="*35)

    except KeyboardInterrupt:
        print("\n👋 Program interrupted. Goodbye!")
    except Exception as ex:
        print(f'❌ Exception occurred: {ex}')

if __name__ == "__main__":
    main()
    