#Automation script that displays the current running processes ..
import psutil

def processdisplay():
    listprocess=[]
    for proc in psutil.process_iter():    #psutil.process_iter is used to iterating in process
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])  #Attrs : in hich we pass the parameters as list tupple string
                                                                #as_dict is used to type cast as dictonary 
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            #print("Error Occured")
            pass

    return listprocess

def main():
    print("Automation script to display the running processes..")
    print("Process Monitor")

    listprocess=processdisplay()
    for elem in listprocess:
        print(elem)


if __name__=="__main__":
    main()

