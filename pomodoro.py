import tkinter as tk

#creating the main application window
root=tk.Tk()
root.title("POMODORO timer ;)")
root.geometry("300x200")

#the visuals
timer_cnt=tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_cnt.pack(pady=20)

time_left=25*60
timer_running=False



def update_timer():
#global is the keyword to tell Python to modify both simultaneously
    global time_left, timer_running
    if timer_running and  time_left>0:
        minutes=time_left//60
        seconds=time_left%60
        timer_cnt.config(text=f"{minutes:02d}:{seconds:02d}")

        time_left -=1
        root.after(1000,update_timer)
    elif time_left==0:
        timer_cnt.config(text="00:00")
        timer_running=False
        
def start_timer():
    global timer_running
    if not timer_running:
        timer_running=True
        update_timer()

def pause_timer():
    global timer_running
    timer_running=False

def reset_timer():
    global time_left, timer_running
    timer_running=False
    time_left=25*60
    timer_cnt.config(text="25.00")
    
cadre_boutons=tk.Frame(root)
cadre_boutons.pack(pady=10)


start_button=tk.Button(cadre_boutons, text="Start",command=start_timer)
pause_button=tk.Button(cadre_boutons, text="Pause",command=pause_timer)
reset_button=tk.Button(cadre_boutons, text="Reset",command=reset_timer)



start_button.config(command=start_timer)
pause_button.config(command=pause_timer)
reset_button.config(command=reset_timer)

start_button.pack(side="left", padx=5)
pause_button.pack(side="left", padx=5)
reset_button.pack(side="left", padx=5)


root.mainloop()


