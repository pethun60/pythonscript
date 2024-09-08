import os
import shutil
import sys

def find_usb_mount_point():
    # The mount points are usually found under /media/<username>/
    print("find_usb_mount_point")
    # media_dir = "/media/" + os.getlogin() + "/"
    media_dir = "/media/peter/"
    print("mediadir="+ media_dir)
    if not os.path.exists(media_dir):
        raise Exception(f"Media directory {media_dir} does not exist.")
    
    # List all directories (mount points) in the media directory
    mount_points = [os.path.join(media_dir, d) for d in os.listdir(media_dir)]
    
    if not mount_points:
        raise Exception("No USB device found.")
    
    # Return the first mount point (assuming only one USB is connected)
    return mount_points[0]

def save_to_usb(file_path):
    print("savetousb")
    usb_mount_point = find_usb_mount_point()
    print(usb_mount_point)
    destination = os.path.join(usb_mount_point, os.path.basename(file_path))
    
    # Copy the file to the USB mount point
    shutil.copy(file_path, destination)
    print(f"File saved to {destination}")
    
def save_from_usb(file_path):
    print("savefromusb")
    usb_mount_point = find_usb_mount_point()
    print(usb_mount_point)
    source = os.path.join(usb_mount_point, os.path.basename(file_path))
    
    # Copy the file to the USB mount point
    shutil.copy(file_path, source)
    print(f"File copied from usb {source}")

if __name__ == "__main__":
    # Path to the file you want to save
    #file_path = "textfile.txt"
    file_path = sys.argv[1]
    # Ensure the file exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("This is a sample text file.")
    
    # Save the file from the USB memory
    try:
        print("start program")
        save_from_usb(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")