"""
Name : Suhas Adiga
Code : Python GUI - Project Rangkosh
Details : This python code deploys a GUI for manual curation of dataset for color prediction in inorganic compounds.

Note: Currently code doesnt follow PEP-8 Guidelines
"""
# Importing all necessary library

from tkinter import *
from tkinter import ttk
import pandas as pd 
import os
import colorsys 
import pandas as pd

window = Tk()
window.geometry('1420x1580')
window.title('Project - Rangkosh Data collector')

window.config(background = '#F2F2F2')

# HEX code to RGB Convertor

def hex_to_others(value):
    value = value.lstrip('#')
    lv = len(value)
    rgb_code = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    hls_code = colorsys.rgb_to_hls(rgb_code[0]/255, rgb_code[1]/255, rgb_code[2]/255)
    return rgb_code, hls_code

# Entry Fields

entry_fields = []

# Declaring universal constants

LABEL_FONT = ("Nunito", 12, "bold")
SECTION_HEADING = ("Nunito", 14, "bold")
FG_COLOR = "#002676"
HEADING_COLOR = "#E7115E"

BG_COLOR = '#F2F2F2'

# Inorganic compound information

compound_name = Label(window,
	text = 'Name of the compound :',
	font = LABEL_FONT,
	padx = 5,
	pady = 5,
	fg = FG_COLOR,
	bg = BG_COLOR
	)

compound_name.place(x = 20, y = 20)

compound_name_entry = Entry(window, width = 30)
compound_name_entry.place(x = 430, y = 27)

## Chemical Composition 

chemical_comp = Label(window,
	text = 'Chemical Composition :',
	font = LABEL_FONT,
	padx = 5,
	pady = 5,
	fg = FG_COLOR,
	bg = BG_COLOR
	)
chemical_comp.place(x = 20, y = 90)

chemical_comp_entry = Entry(window, width = 30)
chemical_comp_entry.place(x = 430, y = 97)

# Pigment Details

pigment_no = Label(window,
	text = 'Pigment Number :',
	font = LABEL_FONT,
	padx = 5,
	pady = 5,
	fg = FG_COLOR,
	bg = BG_COLOR
	)
pigment_no.place(x = 20, y = 160)

pigment_no_entry = Entry(window, width = 15)
pigment_no_entry.place(x = 430, y = 167)

# Color Name 
color_name = Label(window,
	text = 'Color Name :',
	font = LABEL_FONT,
	padx = 5,
	pady = 5,
	fg = FG_COLOR,
	bg = BG_COLOR
	)
color_name.place(x = 750, y = 160)

color_name_entry = Entry(window, width = 25)
color_name_entry.place(x = 980, y = 167)

# Manufacturer Details

manufacturer = Label(window,
	text = 'Manufacturer :',
	font = LABEL_FONT,
	padx = 5,
	pady = 5,
	fg = FG_COLOR,
	bg = BG_COLOR
	)
manufacturer.place(x = 20, y = 230)

manufacturer_entry = Entry(window, width = 30)
manufacturer_entry.place(x = 430, y = 237)

# Color Details

heading_color = Label(window,
	text = 'Color Details',
	font = LABEL_FONT,
	fg = '#770747',
	bg = '#FFC31B',
	padx = 5,
	pady = 5,
	relief = RAISED,
	bd = 4)

heading_color.place(x = 20, y = 300)

# HEX Input 

hex_code_txt = Label(window,
	text = 'HEX Code :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)

hex_code_txt.place(x = 20, y = 370)

hex_entry = Entry(window, width = 12)
hex_entry.place(x = 220, y = 377)

rgb_code = (0, 0, 0) # Initialized the value of RGB 
hls_code = (0.0, 0.0, 0.0) # Initialized the value of HLS 

def calculate():
    global rgb_code, hls_code
    hex_code = hex_entry.get().strip()
    if not hex_code:
        return
    try:
        rgb_code, hls_code = hex_to_others(hex_code)
        red_value.config(text=str(rgb_code[0]))
        green_value.config(text=str(rgb_code[1]))
        blue_value.config(text=str(rgb_code[2]))
        hue_value.config(text=str(hls_code[0]*360))
        lightness_value.config(text=str(hls_code[1]*100))
        saturation_value.config(text=str(hls_code[2]*100))
        #print("RGB:", rgb_code)
        #print("HLS:", hls_code)
    except Exception as e:
        print("Error:", e)

button = Button(window, 
	text="Calculate", 
	font = ('Nunito', 14, 'bold'), 
	fg = '#FDB515',
	bg = '#002676',
	command=calculate)
button.place(x = 430, y = 370 )

red = Label(window,
	text = 'Red :',
	font = LABEL_FONT,
	fg = '#ED1C24',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
red.place(x = 20, y = 440)

red_value = Label(window,
	text = rgb_code[0],
	font = LABEL_FONT,
	fg = '#ED1C24',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
red_value.place(x = 180, y =440)


green = Label(window,
	text = 'Green :',
	font = LABEL_FONT,
	fg = '#00ff00',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
green.place(x = 20, y = 510)

green_value = Label(window,
	text = rgb_code[1],
	font = LABEL_FONT,
	fg = '#00ff00',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
green_value.place(x = 180, y =510)

blue = Label(window,
	text = 'Blue :',
	font = LABEL_FONT,
	fg = '#0000ff',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
blue.place(x = 20, y = 580)

blue_value = Label(window,
	text = rgb_code[2],
	font = LABEL_FONT,
	fg = '#0000ff',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
blue_value.place(x = 180, y =580)
#hex_code = hex_entry.get()
#rgb_code = hex_to_rgb(f'{hex_code}')
#print(colorsys.rgb_to_hls(0/255,74/255,174/255))

wavelength_txt = Label(window,
	text = 'λ (in nm) :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)  

wavelength_txt.place(x = 20, y = 650)

wavelength_entry = Entry(window, width = 12)
wavelength_entry.place(x = 210, y = 657)

# HSL Values

hue = Label(window,
	text = 'Hue (in °) :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
hue.place(x = 550, y = 440)

hue_value = Label(window,
	text = hls_code[0]*360,
	font = LABEL_FONT,
	fg = '#0000ff',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
hue_value.place(x = 730, y =440)


saturation = Label(window,
	text = 'Saturation (%) :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
saturation.place(x = 550, y = 510)

saturation_value = Label(window,
	text = hls_code[2]*100,
	font = LABEL_FONT,
	fg = '#0000ff',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
saturation_value.place(x = 800, y =510)

lightness = Label(window,
	text = 'Lightness (%) :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)

lightness.place(x = 550, y = 580)

lightness_value = Label(window,
	text = hls_code[1]*100,
	font = LABEL_FONT,
	fg = '#0000ff',
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
lightness_value.place(x = 800, y =580)

lrv = Label(window,
	text = 'LRV (%) :',
	font = LABEL_FONT,
	fg = FG_COLOR,
	bg = BG_COLOR,
	padx = 5,
	pady = 5
	)
lrv.place(x = 550, y = 650)

lrv_entry = Entry(window, width = 12)
lrv_entry.place(x = 700, y = 657)

heading_chemical = Label(window,
	text = 'Chemical and Structural Details',
	font = LABEL_FONT,
	fg = '#770747',
	bg = '#FFC31B',
	padx = 5,
	pady = 5,
	relief = RAISED,
	bd = 4)

heading_chemical.place(x = 20, y = 720)

mineral_name = Label(window,
	text ='Mineral :', 
	font = LABEL_FONT, 
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4)

mineral_name.place(x= 30, y= 790)

mineral_name_entry = Entry(window)
mineral_name_entry.place(x = 195, y = 797)

# Temp_critical (SuperCon-MTG) Data Entry

oxidation_state = Label(window,
	text ='Oxidation State :', 
	font = LABEL_FONT, 
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4)

oxidation_state.place(x= 30, y= 860)

oxidation_state_entry = Entry(window)
oxidation_state_entry.place(x = 310, y = 867)

# Combobox containing crystal system information

crystal_systems = ['Cubic', 'Tetragonal', 'Monoclinic', 'Orthorhombic', 'Triclinic', 'Hexagonal', 'Trigonal']

text_cs = Label(window,
	text ='Crystal System :', 
	font = LABEL_FONT, 
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4)

text_cs.place(x= 30, y= 930)

crystal_system_inp = ttk.Combobox(window, values = crystal_systems)
crystal_system_inp.set('Select a crystal system')
crystal_system_inp.place(x = 310, y = 937)

# 

text_sg = Label(window,
	text ='Space Group Number :', 
	font = LABEL_FONT, 
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4)

text_sg.place(x= 700, y= 930)

space_group_n = Entry(window, width = 8)
space_group_n.place(x = 1080, y = 937)

# Lattice Parameter Details
text_lp = Label(window,
	text = 'Lattice Parameter',
	font = LABEL_FONT, 
	bg =BG_COLOR, 
	fg =FG_COLOR,
	relief = RAISED,
	bd = 4,
	padx = 10,
	pady =10)

text_lp.place(x = 30, y = 1000)

text_ang = Label(window, 
	text = 'in Å',
	font = ('Nunito', 9, 'italic'),
	bg =BG_COLOR, 
	fg =FG_COLOR)

text_ang.place(x = 195, y = 1097)

text_lp_a = Label(window,
	text = 'a :',
	font = ('Nunito', 12, 'bold'),
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

text_lp_a.place(x = 30, y = 1090)

lattice_parameter_a = Entry(window, width = 6)
lattice_parameter_a.place(x = 80, y = 1097)

# lattice parameter - b
text_lp_b = Label(window,
	text = 'b :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

text_lp_b.place(x = 30, y = 1160)

text_ang_b = Label(window, 
	text = 'in Å',
	font = ('Nunito', 9, 'italic'),
	bg =BG_COLOR, 
	fg =FG_COLOR)

text_ang_b.place(x = 195, y = 1167)

lattice_parameter_b = Entry(window, width = 6)
lattice_parameter_b.place(x = 80, y = 1167)

# Warning

warning = Label(window,
	text = 'Cubic → a = b = c',
	font = ('Nunito', 9 , 'bold'),
	bg =BG_COLOR, 
	fg ='#900000',
	padx = 4,
	pady =4)

warning.place(x = 280, y = 1097)

warning_1 = Label(window,
	text = 'Monoclinic and Orthorhombic → a ≠ b ≠ c',
	font = ('Nunito', 9 , 'bold'),
	bg =BG_COLOR, 
	fg ='#900000',
	padx = 4,
	pady =4)

warning_1.place(x = 280, y = 1167)

warning_2 = Label(window,
	text = 'Trigonal, Tetragonal and Hexagonal → a = b ≠ c',
	font = ('Nunito', 9 , 'bold'),
	bg =BG_COLOR, 
	fg ='#900000',
	padx = 4,
	pady =4)

warning_2.place(x = 280, y = 1237)

# lattice parameter - c
text_lp_c = Label(window,
	text = 'c :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

text_lp_c.place(x = 30, y = 1230)

text_ang_c = Label(window, 
	text = 'in Å',
	font = ('Nunito', 9, 'italic'),
	bg =BG_COLOR, 
	fg =FG_COLOR)

text_ang_c.place(x = 195, y = 1237)

lattice_parameter_c = Entry(window, width = 6)
lattice_parameter_c.place(x = 80, y = 1237)

# Bandgap 
bandgap_text = Label(window,
	text = 'Bandgap :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

bandgap_text.place(x = 30, y = 1290)

bandgap_unit = Label(window, 
	text = 'in eV',
	font = ('Nunito', 9, 'italic'),
	bg =BG_COLOR, 
	fg =FG_COLOR)

bandgap_unit.place(x = 315, y = 1297)

bandgap_entry = Entry(window, width = 6)
bandgap_entry.place(x = 210, y = 1297)

# Refractive Index 
refractive_text = Label(window,
	text = 'Refractive Index :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

refractive_text.place(x = 450, y = 1290)

refractive_entry = Entry(window, width = 6)
refractive_entry.place(x = 750, y = 1297)

# Density 
density_text = Label(window,
	text = 'Density :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

density_text.place(x = 900, y = 1290)

density_unit = Label(window, 
	text = 'in g/cm³',
	font = ('Nunito', 9, 'italic'),
	bg =BG_COLOR, 
	fg =FG_COLOR)

density_unit.place(x = 1160, y = 1297)

density_entry = Entry(window, width = 6)
density_entry.place(x = 1050, y = 1297)

# SMILES 
smiles_text = Label(window,
	text = 'SMILES :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

smiles_text.place(x = 30, y = 1360)

smiles_entry = Entry(window, width = 50)
smiles_entry.place(x = 180, y = 1367)

# Reference 
reference_text = Label(window,
	text = 'Reference :',
	font = LABEL_FONT,
	bg =BG_COLOR, 
	fg =FG_COLOR,
	padx = 4,
	pady =4
	)

reference_text.place(x = 30, y = 1430)

reference_entry = Entry(window, width = 50)
reference_entry.place(x = 230, y = 1437)


entry_fields = [compound_name_entry, chemical_comp_entry, pigment_no_entry, manufacturer_entry, hex_entry, wavelength_entry, lrv_entry, mineral_name_entry, oxidation_state_entry, space_group_n, lattice_parameter_a, lattice_parameter_b, lattice_parameter_c, bandgap_entry, refractive_entry, density_entry, smiles_entry, reference_entry]

def reset_fields():
	for entry in entry_fields:
		entry.delete(0, END)

def entry_to_csv():
    compound_name_data = compound_name_entry.get()
    chemical_comp_data = chemical_comp_entry.get()
    pigment_no_data = pigment_no_entry.get()
    manufacturer_data = manufacturer_entry.get()
    color_name_data = color_name_entry.get()
    hex_code_data = hex_entry.get()
    red_data = rgb_code[0]
    green_data = rgb_code[1]
    blue_data = rgb_code[2] 
    hue_data = hls_code[0]*360
    saturation_data = hls_code[2]*100
    lightness_data = hls_code[1]*100
    wavelength_data = wavelength_entry.get()
    lrv_data = lrv_entry.get()
    mineral_name_data = mineral_name_entry.get()
    oxidation_state_data = oxidation_state_entry.get()
    space_group_n_data = space_group_n.get()
    bandgap_data = bandgap_entry.get()
    refractive_data = refractive_entry.get()
    density_data = density_entry.get()
    smiles_data = smiles_entry.get()
    reference_data = reference_entry.get()
    crystal_system_entry = crystal_system_inp.get()

    # Conditionals for lattice parameters based on crystal system
    if crystal_system_entry == 'Cubic':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_a_entry
    	lattice_parameter_c_entry = lattice_parameter_a_entry

    if crystal_system_entry == 'Monoclinic':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_b.get()
    	lattice_parameter_c_entry = lattice_parameter_c.get()

    if crystal_system_entry == 'Tetragonal':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_a_entry
    	lattice_parameter_c_entry = lattice_parameter_c.get()

    if crystal_system_entry == 'Orthorhombic':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_b.get()
    	lattice_parameter_c_entry = lattice_parameter_c.get()
    
    if crystal_system_entry == 'Triclinic':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_b.get()
    	lattice_parameter_c_entry = lattice_parameter_c.get()

    if crystal_system_entry == 'Hexagonal':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_a_entry
    	lattice_parameter_c_entry = lattice_parameter_c.get()

    if crystal_system_entry == 'Trigonal':
    	lattice_parameter_a_entry = lattice_parameter_a.get()
    	lattice_parameter_b_entry = lattice_parameter_a_entry
    	lattice_parameter_c_entry = lattice_parameter_c.get()


    # Prepare new row as a DataFrame
    new_row = pd.DataFrame([[compound_name_data, chemical_comp_data,pigment_no_data, manufacturer_data, color_name_data, hex_code_data, red_data, green_data, blue_data, hue_data, saturation_data,lightness_data, wavelength_data, mineral_name_data, lrv_data, oxidation_state_data, space_group_n_data, crystal_system_entry, lattice_parameter_a_entry, lattice_parameter_b_entry, lattice_parameter_c_entry, bandgap_data, refractive_data,
    	density_data, smiles_data, reference_data
    ]], columns=['Name of Compound', 'Chemical Composition', 'Pigment No',
       'Manufacturer', 'Color Name', 'Hex Code', 'Red', 'Green', 'Blue',
       'Hue (degrees)', 'Saturation (%)', 'Lightness (%)', 'lambda (nm)',
       'Minerals', 'LRV (%)', 'Oxidation States', 'Space Group Number',
       'Crystal System', 'a', 'b', 'c',  'Band Gap (eV)', 'Refractive Index',
       'Density (g/cm^3)', 'SMILES', 'Reference'
])

    filename = 'Rangkosh_Output.csv'
    file_exists_and_not_empty = os.path.isfile(filename) and os.path.getsize(filename) > 0

    new_row.to_csv(filename, mode='a', index=False, header=not file_exists_and_not_empty)
    print("Data appended successfully!")




button = Button(window, 
	text="Submit entry", 
	font = ('Nunito', 14, 'bold'), 
	fg = '#FDB515',
	bg = '#002676',
	command=entry_to_csv)

button.place(x = 750, y = 1500 )




reset_btn = Button(window, 
	text="Reset entries",
	font = ('Nunito', 14, 'bold'), 
	fg = '#FDB515',
	bg = '#002676', 
	command=reset_fields)

reset_btn.place(x = 300, y = 1500)




window.mainloop()