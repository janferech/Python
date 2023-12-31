import speedtest

def run_speed_test():
    test = speedtest.Speedtest()
    download = test.download() / 10**6  
    upload = test.upload() / 10**6 

    print(f"Download speed: {download:.2f} Mbps")
    print(f"Upload speed: {upload:.2f} Mbps")

if __name__ == "__main__":
    run_speed_test()
