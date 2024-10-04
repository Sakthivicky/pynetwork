import paramiko

def ssh(host,port,username,passwd):
    sshclient=paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    try:
        sshclient.connect(host,port,username=username,password=passwd)
        command='uname -a'
        stdin,stdout,err=sshclient.exec_command(command)
   
        print(f'output:{stdout.read().decode()}')
          
    except Exception as e:
       print("error",e)

    finally:
        sshclient.close()

if __name__=="__main__":
    username="sakthi"
    port=22
    passwd="852692"
    host="127.0.0.1"
    

    ssh(host,port,username,passwd)
