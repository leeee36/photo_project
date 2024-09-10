from tkinter import *

root = Tk()                      # 창을 생성
root.geometry("600x400")         # 창 크기설정
root.title("jpg and dng")        # 창 제목설정
root.resizable(False, False)     # x, y 창 크기 변경 불가

# ===== Functions ===== #

# def delete_btn():
#     text1.delete('0', END)
#     text2.delete('0', END)

def btnpress():
    a = []
    if chkvar.get() == 1:         # 체크박스가 체크 되었는지 확인
        a.append("JPG")
    if chkvar1.get() == 1:
        a.append("DNG")
    if chkvar2.get() == 1:
        a.append("RAW")
    lb.config(text =a)

# ===== Checkbox ===== #

chkvar = IntVar()                            # chkvar 에 int 형으로 값을 저장
chkbox = Checkbutton(root, variable=chkvar)  # root라는 창에 체크 박스 생성
chkbox.config(text="JPG")                    # 체크박스에 나타낼 내용 설정
chkbox.pack()                                # 체크박스 배치

chkvar1 = IntVar()                            
chkbox1 = Checkbutton(root, variable=chkvar1)
chkbox1.config(text="DNG")                  
chkbox1.pack()              

chkvar2 = IntVar()                       
chkbox2 = Checkbutton(root, variable=chkvar2) 
chkbox2.config(text="RAW")             
chkbox2.pack()  

lb = Label(root)
lb.pack()

# # ===== text box ===== #

# t1 = Label(root)
# t1.config(text='JPG')
# t1.pack()

# text1 = Entry(root)
# text1.config(width=30)
# text1.pack()

# t2 = Label(root)
# t2.config(text='DNG')
# t2.pack()

# text2 = Entry(root)
# text2.config(width=30)
# text2.pack()

# delete = Button(root)                    # root라는 창에 버튼 생성
# delete.config(text= "삭제")               # 버튼 내용 
# delete.config(width=10)                  # 버튼 크기
# delete.config(command=delete_btn)        # 버튼 기능 (delete_btnpree() 함수 호출)
# delete.pack()                            # 버튼 배치

root.mainloop()