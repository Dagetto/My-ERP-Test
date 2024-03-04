from tkinter import *
from tkinter import messagebox
from peewee import *
from peewee import MySQLDatabase
from peewee import Model
from peewee import CharField
from peewee import DateField
from peewee import IntegerField
from datetime import datetime
import traceback
import os
import configparser


def get_database_credentials(filename='config.ini'):
    """
    Read the credential from the script config.ini
    """
    config = configparser.ConfigParser()
    config.read(filename)

    db_name = config['MySQLDatabase']['db_name']
    user = config['MySQLDatabase']['user']
    password = config['MySQLDatabase']['password']
    host = config['MySQLDatabase']['host']

    return db_name, user, password, host


def connect_to_database():
    """
    Conecta a la base de datos utilizando las credenciales del archivo config.ini
    """
    db_name, user, password, host = get_database_credentials()
    database = MySQLDatabase(db_name, user=user, password=password, host=host)
    return database


db = connect_to_database()


class BaseModel(Model):
    """Peewee class use to defines type  of data and metadata
    """
    class Meta:
        database = db


class Clients(BaseModel):
    """Creation of the table 'Clients'

    Args:
        BaseModel: Use the type of data defined on the class BaseModel
    """
    client = CharField()
    client_num = CharField(unique=True)
    phone_number = CharField()
    address = CharField()  # type of data used by peewee
    email = CharField()
    city = CharField()
    zip_code = CharField()
    bill_address = CharField()
    fax = CharField()


class Suppliers(BaseModel):
    supplier = CharField()
    supplier_num = CharField(unique=True)
    phone_number = CharField()
    address = CharField()
    email = CharField()
    city = CharField()
    zip_code = CharField()
    bill_address = CharField()
    fax = CharField()


class BuyOrders(BaseModel):
    supplier = CharField()
    supplier_num = CharField()
    order_num = CharField(unique=True)
    order_date = CharField()
    import_type = CharField()
    subtotal = IntegerField()
    total = IntegerField()


class SellsOrders(BaseModel):
    client = CharField()
    client_num = CharField()
    invoice_num = CharField(unique=True)
    invoice_date = CharField()
    import_type = CharField()
    subtotal = IntegerField()
    total = IntegerField()


db.connect()
db.create_tables([Clients])
db.create_tables([Suppliers])
db.create_tables([BuyOrders])
db.create_tables([SellsOrders])
######################################################################################################################


class CRUD():
    """Class 'CRUD' with all methods needed to make a CRUD operation on the
        tables.
    """
    def __init__(
        self,
    ):

        print('Inside CRUD class')

    def fun_new_sell(
        self,
        client,
        client_num,
        invoice_num,
        invoice_date,
        import_type,
        subtotal,
        total,
        tree
    ):
        sellorders = SellsOrders()

        try:
            sellorders.client = client.get()
            sellorders.client_num = client_num.get()
            sellorders.invoice_num = invoice_num.get()
            sellorders.invoice_date = invoice_date.get()
            sellorders.import_type = import_type.get()
            sellorders.subtotal = subtotal.get()
            sellorders.total = total.get()

            sellorders.save()
            print('sell saved')
            client.set("")
            client_num.set("")
            invoice_num.set("")
            import_type.set("")
            subtotal.set("")
            total.set("")
            self.fun_consult_sells_orders(tree)
            messagebox.showinfo(
                "New sell saved",
                "New sell saved.",
            )
        except Exception as e:
            error_description = traceback.format_exc()
            print(error_description)
            raise e

    def delete_sell_order(self, var_id, tree):
        sell_select = tree.focus()
        sell_id = tree.item(sell_select)
        delet_sell = SellsOrders.get(SellsOrders.id == sell_id["text"])
        delet_sell.delete_instance()
        self.fun_consult_sells_orders(tree)
        messagebox.showinfo(
            "Sell removed",
            "Sell removed.",
            )

    def fun_update_sell(
        self,
        client,
        client_num,
        invoice_num,
        invoice_date,
        import_type,
        subtotal,
        total,
        tree
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = SellsOrders.update(
            client=client.get(),
            client_num=client_num.get(),
            invoice_num=invoice_num.get(),
            invoice_date=invoice_date.get(),
            import_type=import_type.get(),
            subtotal=subtotal.get(),
            total=total.get(),
        ).where(
            SellsOrders.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.fun_consult_sells_orders(tree)
        messagebox.showinfo(
            "Sell modify",
            "The invoice has been modified.",
            )
        client.set("")
        client_num.set("")
        invoice_num.set("")
        import_type.set("")
        subtotal.set("")
        total.set("")

    def fun_consult_sells_orders(self, tree):
        registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (
            fila
        ) in SellsOrders.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.client,
                    fila.client_num,
                    fila.invoice_num,
                    fila.invoice_date,
                    fila.import_type,
                    fila.subtotal,
                    fila.total,
                ),
            )

    def fun_new_buy(
        self,
        supplier,
        supplier_num,
        order_num,
        order_date,
        import_type,
        subtotal,
        total,
        tree
    ):

        buyorders = BuyOrders()

        try:
            buyorders.supplier = supplier.get()
            buyorders.supplier_num = supplier_num.get()
            buyorders.order_num = order_num.get()
            buyorders.order_date = order_date.get()
            buyorders.import_type = import_type.get()
            buyorders.subtotal = subtotal.get()
            buyorders.total = total.get()

            buyorders.save()
            print('buy saved')
            self.fun_consult_buys_orders(tree)
            messagebox.showinfo(
                "New buy",
                "New buy saved.",
            )
            supplier.set("")
            supplier_num.set("")
            order_num.set("")
            import_type.set("")
            subtotal.set("")
            total.set("")
        except Exception as e:
            error_description = traceback.format_exc()
            print(error_description)
            raise e

    def delete_buy_order(self, var_id, tree):
        sell_select = tree.focus()
        sell_id = tree.item(sell_select)
        delet_sell = BuyOrders.get(BuyOrders.id == sell_id["text"])
        delet_sell.delete_instance()
        self.fun_consult_buys_orders(tree)
        messagebox.showinfo(
            "Delete order",
            "The order has been removed",
        )

    def fun_consult_buys_orders(self, tree):
        registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (
            fila
        ) in BuyOrders.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.supplier,
                    fila.supplier_num,
                    fila.order_num,
                    fila.order_date,
                    fila.import_type,
                    fila.subtotal,
                    fila.total,
                ),
            )

    def fun_update_buy(
        self,
        supplier,
        supplier_num,
        order_num,
        order_date,
        import_type,
        subtotal,
        total,
        tree
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = BuyOrders.update(
            supplier=supplier.get(),
            supplier_num=supplier_num.get(),
            order_num=order_num.get(),
            order_date=order_date.get(),
            import_type=import_type.get(),
            subtotal=subtotal.get(),
            total=total.get(),
        ).where(
            BuyOrders.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.fun_consult_buys_orders(tree)
        messagebox.showinfo(
            "Modify order",
            "The order has been modified",
        )
        supplier.set("")
        supplier_num.set("")
        order_num.set("")
        import_type.set("")
        subtotal.set("")
        total.set("")

    def fun_new_client(
        self,
        client,
        client_num,
        phone_number,
        address,
        email,
        city,
        zip_code,
        bill_address,
        fax,
        tree
    ):

        clients = Clients()

        try:
            clients.client = client.get()
            clients.client_num = client_num.get()
            clients.phone_number = phone_number.get()
            clients.address = address.get()
            clients.email = email.get()
            clients.city = city.get()
            clients.zip_code = zip_code.get()
            clients.bill_address = bill_address.get()
            clients.fax = fax.get()

            clients.save()
            print('client saved')
            self.fun_consult_clients(tree)
            messagebox.showinfo(
                "New client",
                "The client has been added",
            )
            client.set("")
            client_num.set("")
            phone_number.set("")
            address.set("")
            email.set("")
            city.set("")
            zip_code.set("")
            bill_address.set("")
            fax.set("")
        except Exception as e:
            error_description = traceback.format_exc()
            print(error_description)
            raise e

    def delete_client(self, var_id, tree):
        client_select = tree.focus()
        client_id = tree.item(client_select)
        delet_client = Clients.get(Clients.id == client_id["text"])
        delet_client.delete_instance()
        self.fun_consult_clients(tree)
        messagebox.showinfo(
            "Remove client",
            "The client has been removed",
        )

    def fun_update_client(
        self,
        client,
        client_num,
        phone_number,
        address,
        email,
        city,
        zip_code,
        bill_address,
        fax,
        tree
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = Clients.update(
            client=client.get(),
            client_num=client_num.get(),
            phone_number=phone_number.get(),
            address=address.get(),
            email=email.get(),
            city=city.get(),
            zip_code=zip_code.get(),
            bill_address=bill_address.get(),
            fax=fax.get(),
        ).where(
            Clients.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.fun_consult_clients(tree)
        messagebox.showinfo(
            "Modify client",
            "The client has been modified",
            )
        client.set("")
        client_num.set("")
        phone_number.set("")
        address.set("")
        email.set("")
        city.set("")
        zip_code.set("")
        bill_address.set("")
        fax.set("")

    def fun_consult_clients(self, tree):
        registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (
            fila
        ) in Clients.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.client,
                    fila.client_num,
                    fila.phone_number,
                    fila.address,
                    fila.email,
                    fila.city,
                    fila.zip_code,
                    fila.bill_address,
                    fila.fax,
                ),
            )

    def fun_new_supplier(
        self,
        supplier,
        supplier_num,
        phone_number,
        address,
        email,
        city,
        zip_code,
        bill_address,
        fax,
        tree
    ):

        suppliers = Suppliers()

        try:
            suppliers.supplier = supplier.get()
            suppliers.supplier_num = supplier_num.get()
            suppliers.phone_number = phone_number.get()
            suppliers.address = address.get()
            suppliers.email = email.get()
            suppliers.city = city.get()
            suppliers.zip_code = zip_code.get()
            suppliers.bill_address = bill_address.get()
            suppliers.fax = fax.get()
            suppliers.save()
            print('supplier saved')
            self.fun_consult_suppliers(tree)
            messagebox.showinfo(
                "New supplier",
                "The supplier has been added",
            )
            supplier.set("")
            supplier_num.set("")
            phone_number.set("")
            address.set("")
            email.set("")
            city.set("")
            zip_code.set("")
            bill_address.set("")
            fax.set("")
        except Exception as e:
            error_description = traceback.format_exc()
            print(error_description)
            raise e

    def delete_supplier(self, var_id, tree):
        supplier_select = tree.focus()
        supplier_id = tree.item(supplier_select)
        delet_supplier = Suppliers.get(Suppliers.id == supplier_id["text"])
        delet_supplier.delete_instance()
        self.fun_consult_suppliers(tree)
        messagebox.showinfo(
            "Delete supplier",
            "The supplier has been removed",
            )

    def fun_update_supplier(
        self,
        supplier,
        supplier_num,
        phone_number,
        address,
        email,
        city,
        zip_code,
        bill_address,
        fax,
        tree
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = Suppliers.update(
            supplier=supplier.get(),
            supplier_num=supplier_num.get(),
            phone_number=phone_number.get(),
            address=address.get(),
            email=email.get(),
            city=city.get(),
            zip_code=zip_code.get(),
            bill_address=bill_address.get(),
            fax=fax.get(),
        ).where(
            Suppliers.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.fun_consult_suppliers(tree)
        messagebox.showinfo(
            "Modify supplier",
            "The supplier has been modified",
            )
        supplier.set("")
        supplier_num.set("")
        phone_number.set("")
        address.set("")
        email.set("")
        city.set("")
        zip_code.set("")
        bill_address.set("")
        fax.set("")

    def fun_consult_suppliers(self, tree):
        registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (
            fila
        ) in Suppliers.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.supplier,
                    fila.supplier_num,
                    fila.phone_number,
                    fila.address,
                    fila.email,
                    fila.city,
                    fila.zip_code,
                    fila.bill_address,
                    fila.fax,
                ),
            )