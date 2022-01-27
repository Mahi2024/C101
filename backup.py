import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileFrom,'rb')
        dbx.files_upload(f.read(),fileTo)
def main():
    access_token= "sl.BA41dhtMRZOIQ8kT3licskPnHpVF0gAf1B_Zvfiw9h-aZN6vBg2bTFVhI-k3H8XtQI-sksnsPMGr6L5Ge7zjwEat4Dfx0n0qYb4gkKOqzOVdRQUmdAtk-pDcXysW8oQZyVhcphc"
    transferData=TransferData(access_token)
    fileFrom= input("Enetr the file to be transvered- ")
    fileTo= input("Enter the file to upload in dropbox- ")
    transferData.uploadFile(fileFrom,fileTo)
    print("File has been moved")
main()