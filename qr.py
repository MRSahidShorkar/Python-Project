from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class  Qr_Generator:
        def __init__(self,root):
            self.root=root
            self.root.geometry("900x600+200+50")
            self.root.title("Qr code maker !!!")
            self.root.resizable(False,False)

            self.bg = PhotoImage(file = "J:/Python Project/2022 last/Qr code/bg/2.png")
  
            # Show image using label
            label1 = Label( self.root, image = self.bg)
            label1.place(x = -1.5, y = 30)

            

            title=Label(self.root,text="QR Code Genarator",font=('times new roman',18,'bold'),bg='#D9D9D9',fg='black',anchor='c').place(x=0,y=0,relwidth=1)

            #========= variables ===========#
            self.var_valid_id=StringVar()
            self.var_team_name=StringVar()
            self.var_position=StringVar()
            self.var_verify=StringVar()
            
            #========= information details===========#

            info_frame= Frame(self.root,bd=2,bg="#D9D9D9",relief=RIDGE)
            info_frame.place(x=50,y=100,width=500,height=380)

            

            info_details=Label(info_frame,text='       QR information details',font=('times new roman',18,'bold'),bg='#053247',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
            
            
            valid_id=Label(info_frame,text="Valid ID :",font=('times new roman',14,'normal'),bg= '#D9D9D9',fg='black').place(x=5,y=50)
            valid_id=Entry(info_frame,textvariable=self.var_valid_id,font=("arial",10),bg='#FCE9A6').place(x=130,y=50,height=30)

            team_name=Label(info_frame,text="Team Name :",font=('time new  roman',14,'normal'),bg="#D9D9D9",fg='black').place(x=5,y=100)
            team_name=Entry(info_frame,textvariable=self.var_team_name,font=("arial",10),bd=1,bg='#FCE9A6').place(x=130,y=100,height=30)
           
            position=Label(info_frame,text="Position :",font=('time new  roman',14,'normal'),bg='#D9D9D9',fg='black').place(x=5,y=150)
            position=Entry(info_frame,textvariable=self.var_position,font=("arial",10),bd=1,bg='#FCE9A6').place(x=130,y=150,height=30)


            verify=Label(info_frame,text="Verify Link :",font=('time new  roman',14,'normal'),bg='#D9D9D9',fg='black').place(x=5,y=200)
            verify=Entry(info_frame,textvariable=self.var_verify,font=("arial",10),bd=1,bg='#FCE9A6').place(x=130,y=200,height=30)


            #================Button sction======================
            qr_genarator=Button(info_frame,text="QR code Genarate",command=self.generate,font=('time new  roman',14,'normal'),bg='#ACF6EB',fg='black').place(x=50,y=270)
            clear=Button(info_frame,text="Clear",command=self.clear,font=('time new  roman',14,'normal'),bg='#ACF6EB',fg='black').place(x=280,y=270)
            #save=Button(info_frame,text="Save",font=('time new  roman',14,'normal'),bg='#ACF6EB',fg='black').place(x=400,y=270)


            self.msg=''
            self.lbl_msg=Label(info_frame,text=self.msg,font=("time new romans",14),bd=2,bg='#D9D9D9',fg='green')
            self.lbl_msg.place(x=0,y=340,relwidth=1)



            
            #========= QR code image section ===========#
            
            QRcode_frame= Frame(root,bd=2,relief=RIDGE)
            QRcode_frame.place(x=570,y=100,width=305,height=385)

            self.bag = PhotoImage(file = "J:/Python Project/2022 last/Qr code/bg/1.png")
  
            # Show image using label
            label1 = Label( QRcode_frame, image = self.bag)
            label1.place(x = 0, y = 0)

            #qr_section=Label(QRcode_frame,text='       QR code image section',font=('times new roman',18,'bold'),bg='#053247',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
            
            #file_location=Button(QRcode_frame,text="File Location",font=('time new  roman',14,'normal'),bg='#ACF6EB',fg='black').place(x=80,y=300)

            self.qr_code=Label(QRcode_frame,text="No \n Available",font=("time new romans",14),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
            self.qr_code.place(x=55,y=80,width=180,height=180)
        #=========================funcition here======================
        def clear(self):

            self.var_valid_id.set(' ')
            self.var_team_name.set(' ')
            self.var_position.set(' ')
            self.var_verify.set(' ')


            self.msg=''
            self.lbl_msg.config(text=self.msg)

        def generate(self):
            if self.var_valid_id.get()=='' or self.var_team_name.get()=='' or self.var_position.get()=='' or self.var_verify.get()=='':
                self.msg='All Fields are Required !!!'
                self.lbl_msg.config(text=self.msg,fg='red')
            else:

                qr_data=(f"Valid ID : {self.var_valid_id.get()}\nTeam Name : {self.var_team_name.get()}\nPosition : {self.var_position.get()},\nVerify: {self.var_verify.get()}")
                qr_code=qrcode.make(qr_data)
                #print(qr_code)
                qr_code=resizeimage.resize_cover(qr_code,[180,180])
                qr_code.save("QR/const_"+str(self.var_valid_id.get())+'.png')
                #==================QR code image update==============
                self.im=ImageTk.PhotoImage(qr_code)
                self.qr_code.config(image=self.im)
                #===============update notification=============
                self.msg='QR code generated Successfully !!!'
                self.lbl_msg.config(text=self.msg,fg='green')


root=Tk()
object=Qr_Generator(root)
root.mainloop()
