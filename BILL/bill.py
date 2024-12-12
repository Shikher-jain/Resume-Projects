from tkinter import*
import math,random,os
from tkinter import messagebox 
class bill_app: 

    def __init__(self,root):
        def rgb_to_hex(r, g, b):
            return f"#{r:02x}{g:02x}{b:02x}"

        self.root=root
        self.root.geometry("1350x700+0+0") 
        self.root.title("Billing software")
        bg_color= rgb_to_hex(173, 216, 230) 
        # bg_color="blue"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #===========variables=======

        #=============cosmetic==========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        #=============grocery==========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #===============cold drinks======

        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #============total product price and tex variable============

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()


        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()


        #==============customer======

        self.c_name=StringVar()
        self.c_phon=StringVar()


        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.search_bill=StringVar()
        self.bill_no.set(str(x))





        #========Customer details
        F1= LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("#========Customer details",18,"bold")).grid(row=0,column=0,padx=20,pady=5)

        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        cphn_lbl = Label(F1, text="PhoneNo.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)



        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)


        bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #=======cosmetic frame==========

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetic ",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=330)


        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,pady=5, padx=5)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,pady=5, padx=5)

        hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        hair_s_txt = Entry(F2, width=10,textvariable=self.spray,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,pady=5, padx=5)

        hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,pady=5, padx=5)

        body_lbl = Label(F2, text="Body Lotion ", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        body_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=5, padx=5)

        # =======grocery frame==========

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery ", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=330)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,pady=5, padx=5)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,pady=5,padx=5)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,pady=5,padx=5)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,pady=5,padx=5)

        g5_lbl = Label(F3, text="sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.sugar,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,pady=5, padx=5)

        g6_lbl = Label(F3, text="Tea ", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=5, padx=5)

        # =======cold drink frame==========

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drink ", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=330)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,pady=5, padx=5)

        c2_lbl = Label(F4, text="cocka", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=5)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,pady=5, padx=5)

        c4_lbl = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,pady=5, padx=5)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,pady=5, padx=5)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,pady=5, padx=5)


        #=================== bill area============

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=270,height=330)

        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)

        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===========button frame=======

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu ", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=510, relwidth=1, height=130)

        m1=Label(F6,text="Total cosmetic Price",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2 = Label(F6, text="Total Grocery Price", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=20,pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Cold Drink Price", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=20,pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)


        #============tax labels==========


        c1 = Label(F6, text="cosmetic tax", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=20,pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text=" Grocery tax", font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=20,pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text=" Cold Drink tax", font=("times new roman", 12, "bold")).grid(row=2, column=2,padx=20, pady=1,sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=700,width=530,height=100)


        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=11,font="arial 15 bold",bd=5).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_f, text="Generate Bill",command=self.bill_area,bg="cadetblue", fg="white", pady=15, width=11, font="arial 15 bold",bd=5).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f,command=self.clear_data, text="Clear", bg="cadetblue", fg="white", pady=15, width=6, font="arial 15 bold",bd=5).grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_f,command=self.Exit_app , text="Exit", bg="cadetblue", fg="white", pady=15, width=6, font="arial 15 bold",bd=5).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
            self.c_s_p=(self.soap.get()*40)
            self.c_fc_p=(self.face_cream.get() * 120)
            self.c_fw_p=(self.face_wash.get() * 60)
            self.c_hs_p= (self.spray.get() * 180)
            self.c_hg_p=(self.gell.get() * 140)
            self.c_bl_p=  (self.lotion.get() * 180)

            self.total_cosmetic_price=float(
                                            self.c_s_p+
                                            self.c_fc_p +
                                            self.c_fw_p +
                                            self.c_hs_p +
                                            self.c_hg_p +
                                            self.c_bl_p
            )

            self.cosmetic_price.set("Rs  "+str(self.total_cosmetic_price))
            self.c_tax=round((self.total_cosmetic_price*0.05),2)
            self.cosmetic_tax.set("Rs "+str(self.c_tax))



            self.g_r_p=(self.rice.get() * 80)
            self.g_f_p=(self.food_oil.get() * 180)
            self.g_d_p= (self.daal.get() * 60)
            self.g_w_p=(self.wheat.get() * 240)
            self.g_s_p= (self.wheat.get() * 240)
            self.g_t_p=(self.tea.get() * 150)


            self.total_grocery_price = float(
                                                self.g_r_p +
                                                self.g_f_p +
                                                self.g_d_p +
                                                self.g_w_p +
                                                self.g_s_p +
                                                self.g_t_p

                                                )
            self.grocery_price.set("Rs  "+str(self.total_grocery_price))
            self.g_tax=round((self.total_grocery_price* 0.1),2)
            self.grocery_tax.set("Rs " + str(self.g_tax))


            self.d_m_p=(self.maza.get() * 60)
            self.d_c_p=(self.cock.get() * 60)
            self.d_f_p= (self.frooti.get() * 50)
            self.d_t_p=(self.thumbsup.get() * 45)
            self.d_l_p= (self.limca.get() * 40)
            self.d_s_p= (self.sprite.get() * 60)


            self.total_drinks_price = float(
                                            self.d_m_p +
                                            self.d_c_p +
                                            self.d_f_p +
                                            self.d_t_p +
                                            self.d_l_p +
                                            self.d_s_p
                                            )


            self.cold_drink_price.set("Rs  "+str(self.total_drinks_price))
            self.d_tax=round((self.total_drinks_price * 0.05),2)
            self.cold_drink_tax.set("Rs " + str(self.d_tax))


            self.Total_bill=float(
                                    self.total_cosmetic_price+
                                    self.total_grocery_price+
                                    self.total_drinks_price+
                                    self.c_tax+
                                    self.g_tax+
                                    self.d_tax
            )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome To Retail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, "\n===========================")
        self.txtarea.insert(END, "\nProducts \t\tQTY\tRs")
        self.txtarea.insert(END, "\n===========================")

    def bill_area(self):

        if self.c_name.get()=="" or self.c_phon.get()=="" :
            messagebox.showerror("Error","Customer details are must!")
        elif self.cosmetic_price.get()=="Rs  0.0" and self.grocery_price.get()=="Rs  0.0" and self.cold_drink_price.get()=="Rs  0.0" :
            messagebox.showerror("Error", "Product is not Purchased!")

        else:
            self.welcome_bill()
            #========cosmetic=========
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath soap\t\t{self.soap.get()}\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")

            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t{self.c_hs_p}")

            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t{self.c_hg_p}")

            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n lotion\t\t{self.lotion.get()}\t{self.c_bl_p}")




            #============================grocery===========

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_f_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n wheat\t\t{self.wheat.get()}\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t{self.g_t_p}")


            #=================drinks===========

            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t{self.d_m_p}")

            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Cock\t\t{self.cock.get()}\t{self.d_c_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t{self.d_f_p}")

            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbsup\t\t{self.thumbsup.get()}\t{self.d_t_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t{self.d_l_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t{self.d_s_p}")

            #========= tax =========

            self.txtarea.insert(END, f"\n--------------------------")
            if self.cosmetic_tax.get()!="Rs 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax: \t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "Rs 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax: \t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get() != "Rs 0.0":
                self.txtarea.insert(END, f"\nCold Drink Tax: \t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n:Total Bill: \t\t Rs {self.Total_bill}")
            self.txtarea.insert(END, f"\n----------------------------")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No.:{self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        # =====================================
        for i in os.listdir("bills"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")


    def clear_data(self):

        op = messagebox.askyesno("Clear", "Do you want to clear bill?")
        if op > 0:


            # =============cosmetic==========

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            # =============grocery==========

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ===============cold drinks======

            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ============total product price and tex variable============

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ==============customer======

            self.c_name.set("")
            self.c_phon.set("") 

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.search_bill.set("")
            self.bill_no.set(str(x))

            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
obj = bill_app(root)
root.mainloop()