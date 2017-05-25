import apps

def restart():
    reload(apps)
    apps.start()

if __name__ == "__main__":
    apps.start()
