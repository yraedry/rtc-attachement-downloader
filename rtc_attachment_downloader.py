import sys
from mediator_process import start_attachment_download, start_download_rethrow_file
from utils.Directory_utils import read_rethrow_file, rotate_logs


def start_process():
    print("************Welcome to RTC Attachment Downloader**************")
    menu()


def menu():
    choice = input("""
A: Start download of attachments
B: Start download of failed attachments
C: View failed attachments
Q: Exit

Please enter your choice: """)

    if choice == "A" or choice == "a":
        start_attachment_download()
        rotate_logs()
    elif choice == "B" or choice == "b":
        start_download_rethrow_file()
        rotate_logs()
    elif choice == "C" or choice == "c":
        rethrow_files = read_rethrow_file()
        if rethrow_files is not None:
            for files in rethrow_files:
                print("workitemID => " + files)
        else:
            print()
            print("No workitems to relaunch")
            menu()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("Options are A, B, C or Q")
        print("Please try again")
        menu()


start_process()
