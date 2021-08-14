'''
Project:Onmyoji auto bot
Version:1.0.0

Powered By KoyominZ
'''

from Processing import *
import pyautogui

accounts=[]

def main():
    alert="Warning: Please be sure to run with Administrator!\n\n"
    accountCount=int(pyautogui.prompt(text=alert+'Enter number of account: ', title='Onmyoji bot' , default='1'))
    while accountCount:
        accountCount-=1
        name_acc='Account '+str(accountCount)+'\n\n'
        gameMode="Game Type:\n1. Multi-player Soul/Evolution\
             \n2. Exploration \
                \n3. Single Exploration \
                  \n4. Realm Raid \
                  \n5. Demon Seal \
                  \n6. Event\n "
        gameMode=int(pyautogui.prompt(text=alert+name_acc+gameMode, title='Onmyoji bot' , default='2'))
        isCaptain=True
        isMainDMG=True
        windowName=int(pyautogui.prompt(text=alert+name_acc+'Enter name of window game: \n1. Onmyoji \n2. [#] Onmyoji [#] ', title='Onmyoji bot' , default='1'))
        if windowName==1:
            windowName='Onmyoji'
        else:
            windowName='[#] Onmyoji [#]'
        count=int(pyautogui.prompt(text=alert+name_acc+'Enter number of round: ', title='Onmyoji bot' , default='9999'))
        if gameMode == 2 or gameMode == 1:
            isCaptainChar=pyautogui.prompt(text=alert+name_acc+'Whether it is a leader(Y/N): ', title='Onmyoji bot' , default='Y')
            isMainDMGChar=pyautogui.prompt(text=alert+name_acc+'Whether it is a main dmg dealer(Y/N): ', title='Onmyoji bot' , default='Y')
            if isCaptainChar=='y' or isCaptainChar=="Y":
                isCaptain=True
            else:
                isCaptain=False
            if isMainDMGChar=='y' or isMainDMGChar=="Y":
                isMainDMG=True
            else:
                isMainDMG=False
        
        accounts.append(Processing(windowName,gameMode,count,isCaptain,isMainDMG))
    
    if len(accounts) == 2:
        accounts.append(Processing('[#] Onmyoji [#]',2,9999,False,True))
        account1=threading.Thread(accounts[0].run())
        account2=threading.Thread(accounts[1].run())
    else:
        account1=threading.Thread(accounts[0].run())
    


main()