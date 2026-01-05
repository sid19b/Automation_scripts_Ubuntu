import requests
import sys

def health_check():
    url = "http://localhost:8081/health"

    try:
        response = requests.get(url,timeout=(5,10))

        if response.status_code==200:
            print("status:ok")
            sys.exit(0)
        else:
            print("status:not ok")
            sys.exit(1)
    except requests.exceptions.ConnectTimeout:
        print("ERROR: Connection timed out.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"ERROR: A network error occurred: {e}")
        sys.exit(1)


if __name__=="__main__":
    health_check()
