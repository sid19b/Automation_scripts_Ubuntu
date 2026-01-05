import requests
import sys

def ready_check():
    url = "http://localhost:8081/ready"

    try:
        response = requests.get(url,timeout=(5,10))

        if response.status_code==200:
            print("status:ready")
            sys.exit(0)
        else:
            print("status:not ready")
            sys.exit(1)
    except requests.exceptions.ConnectTimeout:
        print("ERROR: Connection timed out.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"ERROR: A network error occurred: {e}")
        sys.exit(1)


if __name__=="__main__":
    ready_check()
