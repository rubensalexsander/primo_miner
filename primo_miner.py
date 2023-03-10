from libs.arq_manipulator import Arq_txt
from libs.pyprimo import *
from tkinter import *
from tkinter import ttk
import shutil
from format_numbers import *

minning = True
running = True

def main():
    global running

    # Configs ---------------------------------------
    arq = r'./primos_found.txt'
    save_len = 10000
    arq_lenth_primos = 10000000
    #------------------------------------------------
    
    arq_txt = Arq_txt(arq)
    first_arq_number = int(arq_txt.get_lines(-1))
    first_number_find = first_arq_number
    last_arq_number = first_arq_number+arq_lenth_primos

    def print_settings():
        print('### Primo_Miner RUNNING ###\n')
        print(f'Local_arq: {arq}')
        print(f'First_minering_number: {first_arq_number}\n')
    print_settings()

    # Front sets ------------------------------------
    root = Tk()
    root.title("Primo_Miner")
    geometry = (350, 200)
    root.minsize(geometry[0], geometry[1]), root.maxsize(geometry[0], geometry[1]) 

    frm = ttk.Frame(root, padding=10)
    frm.pack(side=TOP, fill=X)

    label_path = ttk.Label(frm, text='Local: \n'+arq, font=("Arial", 8))
    label_path.pack(side=TOP, anchor='w', pady=5)

    label_state_var = StringVar()
    label_state_var.set(f'Running: {minning}')

    label_state = ttk.Label(frm, textvariable=label_state_var, padding=2)
    label_state.pack(side=TOP, pady=10)

    def change_state():
        global minning
        if minning:
            minning = False
            bt_state.config(text='Iniciar')
            label_state.config(background='red')
            print('Paused\n')
        else:
            minning = True
            bt_state.config(text='Pausar')
            label_state.config(background='green')
            print('Started\n')

        label_state_var.set(f'Minning: {minning}')

    bt_state = ttk.Button(command=change_state)
    bt_state.pack()

    def quit():
        global running
        root.destroy()
        running = False

    bt_quit = ttk.Button(text='Sair', command=quit)
    bt_quit.pack()
    #------------------------------------------------

    change_state()
    change_state()
    
    #first_number = int(arq_txt.get_lines(-1))
    #last_number = first_number+arq_lenth_primos
    
    while running:
        if first_number_find < last_arq_number:
            if minning:
                new_primos = find_primos(first_number_find, first_number_find+save_len)
                first_number_find += save_len
                if len(new_primos) > 0:
                    primos_line = ''
                    for n in new_primos:
                        primos_line += str(n)+','
                    arq_txt.rewrite_line(primos_line)
                    n_lines = len(arq_txt.get_lines('all'))
                    arq_txt.rewrite_line(str(first_number_find), n_lines)
        else:
            #Copia arquivo para founds com nome de 'primo_found (até first_number).txt'
            dest = f'./founds/primos_found (até {first_number_find}).txt'
            
            #format arq
            format_numbers(arq, ',', 10)
            print('Novo arquivo criado.')
            print(f'first number: {first_number_find}\n')
             
            shutil.copy(arq, dest)
            #Reescrever first_number no arquivo
            arq_txt.rewrite_all([str(first_number_find)])
            
            last_arq_number += arq_lenth_primos
            

        root.update()

if __name__ == '__main__':
    main()
