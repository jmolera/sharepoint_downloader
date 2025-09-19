#!/usr/bin/env python3
"""
SharePoint Downloader using rclone
Automatically downloads rclone and syncs files from SharePoint
"""

import os
import urllib.request
import zipfile
import shutil
import subprocess
import sys

def download_rclone():
    """Download rclone if it doesn't exist"""
    rclone_url = "https://downloads.rclone.org/rclone-current-windows-amd64.zip"
    rclone_zip = "rclone.zip"
    rclone_exe = os.path.join(os.getcwd(), "rclone.exe")
    
    if not os.path.exists(rclone_exe):
        print("[INFO] Downloading rclone...")
        try:
            urllib.request.urlretrieve(rclone_url, rclone_zip)
            with zipfile.ZipFile(rclone_zip, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith("rclone.exe"):
                        zip_ref.extract(file, ".")
                        shutil.move(file, "rclone.exe")
            os.remove(rclone_zip)
            print("[OK] rclone.exe downloaded and ready.")
        except Exception as e:
            print(f"[ERROR] Failed to download rclone: {e}")
            sys.exit(1)
    else:
        print("[OK] rclone.exe already exists.")

def configure_rclone():
    """Open rclone interactive configuration"""
    print("[INFO] Opening rclone configuration in separate terminal.")
    print("Configure OneDrive (SharePoint) connection.")
    print("[INFO] Press Enter when configuration is complete...")
    
    try:
        subprocess.run(["cmd", "/c", "start", "cmd", "/k", "rclone.exe config"])
        input("Press Enter when rclone is configured...")
    except Exception as e:
        print(f"[ERROR] Failed to open configuration: {e}")

def sync_files(remote, remote_path, local_path="."):
    """Sync files from SharePoint"""
    cmd = ['rclone', 'copy', f'{remote}:{remote_path}', local_path, '--progress']
    print("Executing:", " ".join(cmd))
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')
        process.wait()
        
        print(f"\nProcess finished with code: {process.returncode}")
        if process.returncode == 0:
            print("[OK] Sync completed successfully.")
        else:
            print(f"[ERROR] Sync failed. Code: {process.returncode}")
    except Exception as e:
        print(f"[ERROR] Failed to execute rclone: {e}")

def main():
    """Main function"""
    print("=== SharePoint Downloader ===")
    
    # Download rclone if needed
    download_rclone()
    
    # Check for existing configuration
    config_exists = os.path.exists(os.path.expanduser("~\\AppData\\Roaming\\rclone\\rclone.conf"))
    if not config_exists:
        print("[INFO] No rclone configuration found.")
        configure_rclone()
    else:
        print("[OK] rclone configuration found.")
    
    # Get sync parameters
    remote = input("Remote name (default: m30): ").strip() or "m30"
    remote_path = input("Remote path (default: sites/ATMC30/Documentos compartidos/LOTE 1): ").strip() or "sites/ATMC30/Documentos compartidos/LOTE 1"
    local_path = input("Local destination (default: current dir): ").strip() or "."
    
    # Execute sync
    sync_files(remote, remote_path, local_path)

if __name__ == "__main__":
    main()
