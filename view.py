from tkinter import Label
from tkinter import Entry
from tkcalendar import DateEntry
from tkinter import W
from tkinter import N
from tkinter import Button
from model import CRUD
from tkinter import Toplevel
from tkinter import IntVar, StringVar, DoubleVar
from tkinter import ttk
import tkinter as tk
from tkinter import HORIZONTAL
from tkinter import VERTICAL
from tkinter import NS
from tkinter import EW


class MyErpApp:

    def __init__(self, interface_view):
        ventana_emergente_t = interface_view
        ventana_emergente_t.title("ERP TEST")
        ventana_emergente_t.config(bg="#1E90FF")
        ventana_emergente_t.geometry("300x300")

        estilo_botones = {'background': '#E4E4E4', 'borderwidth': 0}
        self.crud_object = CRUD()
        boton_1 = Button(
            ventana_emergente_t,
            text="New Buy Order",
            padx=10,
            pady=5,
            command=self.v_buys_orders_new,
            **estilo_botones
        )
        boton_1.pack(pady=(50, 5))

        boton_2 = Button(
            ventana_emergente_t,
            text="New Sell Order",
            padx=10,
            pady=5,
            command=self.v_sell_orders_new,
            **estilo_botones
        )
        boton_2.pack(pady=5)

        boton_3 = Button(
            ventana_emergente_t,
            text="Buy Orders List",
            padx=10,
            pady=5,
            command=self.v_buys_orders,
            **estilo_botones
        )
        boton_3.pack(pady=5)

        boton_3_a = Button(
            ventana_emergente_t,
            text="Sell Orders List",
            padx=10,
            pady=5,
            command=self.v_sell_orders,
            **estilo_botones
        )
        boton_3_a.pack(pady=5)

        boton_4 = Button(
            ventana_emergente_t,
            text="Clients",
            padx=10,
            pady=5,
            command=self.v_client_list,
            **estilo_botones
        )
        boton_4.pack(pady=5)

        boton_5 = Button(
            ventana_emergente_t,
            text="Suppliers",
            padx=10,
            pady=5,
            command=self.v_suppliers_list,
            **estilo_botones
        )
        boton_5.pack(pady=5)

    def v_client_list(self):
        ventana_emergente_client_list = Toplevel()
        ventana_emergente_client_list.title("Client List")
        (
            var_id,
            var_client,
            var_client_num,
            var_phone_number,
            var_address,
            var_email,
            var_city,
            var_zip_code,
            var_bill_address,
            var_fax
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar()
        )

        titulo = Label(
            ventana_emergente_client_list,
            text="Client Name"
            )
        titulo.grid(
            row=1,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Client Num"
        )
        titulo.grid(
            row=1,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Phone Num"
            )
        titulo.grid(
            row=2,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Address"
            )
        titulo.grid(
            row=2,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Email"
            )
        titulo.grid(
            row=3,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="City"
            )
        titulo.grid(
            row=4,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Zip Code"
            )
        titulo.grid(
            row=3,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_client_list,
            text="Bill Address"
        )
        titulo.grid(
            row=4,
            column=2
        )
        titulo = Label(
            ventana_emergente_client_list,
            text="Fax"
        )
        titulo.grid(
            row=5,
            column=0
        )
        entry_s = Entry(
            ventana_emergente_client_list,
            text=var_client,
            width=50
            )
        entry_s.grid(
            row=1,
            column=1
            )
        entry_t = Entry(
            ventana_emergente_client_list,
            text=var_client_num,
            width=50
            )
        entry_t.grid(
            row=1,
            column=3
            )
        entry_i = Entry(
            ventana_emergente_client_list,
            text=var_phone_number,
            width=50
            )
        entry_i.grid(
            row=2,
            column=1
            )
        entry_o = Entry(
            ventana_emergente_client_list,
            text=var_address,
            width=50
            )
        entry_o.grid(row=2, column=3)

        entry_email = Entry(
            ventana_emergente_client_list,
            text=var_email,
            width=50
            )
        entry_email.grid(
            row=3,
            column=1
            )
        entry_total = Entry(
            ventana_emergente_client_list,
            text=var_city,
            width=50
            )
        entry_total.grid(
            row=4,
            column=1
            )
        entry_import_type = Entry(
            ventana_emergente_client_list,
            text=var_zip_code,
            width=50
            )
        entry_import_type.grid(
            row=3,
            column=3
            )
        entry_import_type = Entry(
            ventana_emergente_client_list,
            text=var_bill_address,
            width=50
            )
        entry_import_type.grid(
            row=4,
            column=3
            )
        entry_import_type = Entry(
            ventana_emergente_client_list,
            text=var_fax,
            width=50
            )
        entry_import_type.grid(
            row=5,
            column=1
            )
        tree = ttk.Treeview(ventana_emergente_client_list)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
            "col9",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.column("col8", width=20, minwidth=50, anchor=W)
        tree.column("col9", width=20, minwidth=50, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Client")
        tree.heading("col2", text="Client Num")
        tree.heading("col3", text="Phone Number")
        tree.heading("col4", text="Address")
        tree.heading("col5", text="Email")
        tree.heading("col6", text="City")
        tree.heading("col7", text="Zip code")
        tree.heading("col8", text="Bill Adress")
        tree.heading("col9", text="Fax")

        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_client_list,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_client_list, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_client_list,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_clients(tree)
            )

        boton_1.grid(
            row=1,
            column=4
            )

        boton_2 = Button(
            ventana_emergente_client_list,
            text="Modify client",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.fun_update_client(
                var_client,
                var_client_num,
                var_phone_number,
                var_address,
                var_email,
                var_city,
                var_zip_code,
                var_bill_address,
                var_fax,
                tree
            ),
        )

        boton_2.grid(
            row=2,
            column=4
            )
        boton_3 = Button(
            ventana_emergente_client_list,
            text="Delete client",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.delete_client(
                var_id,
                tree
            ),
        )
        boton_3.grid(
            row=3,
            column=4
            )

        boton_4 = Button(
            ventana_emergente_client_list,
            text="Save",
            padx=51,
            pady=1,
            command=lambda: self.crud_object.fun_new_client(
                var_client,
                var_client_num,
                var_phone_number,
                var_address,
                var_email,
                var_city,
                var_zip_code,
                var_bill_address,
                var_fax,
                tree
            ),
        )
        boton_4.grid(
            row=7,
            column=4
            )

    def v_suppliers_list(self):
        ventana_emergente_suppliers = Toplevel()
        ventana_emergente_suppliers.title("Suppliers list")

        (
            var_id,
            var_supplier,
            var_supplier_num,
            var_phone_number,
            var_address,
            var_email,
            var_city,
            var_zip_code,
            var_bill_address,
            var_fax
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar()
        )

        titulo = Label(
            ventana_emergente_suppliers,
            text="Supplier Name"
            )
        titulo.grid(
            row=1,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Supplier Num"
        )
        titulo.grid(
            row=1,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Phone Num"
            )
        titulo.grid(
            row=2,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Address"
            )
        titulo.grid(
            row=2,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Email"
            )
        titulo.grid(
            row=3,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="City"
            )
        titulo.grid(
            row=4,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Zip Code"
            )
        titulo.grid(
            row=3,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Bill Address"
        )
        titulo.grid(
            row=4,
            column=2
        )
        titulo = Label(
            ventana_emergente_suppliers,
            text="Fax"
        )
        titulo.grid(
            row=5,
            column=0
        )
        entry_s = Entry(
            ventana_emergente_suppliers,
            text=var_supplier,
            width=50
            )
        entry_s.grid(
            row=1,
            column=1
            )
        entry_t = Entry(
            ventana_emergente_suppliers,
            text=var_supplier_num,
            width=50
            )
        entry_t.grid(
            row=1,
            column=3
            )
        entry_i = Entry(
            ventana_emergente_suppliers,
            text=var_phone_number,
            width=50
            )
        entry_i.grid(
            row=2,
            column=1
            )
        entry_o = Entry(
            ventana_emergente_suppliers,
            text=var_address,
            width=50
            )
        entry_o.grid(row=2, column=3)

        entry_email = Entry(
            ventana_emergente_suppliers,
            text=var_email,
            width=50
            )
        entry_email.grid(
            row=3,
            column=1
            )
        entry_total = Entry(
            ventana_emergente_suppliers,
            text=var_city,
            width=50
            )
        entry_total.grid(
            row=4,
            column=1
            )
        entry_import_type = Entry(
            ventana_emergente_suppliers,
            text=var_zip_code,
            width=50
            )
        entry_import_type.grid(
            row=3,
            column=3
            )
        entry_import_type = Entry(
            ventana_emergente_suppliers,
            text=var_bill_address,
            width=50
            )
        entry_import_type.grid(
            row=4,
            column=3
            )
        entry_import_type = Entry(
            ventana_emergente_suppliers,
            text=var_fax,
            width=50
            )
        entry_import_type.grid(
            row=5,
            column=1
            )
        tree = ttk.Treeview(ventana_emergente_suppliers)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
            "col9",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.column("col8", width=20, minwidth=50, anchor=W)
        tree.column("col9", width=20, minwidth=50, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Supplier")
        tree.heading("col2", text="Supplier Num")
        tree.heading("col3", text="Phone Number")
        tree.heading("col4", text="Address")
        tree.heading("col5", text="Email")
        tree.heading("col6", text="City")
        tree.heading("col7", text="Zip code")
        tree.heading("col8", text="Bill Adress")
        tree.heading("col9", text="Fax")

        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_suppliers,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_suppliers, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_suppliers,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_suppliers(tree)
            )

        boton_1.grid(
            row=1,
            column=4
            )

        boton_2 = Button(
            ventana_emergente_suppliers,
            text="Modify supplier",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.fun_update_supplier(
                var_supplier,
                var_supplier_num,
                var_phone_number,
                var_address,
                var_email,
                var_city,
                var_zip_code,
                var_bill_address,
                var_fax,
                tree
            ),
        )

        boton_2.grid(
            row=2,
            column=4
            )
        boton_3 = Button(
            ventana_emergente_suppliers,
            text="Delete supplier",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.delete_supplier(
                var_id,
                tree
            ),
        )
        boton_3.grid(
            row=3,
            column=4
            )

        boton_4 = Button(
            ventana_emergente_suppliers,
            text="Save",
            padx=51,
            pady=1,
            command=lambda: self.crud_object.fun_new_supplier(
                var_supplier,
                var_supplier_num,
                var_phone_number,
                var_address,
                var_email,
                var_city,
                var_zip_code,
                var_bill_address,
                var_fax,
                tree
            ),
        )
        boton_4.grid(
            row=7,
            column=4
            )

    def v_sell_orders_new(self):
        ventana_emergente_sellsorders = Toplevel()
        ventana_emergente_sellsorders.title("New Sell Order")
        #delete_object = VistaApp()
        (
            var_id,
            var_client,
            var_client_num,
            var_invoice_num,
            var_invoice_date,
            var_import_type,
            var_subtotal,
            var_total
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            DateEntry(),
            StringVar(),
            DoubleVar(),
            DoubleVar()
        )

        titulo = Label(
            ventana_emergente_sellsorders,
            text="Client Name"
            )
        titulo.grid(
            row=2,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Client Num"
        )
        titulo.grid(
            row=2,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Invoice Num"
            )
        titulo.grid(
            row=3,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Invoice date"
            )
        titulo.grid(
            row=3,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Detail"
            )
        titulo.grid(
            row=4,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Sub Total"
            )
        titulo.grid(
            row=5,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Total"
            )
        titulo.grid(
            row=5,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_sellsorders,
            text="Import Type"
        )
        titulo.grid(
            row=4,
            column=2
        )
        entry_s = Entry(
            ventana_emergente_sellsorders,
            text=var_client,
            width=50
            )
        entry_s.grid(
            row=2,
            column=1
            )
        entry_t = Entry(
            ventana_emergente_sellsorders,
            text=var_client_num,
            width=50
            )
        entry_t.grid(
            row=2,
            column=3
            )
        entry_i = Entry(
            ventana_emergente_sellsorders,
            text=var_invoice_num,
            width=50
            )
        entry_i.grid(
            row=3,
            column=1
            )
        entry_o = DateEntry(
            ventana_emergente_sellsorders,
            text=var_invoice_date,
            width=25,
            background='darkblue',
            foreground='white',
            borderwidth=2
            )
        entry_o.grid(row=3, column=3)

        entry_subtotal = Entry(
            ventana_emergente_sellsorders,
            text=var_subtotal,
            width=50
            )
        entry_subtotal.grid(
            row=5,
            column=1
            )

        entry_total = Entry(
            ventana_emergente_sellsorders,
            text=var_total,
            width=50
            )
        entry_total.grid(
            row=5,
            column=3
            )
        entry_import_type = Entry(
            ventana_emergente_sellsorders,
            text=var_import_type,
            width=50
            )
        entry_import_type.grid(
            row=4,
            column=3
            )

        tree = ttk.Treeview(ventana_emergente_sellsorders)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Client")
        tree.heading("col2", text="Client Num")
        tree.heading("col3", text="Invoice Num")
        tree.heading("col4", text="Invoice Date")
        tree.heading("col5", text="Import Type")
        tree.heading("col6", text="Sub Total")
        tree.heading("col7", text="Total")
        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_sellsorders,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_sellsorders, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_sellsorders,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_sells_orders(tree)
            )

        boton_1.grid(
            row=1,
            column=4
            )

        boton_2 = Button(
            ventana_emergente_sellsorders,
            text="Modify order",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.fun_update_sell(
                var_client,
                var_client_num,
                var_invoice_num,
                var_invoice_date,
                var_import_type,
                var_subtotal,
                var_total,
                tree
            )
        )

        boton_2.grid(
            row=2,
            column=4
            )
        boton_3 = Button(
            ventana_emergente_sellsorders,
            text="Delete order",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.delete_sell_order(
                var_id,
                tree
            ),
        )
        boton_3.grid(
            row=3,
            column=4
            )

        boton_4 = Button(
            ventana_emergente_sellsorders,
            text="Save",
            padx=51,
            pady=1,
            command=lambda: self.crud_object.fun_new_sell(
                var_client,
                var_client_num,
                var_invoice_num,
                var_invoice_date,
                var_import_type,
                var_subtotal,
                var_total,
                tree
            ),
        )
        boton_4.grid(
            row=7,
            column=4
            )
        boton_5 = Button(
            ventana_emergente_sellsorders,
            text="Details",
            padx=51,
            pady=1,
            command=self.v_buys_details
        )
        boton_5.grid(
            row=4,
            column=1
            )

    def v_buys_orders_new(self):
        ventana_emergente_buy_orders_new = Toplevel()
        ventana_emergente_buy_orders_new.title("New Buy")
        (
            var_id,
            var_supplier,
            var_supplier_num,
            var_order_num,
            var_order_date,
            var_import_type,
            var_subtotal,
            var_total
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            DateEntry(),
            StringVar(),
            DoubleVar(),
            DoubleVar()
        )

        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Supplier Name"
            )
        titulo.grid(
            row=2,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Supplier Num"
            )
        titulo.grid(
            row=2,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Order Num"
            )
        titulo.grid(
            row=3,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Order date"
            )
        titulo.grid(
            row=3,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Detail"
            )
        titulo.grid(
            row=4,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Sub Total"
            )
        titulo.grid(
            row=5,
            column=0,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Total"
            )
        titulo.grid(
            row=5,
            column=2,
            sticky=W
            )
        titulo = Label(
            ventana_emergente_buy_orders_new,
            text="Import Type"
        )
        titulo.grid(
            row=4,
            column=2
        )
        entry_supplier = Entry(
            ventana_emergente_buy_orders_new,
            text=var_supplier,
            width=50
            )
        entry_supplier.grid(
            row=2,
            column=1
            )
        entry_l = Entry(
            ventana_emergente_buy_orders_new,
            text=var_supplier_num,
            width=50
            )
        entry_l.grid(
            row=2,
            column=3
            )
        entry_i = Entry(
            ventana_emergente_buy_orders_new,
            text=var_order_num,
            width=50
            )
        entry_i.grid(
            row=3,
            column=1
            )
        entry_o = DateEntry(
            ventana_emergente_buy_orders_new,
            text=var_order_date,
            width=25,
            background='darkblue',
            foreground='white',
            borderwidth=2
            )
        entry_o.grid(row=3, column=3)

        entry_import_type = Entry(
            ventana_emergente_buy_orders_new,
            text=var_import_type,
            width=50
            )
        entry_import_type.grid(
            row=4,
            column=3
            )

        entry_subtotal = Entry(
            ventana_emergente_buy_orders_new,
            text=var_subtotal,
            width=50
            )
        entry_subtotal.grid(
            row=5,
            column=1
            )

        entry_total = Entry(
            ventana_emergente_buy_orders_new,
            text=var_total,
            width=50
            )
        entry_total.grid(
            row=5,
            column=3
            )

        tree = ttk.Treeview(ventana_emergente_buy_orders_new)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Client")
        tree.heading("col2", text="Client Num")
        tree.heading("col3", text="Order Num")
        tree.heading("col4", text="Order Date")
        tree.heading("col5", text="Import Type")
        tree.heading("col6", text="Sub Total")
        tree.heading("col7", text="Total")
        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_buy_orders_new,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_buy_orders_new, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_buy_orders_new,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_buys_orders(tree)
            )

        boton_1.grid(
            row=1,
            column=4
            )

        boton_2 = Button(
            ventana_emergente_buy_orders_new,
            text="Modify order",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.fun_update_buy(
                var_supplier,
                var_supplier_num,
                var_order_num,
                var_order_date,
                var_import_type,
                var_subtotal,
                var_total,
                tree
            )
        )

        boton_2.grid(
            row=2,
            column=4
            )
        boton_3 = Button(
            ventana_emergente_buy_orders_new,
            text="Delete order",
            padx=100,
            pady=1,
            command=lambda: self.crud_object.delete_buy_order(
                var_id,
                tree
            ),
        )
        boton_3.grid(
            row=3,
            column=4
            )

        boton_4 = Button(
            ventana_emergente_buy_orders_new,
            text="Save",
            padx=51,
            pady=1,
            command=lambda: self.crud_object.fun_new_buy(
                var_supplier,
                var_supplier_num,
                var_order_num,
                var_order_date,
                var_import_type,
                var_subtotal,
                var_total,
                tree
            ),
        )
        boton_4.grid(
            row=7,
            column=4
            )
        boton_5 = Button(
            ventana_emergente_buy_orders_new,
            text="Details",
            padx=51,
            pady=1,
            command=self.v_buys_details
        )
        boton_5.grid(
            row=4,
            column=1
            )

    def v_buys_orders(self):
        ventana_emergente_a = Toplevel()
        ventana_emergente_a.title("Buy Orders")

        tree = ttk.Treeview(ventana_emergente_a)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.column("col8", width=30, minwidth=120, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Supplier")
        tree.heading("col2", text="Supplier Num")
        tree.heading("col3", text="Order num")
        tree.heading("col4", text="Order date")
        tree.heading("col5", text="Import Type")
        tree.heading("col6", text="Sub Total")
        tree.heading("col7", text="Total")
        tree.heading("col8", text="Registration Date")
        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_a,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_a, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_a,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_buys_orders(tree))

        boton_1.grid(
            row=1,
            column=1
            )

    def v_sell_orders(self):
        ventana_emergente_o = Toplevel()
        ventana_emergente_o.title("Sell Orders")

        tree = ttk.Treeview(ventana_emergente_o)
        tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
            "col8",
        )

        tree.column("#0", width=20, minwidth=50, anchor=W)
        tree.column("col1", width=90, minwidth=100, anchor=W)
        tree.column("col2", width=90, minwidth=100, anchor=W)
        tree.column("col3", width=80, minwidth=80, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=80, minwidth=100, anchor=W)
        tree.column("col6", width=100, minwidth=100, anchor=W)
        tree.column("col7", width=20, minwidth=50, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Client")
        tree.heading("col2", text="Client Num")
        tree.heading("col3", text="Invoice Num")
        tree.heading("col4", text="Invoice Date")
        tree.heading("col5", text="Import Type")
        tree.heading("col6", text="Sub Total")
        tree.heading("col7", text="Total")
        tree.grid(column=0, row=12, columnspan=5)
        scrollbar_v = ttk.Scrollbar(
            ventana_emergente_o,
            orient=VERTICAL,
            command=tree.yview
            )
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            ventana_emergente_o, orient=HORIZONTAL, command=tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        tree.configure(xscrollcommand=scrollbar_h.set)

        boton_1 = Button(
            ventana_emergente_o,
            text="Refresh",
            padx=100,
            pady=1,
            command=self.crud_object.fun_consult_sells_orders(tree))

        boton_1.grid(
            row=1,
            column=1
            )
# #########################################WORK IN PROGRESS##################

    def v_buys_details(self):
        v_buy_details = Toplevel()
        v_buy_details.title("Buy Details")
        (
            var_product_1,
            var_quantity_1,
            var_product_2,
            var_quantity_2,
            var_product_3,
            var_quantity_3,
            var_product_4,
            var_quantity_4,
            var_product_5,
            var_quantity_5
            ) = (
            StringVar(),
            IntVar(),
            StringVar(),
            IntVar(),
            StringVar(),
            IntVar(),
            StringVar(),
            IntVar(),
            StringVar(),
            IntVar()
        )
        titulo = Label(
            v_buy_details,
            text="Product 1"
            )
        titulo.grid(
            row=1,
            column=0,
            sticky=W)
        titulo = Label(
            v_buy_details,
            text="Product 2"
            )
        titulo.grid(
            row=2,
            column=0,
            sticky=W
            )
        titulo = Label(
            v_buy_details,
            text="Product 3"
            )
        titulo.grid(
            row=3,
            column=0,
            sticky=W)
        titulo = Label(
            v_buy_details,
            text="Product 4"
            )
        titulo.grid(
            row=4,
            column=0,
            sticky=W)

        titulo = Label(
            v_buy_details,
            text="Product 5"
            )
        titulo.grid(
            row=5,
            column=0,
            sticky=W)

        entry_product_1 = Entry(
            v_buy_details,
            text=var_product_1,
            width=50
            )
        entry_product_1.grid(
            row=1,
            column=1
            )
        entry_quantity_1 = Entry(
            v_buy_details,
            text=var_quantity_1,
            width=50
            )
        entry_quantity_1.grid(
            row=1,
            column=2
            )
        entry_product_2 = Entry(
            v_buy_details,
            text=var_product_2,
            width=50
            )
        entry_product_2.grid(
            row=2,
            column=1
            )
        entry_quantity_2 = Entry(
            v_buy_details,
            text=var_quantity_2,
            width=50)
        entry_quantity_2.grid(
            row=2,
            column=2
            )
        entry_product_3 = Entry(
            v_buy_details,
            text=var_product_3,
            width=50
            )
        entry_product_3.grid(
            row=3,
            column=1
            )
        entr_quantity_3 = Entry(
            v_buy_details,
            text=var_quantity_3,
            width=50
            )
        entr_quantity_3.grid(
            row=3,
            column=2
            )
        entry_product_4 = Entry(
            v_buy_details,
            text=var_product_4,
            width=50
            )
        entry_product_4.grid(
            row=4,
            column=1
            )
        entry_quantity_4 = Entry(
            v_buy_details,
            text=var_quantity_4,
            width=50
            )
        entry_quantity_4.grid(
            row=4,
            column=2
            )
        entry_product_5 = Entry(
            v_buy_details,
            text=var_product_5,
            width=50
            )
        entry_product_5.grid(
            row=5,
            column=1
            )
        entry_quantity_5 = Entry(
            v_buy_details,
            text=var_quantity_5,
            width=50
            )
        entry_quantity_5.grid(
            row=5,
            column=2
            )

        boton_7 = Button(
            v_buy_details,
            text="Add order",
            padx=51,
            pady=1,
            command=lambda: funcion_calculo_caida_tension_monofasica(
                var_product_1,
                var_quantity_1,
                var_product_2,
                var_quantity_2,
                var_product_3,
                var_quantity_3,
                var_product_4,
                var_quantity_4,
                var_product_5,
                var_quantity_5
                ),
        )
        boton_7.grid(
            row=6,
            column=1
            )
