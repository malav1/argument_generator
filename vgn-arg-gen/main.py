from random import choice
from guizero import App, Text, PushButton, Combo

#PROCESSING FILE
file = open("args.csv","r")
args_and_rank=[]
for line in file:
    line=line.strip().split(",")
    args_and_rank.append(line)

#creating new lists based on difficulty
args_1=[element[0] for element in args_and_rank if element[1]=="1"]
args_2=[element[0] for element in args_and_rank if element[1]=="2"]
args_3=[element[0] for element in args_and_rank if element[1]=="3"]
args_4=[element[0] for element in args_and_rank if element[1]=="4"]

#GUI
#gen_button will gen arg based on rank_button difficulty
def pick_arg():
    # chosen_arg=None
    if rank_button.value == "1":
        chosen_arg=choice(args_1)
    elif rank_button.value == "2":
        chosen_arg=choice(args_2)
    elif rank_button.value == "3":
        chosen_arg=choice(args_3)
    else:
        chosen_arg=choice(args_4)
    #line break if line char count too high
    if len(chosen_arg)>50:
        new_chosen_arg=chosen_arg[50:].replace(" ","\n",1)
        display_arg.value = f"\n\n{chosen_arg[0:50]}{new_chosen_arg}"
    else:
        display_arg.value = f"\n\n{chosen_arg}"

  
app = App(bg = "white", title="Vegan Argument Generator",height=200, width=500)

rank_button=Combo(app, options=["1","2","3","4"])
gen_button=PushButton(app, text="Generate Argument", command=pick_arg)
display_arg = Text(app, text="")
    
app.display()