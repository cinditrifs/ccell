import view_login
import view_main_menu

def auth (self):
        key = self.username.get()
        password = self.password.get()
        #print (type(password))
        pass_auth = (str(ccell.hmget(key, 'password'))).replace('b','')
        pass_auth = pass_auth.replace(']', '')
        pass_auth = pass_auth.replace('[', '')
        pass_auth = pass_auth.replace("'", '')
        #print(type(pass_auth))
        if password == pass_auth :
            self.auth = Toplevel(self.master)
            self.app= main_menu(self.auth)    
            self.main_menu = view_main_menu()
        else :
            messagebox.showinfo("failed", "Usename dan Password tidak sama")


        
