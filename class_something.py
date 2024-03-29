
from tkinter import *

custom_colors_dict = {
    'queen_blue':'#467599',
    'blizzard_blue':'#beecf6',
    'light_cyan':'#e9fff9',
    'fire_engine':'#ce2029',
    'oxfor_blue':'#000022',
    'pakistan_green':'#006600'
}

font_type = 'Arial'
font_size = 20
font_kind = 'bold'
FONT_DEFINITIONS = (font_type, font_size, font_kind)

CNPJ_CHAR_QUANTITY = 14
MONEY_CHAR_QUANTITY = 10
QUANTITY_CHAR_QUANTITY = 10 #TODO: rename this variable
TEXT_CHAR_QUANTITY = 50

root_w = Tk()


class EntryFieldForm(Frame):
    def __init__(self, window, label_text, **kwargs):
        super().__init__(window, **kwargs)

        #TODO: using for debugging, remove later
        self.config(bg=custom_colors_dict['queen_blue'], borderwidth=2)

        # initializing the widgets inside the frame
        self.text_label = Label(self)
        self.entry_box = Entry(self)

        # Creating a variable to hold the entr widget text
        # TODO: Remove this starting value, it is here for tests only
        self.text_variable = StringVar(self.entry_box, value="test")

        # changing configuration for widgets
        self.text_label.config(
            font=FONT_DEFINITIONS,
            text=" " + label_text + " ",
            borderwidth=1,
            bg=custom_colors_dict["blizzard_blue"]
        )

        self.entry_box.config(
            font=FONT_DEFINITIONS,
            textvariable=self.text_variable,
            bg=custom_colors_dict['light_cyan']
        )

        # placing widgets on the grid inside the frame
        # both on the same row, different columns
        self.text_label.grid(
            row=0,
            column=0,
            sticky=EW,
            padx=(0,3)
        )

        self.entry_box.grid(
            row=0,
            column=1,
            sticky=EW
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)

    def get_entry_text(self):
        return self.text_variable.get()

    def set_entry_text(self, text):
        self.text_variable.set(text)

    def clear_entry_field_text(self):
        self.text_variable.set("")

class FinishingButton(Button):
    def __init__(self, window, button_display_text, **kwargs):
        super().__init__(window, **kwargs)

        border_size = 3

        self.config(
            #TODO: review this color later
            fg="white",
            text=button_display_text,
            borderwidth=border_size,
            font=FONT_DEFINITIONS
        )

    def function_to_call_when_pressed(self, function_address):
        self.config(command=function_address)

class CnpjEntry(EntryFieldForm):
    
    def __init__(self, window, label_text, **kwargs):
        super().__init__(window, label_text, **kwargs)

        cnpj_validate_command = (root_w.register(self.validade_entry), '%P')

        self.entry_box.config(
            validate='key', # this will invoke the validate command when a key is pressed
            validatecommand= cnpj_validate_command
        )

    def validade_entry(self, entry_text_plus_new_char):

        """
        This will check if the new char can be added or removed from the entry.
        Ther rules are:
            - it must be a digit
            - the entry cannot exceed 14 digits
            - the entry can be blank
        """

        text_size = len(entry_text_plus_new_char)

        entry_is_digit = entry_text_plus_new_char.isdigit()
        entry_is_less_than_14_chars = text_size <= CNPJ_CHAR_QUANTITY
        entry_is_empty = text_size == 0

        entry_is_valid = entry_is_less_than_14_chars and (
            entry_is_digit or entry_is_empty
            )

        if entry_is_valid:
            return True
        else:
            return False

class MoneyEntry(EntryFieldForm):
    def __init__(self, window, label_text, **kwargs):
        super().__init__(window, label_text, **kwargs)

        money_validate_command = (root_w.register(self.validade_entry), '%P')

        self.entry_box.config(
            validate='key', # this will invoke the validate command when a key is pressed
            validatecommand= money_validate_command
        )

    def validade_entry(self, entry_text_plus_new_char):

        """
        This will check if the new char can be added or removed from the entry.
        Ther rules are:
            - it must be a digit
            - the entry cannot exceed 10 digits
            - the entry can be blank
        """

        text_size = len(entry_text_plus_new_char)

        entry_is_digit = entry_text_plus_new_char.isdigit()
        entry_is_less_than_10_chars = text_size <= MONEY_CHAR_QUANTITY
        entry_is_empty = text_size == 0

        entry_is_valid = entry_is_less_than_10_chars and (
            entry_is_digit or entry_is_empty
            )

        if entry_is_valid:
            return True
        else:
            return False

class QuantityEntry(EntryFieldForm):
    def __init__(self, window, label_text, **kwargs):
        super().__init__(window, label_text, **kwargs)

        quant_validate_command = (root_w.register(self.validade_entry), '%P')

        self.entry_box.config(
            validate='key', # this will invoke the validate command when a key is pressed
            validatecommand= quant_validate_command
        )

    def validade_entry(self, entry_text_plus_new_char):

        """
        This will check if the new char can be added or removed from the entry.
        Ther rules are:
            - it must be a digit
            - the entry cannot exceed 10 digits
            - the entry can be blank
        """

        text_size = len(entry_text_plus_new_char)

        entry_is_digit = entry_text_plus_new_char.isdigit()
        entry_is_less_than_10_chars = text_size <= QUANTITY_CHAR_QUANTITY
        entry_is_empty = text_size == 0

        entry_is_valid = entry_is_less_than_10_chars and (
            entry_is_digit or entry_is_empty
            )

        if entry_is_valid:
            return True
        else:
            return False

class TextEntry(EntryFieldForm):
    def __init__(self, window, label_text, **kwargs):
        super().__init__(window, label_text, **kwargs)

        text_validate_command = (root_w.register(self.validade_entry), '%P')

        self.entry_box.config(
            validate='key', # this will invoke the validate command when a key is pressed
            validatecommand= text_validate_command
        )

    def validade_entry(self, entry_text_plus_new_char):

        """
        This will check if the new char can be added or removed from the entry.
        Ther rules are:
            - The entry cannot exceed 50 chars
        """

        entry_length = len(entry_text_plus_new_char)

        entry_is_less_than_50_chars = entry_length <= TEXT_CHAR_QUANTITY

        if entry_is_less_than_50_chars:
            return True
        else:
            return False


entry_fields_frame = Frame(root_w)

cnpj_remetente_entry_field = CnpjEntry(entry_fields_frame, "CNPJ REMETENTE")

cnpj_destino_entry_field= CnpjEntry(entry_fields_frame, "CNPJ DESTINATARIO")

valor_nota_entry_field = MoneyEntry(entry_fields_frame, "VALOR DA NOTA")

peso_entry_field = QuantityEntry(entry_fields_frame, "PESO")

volume_entry_field = QuantityEntry(entry_fields_frame, "VOLUME")

medidas_entry_field = QuantityEntry(entry_fields_frame, "MEDIDAS")

pagador_frete_entry_field = TextEntry(entry_fields_frame, "PAGADOR DO FRETE")

entrega_zona_rural_entry_field = TextEntry(entry_fields_frame, "ZONA RURAL")

entry_fields_list = [
    cnpj_remetente_entry_field,
    cnpj_destino_entry_field,
    valor_nota_entry_field,
    peso_entry_field,
    volume_entry_field,
    medidas_entry_field,
    pagador_frete_entry_field,
    entrega_zona_rural_entry_field
]

for entry_field in entry_fields_list:
    entry_field_index = entry_fields_list.index(entry_field)

    entry_field.grid(row=entry_field_index, sticky=EW)
    
# TODO: This seems odd. It doesn't feel right
def clear_text_from_all_entry_fields():
    for entry in entry_fields_list:
        entry.clear_entry_field_text()

def copy_text_from_all_entry_fields():
    final_text = ""

    for entry in entry_fields_list:
        entry_name = entry.text_label.cget('text')
        entry_text = entry.get_entry_text() + "\n"

        final_text += entry_name + entry_text
    else: # This removes the last '\n' which adds a new line
        final_text = final_text[:-1]

    # for the moment it will only print the result
    # don't want to fill my clipboard with it
    print(final_text)


#TODO: using for debugging, remove later
buttons_frame = Frame(root_w, borderwidth=1, bg=custom_colors_dict['oxfor_blue'])

button_delete = FinishingButton(buttons_frame, "APAGAR")
button_delete.config(bg=custom_colors_dict['fire_engine'])

button_copy = FinishingButton(buttons_frame, "COPIAR")
button_copy.config(bg=custom_colors_dict['pakistan_green'])

button_delete.function_to_call_when_pressed(clear_text_from_all_entry_fields)

button_copy.function_to_call_when_pressed(copy_text_from_all_entry_fields)


# Both buttons on the same row, diferent columns
button_delete.grid(row=0, column=0)
button_copy.grid(row=0, column=1)

# This places the buttons on the middle of its space at the grid
buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)

# This allows the widgets to expand inside the frame
entry_fields_frame.grid_columnconfigure(0, weight=1)

# This stretches both widgets horizontally on the screen
entry_fields_frame.grid(row=0, column=0, sticky=EW)
buttons_frame.grid(row=1, column=0, sticky=EW)

#TODO: if the main window will have a fixed size, this is not needed
# root_w.grid_columnconfigure(0, weight=1)
# root_w.grid_rowconfigure(0, weight=1)
# root_w.grid_rowconfigure(1, weight=1)

#TODO: using for debugging, remove later
root_w.update()
print(root_w.winfo_geometry())


root_w.mainloop()
