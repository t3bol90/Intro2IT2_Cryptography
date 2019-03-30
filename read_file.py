import hashlib

#hàm load file account.txt và save vào account_hash.txt
def hash_txt_save():
	filein=open('account.txt','r')
	a=filein.readlines()
	i=0
	while(i<len(a)):
		hash_array=hashlib.sha256(a[i].encode())
		wow=hash_array.hexdigest()
		fileout=open('account_hash.txt','a')
		fileout.write(wow+'\n')
		i=i+1

#hàm thêm một account mới
def create_username_password():
	print("SIGN UP")

	print("user name: ")
	temp_user_name=input()
	user_name=temp_user_name+'\n'
	hash_user=hashlib.sha256(user_name.encode())
	hash_user_name=hash_user.hexdigest()

	print("password: ")
	password=input()
	#pasword=temp_password+'\n'
	hash_pass=hashlib.sha256(password.encode())
	hash_password=hash_pass.hexdigest()

	filein=open('account_hash.txt','r')
	a=filein.readlines() #đọc từng dòng vd: a[0] sẽ là dòng đầu tiên
	#mảng a chứa user name và password
	i=0
	#while này là thêm vào account_hash
	while(i<len(a)):
		if(a[i]==hash_user_name+'\n'):#kiểm tra user có tồn tại hay chưa
			print("account already exists ")
			create_username_password()
			break;
			
		if(i==len(a)-1): #đọc tới cuối file nếu ko khớp thì tạo mới
			fileout=open('account_hash.txt','a+')#ghi vào cuối file
			fileout.write(hash_user_name+'\n')
			fileout.write(hash_password+'\n')

			fiout=open('account.txt','a+')
			fiout.write(user_name)
			fiout.write(password+'\n')

			print("add successfully")
			break;
		i=i+1

def login():
	filein=open('account_hash.txt','r')
	a=filein.readlines()
	print("LOGIN")

	print("user name: ")
	temp_user_name=input()
	user_name=temp_user_name+'\n'
	hash_user=hashlib.sha256(user_name.encode())
	hash_user_name=hash_user.hexdigest()

	print("password: ")
	temp_password=input()
	password=temp_password+'\n'
	hash_pass=hashlib.sha256(password.encode())
	hash_password=hash_pass.hexdigest()

	filein=open('account_hash.txt','r')
	a=filein.readlines() 
	i=0
	
	while(i<len(a)):
		if((a[i]==hash_user_name+'\n')and(a[i+1]==hash_password+'\n')):
			print("Login successfully ")
			#ở đây sẽ thêm hàm tiếp
			break;
			
		if(i==len(a)-1): 

			print("Login Failed")
			break;
		i=i+1

#from graphics import*
import graphics

win = graphics.GraphWin("win",200,150)
def buttons():
    rectangle = graphics.Rectangle(Point(30,85),Point(60,55))
    rectangle2 = graphics.Rectangle(Point(170,85),Point(140,55))
    rectangle.setFill("blue")
    rectangle2.setFill("blue")
    rectangle.draw(win)
    rectangle2.draw(win)

	