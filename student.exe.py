import ctypes
import ctypes.wintypes
import psutil
import subprocess

# Constants
TH32CS_SNAPPROCESS = 0x00000002
TH32CS_SNAPTHREAD = 0x00000004
PROCESS_TERMINATE = 0x0001
THREAD_ALL_ACCESS = 0x001F03FF

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize', ctypes.wintypes.DWORD),
        ('cntUsage', ctypes.wintypes.DWORD),
        ('th32ProcessID', ctypes.wintypes.DWORD),
        ('th32DefaultHeapID', ctypes.wintypes.ULONG),
        ('th32ModuleID', ctypes.wintypes.DWORD),
        ('cntThreads', ctypes.wintypes.DWORD),
        ('th32ParentProcessID', ctypes.wintypes.DWORD),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('szExeFile', ctypes.wintypes.WCHAR * 260)
    ]

def print_error_open_proc():
    print(f"Error: {ctypes.GetLastError()}. Press Enter to continue.")
    input()

def get_proc_id(proc_name):
    print(f"Searching for process: {proc_name}")
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'].lower() == proc_name.lower():  # Case insensitive comparison
            print(f"Process found: {proc.info['name']} (PID: {proc.info['pid']})")
            return proc.info['pid']
    print(f"No process found with name: {proc_name}")
    return None
def start_process(target_proc):
    print(f"Starting process: {target_proc}")
    subprocess.Popen(target_proc, shell=True)
    print("Process created")

def suspend_proc_thread(pid):
    if pid is None:
        print("SUSPEND: INVALID PROCESS ID")
        return

    h_thread_snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0)
    if h_thread_snapshot == -1:
        print(f"CreateToolhelp32Snapshot failed with error: {ctypes.GetLastError()}")
        return

    thread_entry = ctypes.create_string_buffer(32)  # Placeholder for thread information
    ctypes.memset(thread_entry, 0, 32)

    if ctypes.windll.kernel32.Thread32First(h_thread_snapshot, ctypes.byref(thread_entry)):
        while True:
            thread_owner_pid = ctypes.cast(thread_entry[8:12], ctypes.POINTER(ctypes.wintypes.DWORD)).contents.value
            if thread_owner_pid == pid:
                thread_id = ctypes.cast(thread_entry[12:16], ctypes.POINTER(ctypes.wintypes.DWORD)).contents.value
                h_thread = ctypes.windll.kernel32.OpenThread(THREAD_ALL_ACCESS, False, thread_id)
                if h_thread:
                    ctypes.windll.kernel32.SuspendThread(h_thread)
                    ctypes.windll.kernel32.CloseHandle(h_thread)
            if not ctypes.windll.kernel32.Thread32Next(h_thread_snapshot, ctypes.byref(thread_entry)):
                break
    print(f"Suspend Process with pid: {pid}")
    ctypes.windll.kernel32.CloseHandle(h_thread_snapshot)

def resume_proc_thread(pid):
    h_thread_snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0)
    if h_thread_snapshot == -1:
        print(f"CreateToolhelp32Snapshot failed with error: {ctypes.GetLastError()}")
        return

    thread_entry = ctypes.create_string_buffer(32)  # Placeholder for thread information

    if ctypes.windll.kernel32.Thread32First(h_thread_snapshot, ctypes.byref(thread_entry)):
        while True:
            thread_owner_pid = ctypes.cast(thread_entry[8:12], ctypes.POINTER(ctypes.wintypes.DWORD)).contents.value
            if thread_owner_pid == pid:
                thread_id = ctypes.cast(thread_entry[12:16], ctypes.POINTER(ctypes.wintypes.DWORD)).contents.value
                h_thread = ctypes.windll.kernel32.OpenThread(THREAD_ALL_ACCESS, False, thread_id)
                if h_thread:
                    ctypes.windll.kernel32.ResumeThread(h_thread)
                    ctypes.windll.kernel32.CloseHandle(h_thread)
            if not ctypes.windll.kernel32.Thread32Next(h_thread_snapshot, ctypes.byref(thread_entry)):
                break
    print(f"Resumed Process with pid: {pid}")
    ctypes.windll.kernel32.CloseHandle(h_thread_snapshot)

def kill_process(pid):
    proc = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
    if proc:
        if ctypes.windll.kernel32.TerminateProcess(proc, 0):
            print(f"Successfully terminated Process with pid {pid}")
            ctypes.windll.kernel32.CloseHandle(proc)
            return 0
        else:
            print(f"Failed to terminate process with pid {pid}, ErrorNo: {ctypes.GetLastError()}")
            ctypes.windll.kernel32.CloseHandle(proc)
            return ctypes.GetLastError()
    else:
        print(f"Failed to open process with pid {pid}, ErrorNo: {ctypes.GetLastError()}")
        return ctypes.GetLastError()

# Example usage
if __name__ == "__main__":
    proc_name = "procexp64.exe"
    pid = get_proc_id(proc_name)
    if pid:
        suspend_proc_thread(pid)
        resume_proc_thread(pid)
        kill_process(pid)