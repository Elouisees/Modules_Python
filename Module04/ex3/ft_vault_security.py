#!/usr/bin/env python3

def secure_archive(file_name: str, action: str, insert_content: str) -> tuple:
    try:
        if action == "write" or action == "w":
            with open(file_name, "w") as file:
                file.write(insert_content)
                return ((True, "Content succesfully written to file"))
        else:
            with open(file_name, "r") as file:
                content = file.read()
                return ((True, content))
    except FileNotFoundError as e:
        return ((False, f"{e}"))
    except PermissionError as e:
        return ((False, f"{e}"))
    except OSError as e:
        return ((False, f"{e}"))
    except Exception as e:
        return ((False, f"{e}"))


if __name__ == "__main__":
    mess = "[FRAGMENT 004]: testtesttest"

    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("secure_archive", "read", ""), "\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("secure_archive_in.txt", "read", ""), "\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("secure_archive.txt", "read", ""), "\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("secure_archive.txt", "write", mess))
