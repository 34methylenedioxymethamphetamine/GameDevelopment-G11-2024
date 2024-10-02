import psutil

def list_disks_with_psutil():
    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        print(f"  Options: {partition.opts}")
        print()

if __name__ == "__main__":
    list_disks_with_psutil()
