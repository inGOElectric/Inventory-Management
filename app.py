from flask import Flask, render_template, url_for, request, redirect, jsonify,make_response,send_file,Response
from collections import defaultdict
import numpy as np
from datetime import datetime
from sqlalchemy import func
from flask import send_file, session
import io
import zipfile
import sqlite3
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask import session
import io
from sqlalchemy import event
from sqlalchemy import literal_column
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)
import datetime
import pytz
import json
ist = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(ist)
formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
datetime_now = datetime.datetime.strptime(formatted_now, '%Y-%m-%d %H:%M:%S')
class Product(db.Model):
    __tablename__ = 'products'
    productId = db.Column(db.String(200), primary_key=True)
    part_id = db.Column(db.Integer)
    area = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime_now)

    def __repr__(self):
        return '<Product %r>' % self.productId
class DeletedProduct(db.Model):
    _tablename_ = 'deleted_products'
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.String(200))
    part_id = db.Column(db.Integer)
    area = db.Column(db.Integer)
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedProduct %r>' % self.productId
@event.listens_for(Product, 'after_delete')
def backup_deleted_product(mapper, connection, target):
    deleted_product = DeletedProduct(productId=target.productId,
                                     part_id=target.part_id,
                                     area=target.area)
    connection.execute(DeletedProduct.__table__.insert(), deleted_product.__dict__)

class Vendor(db.Model):
    __tablename__ = 'vendor'
    vendor_id = db.Column(db.String(200), primary_key=True)
    vendor_address = db.Column(db.Integer)
    vendor_phn = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime_now)

    def __repr__(self):
        return '<Vendor %r>' % self.vendor_id
class DeletedVendor(db.Model):
    _tablename_ = 'deleted_vendors'
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.String(200))
    vendor_address = db.Column(db.Integer)
    vendor_phn = db.Column(db.Integer)
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedVendor %r>' % self.vendor_id
@event.listens_for(Vendor, 'after_delete')
def backup_deleted_vendor(mapper, connection, target):
    deleted_vendor = DeletedVendor(vendor_id=target.vendor_id,
                                     vendor_address=target.vendor_address,
                                     vendor_phn=target.vendor_phn)
    connection.execute(DeletedVendor.__table__.insert(), deleted_vendor.__dict__)
class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.String(200), primary_key=True)
    location_area = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime_now)

    def __repr__(self):
        return '<Location %r>' % self.location_id
class DeletedLocation(db.Model):
    _tablename_ = 'deleted_locations'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(200))
    location_area = db.Column(db.Integer)
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedLocation %r>' % self.location_id
@event.listens_for(Location, 'after_delete')
def backup_deleted_location(mapper, connection, target):
    deleted_location = DeletedLocation(location_id=target.location_id,
                                     location_area=target.location_area,
                                     )
    connection.execute(DeletedLocation.__table__.insert(), deleted_location.__dict__)
class Sales(db.Model):
    __tablename__ = 'sales'
    sales_id = db.Column(db.String(200), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime_now)

    def __repr__(self):
        return '<Sales %r>' % self.sales_id
class Person(db.Model):
    __tablename__ = 'operationperson'
    operationperson_id = db.Column(db.String(200), primary_key=True)
    operationperson_phn = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime_now)

    def __repr__(self):
        return '<Person %r>' % self.operationperson_id
class DeletedPerson(db.Model):
    _tablename_ = 'deleted_operationsperson'
    id = db.Column(db.Integer, primary_key=True)
    operationperson_id = db.Column(db.String(200))
    operationperson_phn = db.Column(db.Integer)
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedPerson %r>' % self.operationperson_id
@event.listens_for(Person, 'after_delete')
def backup_deleted_person(mapper, connection, target):
    deleted_person = DeletedPerson(operationperson_id=target.operationperson_id,
                                     operationperson_phn=target.operationperson_phn,
                                     )
    connection.execute(DeletedPerson.__table__.insert(), deleted_person.__dict__)
class Inwarding(db.Model):
    __tablename__ = 'inwardings'
    inwarding_id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('products.part_id'))
    area = db.Column(db.Integer, db.ForeignKey('products.area'))
    cost = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    quantity1 = db.Column(db.Integer,default=0)
    remaining_area = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    vendor_address = db.Column(db.Integer, db.ForeignKey('vendor.vendor_address'))
    vendor_phn = db.Column(db.Integer, db.ForeignKey('vendor.vendor_phn'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    location_area = db.Column(db.Integer, db.ForeignKey('location.location_area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('operationperson.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey('operationperson.operationperson_phn'))
    inwarding_time= db.Column(db.DateTime, default=datetime_now)
    product = db.relationship('Product',  backref='inwarding',foreign_keys=[productId])
    part = db.relationship('Product', foreign_keys=part_id)
    area1 = db.relationship('Product', foreign_keys=area)
    vendorid = db.relationship("Vendor", foreign_keys=vendor_id)
    vendorphn = db.relationship("Vendor", foreign_keys=vendor_phn)
    vendoraddress = db.relationship("Vendor", foreign_keys=vendor_address)
    location = db.relationship("Location", foreign_keys=location_id)
    larea = db.relationship("Location", foreign_keys=location_area)
    operationperson = db.relationship("Person", foreign_keys=operationperson_id)
    operationpersonphn = db.relationship("Person", foreign_keys=operationperson_phn)
    type = db.Column(db.String(50), nullable=False, default="inward") # Added default value
    def __repr__(self):
        return '<Inwarding %r>' % self.inwarding_id
class DeletedInwarding(db.Model):
    _tablename_ = 'deleted_inwarding'
    id = db.Column(db.Integer, primary_key=True)
    inwarding_id = db.Column(db.Integer)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('products.part_id'))
    area = db.Column(db.Integer, db.ForeignKey('products.area'))
    cost = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    quantity1 = db.Column(db.Integer, default=0)
    remaining_area = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    vendor_address = db.Column(db.Integer, db.ForeignKey('vendor.vendor_address'))
    vendor_phn = db.Column(db.Integer, db.ForeignKey('vendor.vendor_phn'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    location_area = db.Column(db.Integer, db.ForeignKey('location.location_area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('operationperson.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey('operationperson.operationperson_phn'))
    inwarding_time = db.Column(db.DateTime, default=datetime_now)
    type = db.Column(db.String(50), nullable=False, default="inward")  # Added default value
    def _repr_(self):
        return '<DeletedPerson %r>' % self.operationperson_id
@event.listens_for(Inwarding, 'after_delete')
def backup_deleted_inwarding(mapper, connection, target):
    deleted_inwarding = DeletedInwarding(inwarding_id=target.inwarding_id,
                                     productId=target.productId,
                                         part_id=target.part_id,
                                         area =target.area,
                                         cost=target.cost,
                                         quantity=target.quantity,
                                         remaining_area=target.remaining_area,
                                         vendor_id=target.vendor_id,
                                         vendor_address=target.vendor_address,
                                         vendor_phn=target.vendor_phn,
                                         location_id=target.location_id,
                                         location_area=target.location_area,
                                         operationperson_id=target.operationperson_id,
                                         operationperson_phn=target.operationperson_phn,
                                         inwarding_time=target.inwarding_time,
                                         type=target.type
                                     )
    connection.execute(DeletedInwarding.__table__.insert(), deleted_inwarding.__dict__)
class ProductMovement(db.Model):
    __tablename__ = 'productmovements'
    movement_id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('inwardings.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('inwardings.part_id'))
    area  =db.Column(db.Integer,db.ForeignKey('inwardings.area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('inwardings.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey("inwardings.operationperson_phn"))
    quantity = db.Column(db.Integer)
    from_location = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    to_location = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    movement_time = db.Column(db.DateTime, default=datetime_now)
    product = db.relationship('Inwarding', foreign_keys=productId)
    larea= db.relationship('Inwarding', foreign_keys=area)
    fromLoc = db.relationship('Location', foreign_keys=from_location)
    toLoc = db.relationship('Location', foreign_keys=to_location)
    operationpersonid = db.relationship('Inwarding', foreign_keys=operationperson_id)
    operationpersonphn = db.relationship('Inwarding', foreign_keys=operationperson_phn)
    type = db.Column(db.String(50), nullable=False, default="movements")
    def __repr__(self):
        return '<ProductMovement %r>' % self.movement_id
class DeletedMovement(db.Model):
    __tablename__ = 'deleted_movements'
    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer)
    productId = db.Column(db.Integer, db.ForeignKey('inwardings.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('inwardings.part_id'))
    area = db.Column(db.Integer, db.ForeignKey('inwardings.area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('inwardings.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey("inwardings.operationperson_phn"))
    quantity = db.Column(db.Integer)
    from_location = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    to_location = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    type = db.Column(db.String(50), nullable=False, default="movements")
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedMovement %r>' % self.movement_id
@event.listens_for(ProductMovement,'after_delete')
def backup_deleted_movement(mapper, connection, target):
    deleted_movement = DeletedMovement(movement_id=target.movement_id,
                                     productId=target.productId,
                                       part_id=target.part_id,
                                       area=target.area,
                                       operationperson_id=target.operationperson_id,
                                       operationperson_phn=target.operationperson_phn,
                                       quantity=target.quantity,
                                       from_location=target.from_location,
                                       to_location=target.to_location,
                                       type=target.type
                                       )
    connection.execute(DeletedMovement.__table__.insert(), deleted_movement.__dict__)
class Outwarding(db.Model):
    __tablename__ = 'outwards'
    outward_id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('productmovements.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('productmovements.part_id'))
    area  =db.Column(db.Integer,db.ForeignKey('productmovements.area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('productmovements.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey("productmovements.operationperson_phn"))
    quantity = db.Column(db.Integer)
    to_location = db.Column(db.Integer, db.ForeignKey('productmovements.to_location'))
    sales_id =db.Column(db.Integer, db.ForeignKey('sales.sales_id'))
    outward_time = db.Column(db.DateTime, default=datetime_now)
    product = db.relationship('ProductMovement', foreign_keys=productId)
    larea= db.relationship('ProductMovement', foreign_keys=area)
    toLoc = db.relationship('ProductMovement', foreign_keys=to_location)
    operationpersonid = db.relationship('ProductMovement', foreign_keys=operationperson_id)
    operationpersonphn = db.relationship('ProductMovement', foreign_keys=operationperson_phn)
    sale= db.relationship('Sales', foreign_keys=sales_id)
    type = db.Column(db.String(50), nullable=False, default="outwardings")
    def __repr__(self):
        return '<Outwarding %r>' % self.outward_id
class DeletedOutwarding(db.Model):
    _tablename_ = 'deleted_outwarding'
    id = db.Column(db.Integer, primary_key=True)
    outward_id = db.Column(db.Integer)
    productId = db.Column(db.Integer, db.ForeignKey('productmovements.productId'))
    part_id = db.Column(db.Integer, db.ForeignKey('productmovements.part_id'))
    area = db.Column(db.Integer, db.ForeignKey('productmovements.area'))
    operationperson_id = db.Column(db.Integer, db.ForeignKey('productmovements.operationperson_id'))
    operationperson_phn = db.Column(db.Integer, db.ForeignKey("productmovements.operationperson_phn"))
    quantity = db.Column(db.Integer)
    to_location = db.Column(db.Integer, db.ForeignKey('productmovements.to_location'))
    type = db.Column(db.String(50), nullable=False, default="outwardings")
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.sales_id'))
    deleted_date = db.Column(db.DateTime, default=datetime_now)
    def _repr_(self):
        return '<DeletedOutwarding %r>' % self.outward_id
@event.listens_for(Outwarding, 'after_delete')
def backup_deleted_outwarding(mapper, connection, target):
    deleted_outward = DeletedOutwarding(outward_id=target.outward_id,
                                     productId=target.productId,
                                        part_id=target.part_id,
                                        area =target.area,
                                        operationperson_id=target.operationperson_id,
                                        operationperson_phn=target.operationperson_phn,
                                        quantity=target.quantity,
                                        to_location=target.to_location,
                                        type = target.type

    )
    connection.execute(DeletedOutwarding.__table__.insert(), deleted_outward.__dict__)
@app.route("/Summary/",methods=['GET','POST'])
def summary():
    start_date =request.form.get("start_date")
    end_date = request.form.get("end_date")
    inwards = Inwarding.query \
        .join(Product, Inwarding.productId == Product.productId) \
        .add_columns(
        Inwarding.type,
        Inwarding.productId,
        Inwarding.part_id,
        Inwarding.quantity,
        Inwarding.location_id,
        Inwarding.operationperson_id,
        Inwarding.operationperson_phn,
        Inwarding.inwarding_time,
    ) \
        .group_by(Inwarding.inwarding_id) \
        .all()
    data = [('Type', 'Part', 'Id', 'Quantity', 'to_location',
             'Person', 'Contact', 'Date',
             )] + [row[1:] for row in inwards]
    df = pd.DataFrame(data[1:], columns=data[0])
    print(df)
    df.fillna(0,inplace=True)
    movements = ProductMovement.query \
        .join(Inwarding, ProductMovement.productId == Inwarding.productId) \
        .add_columns(
        ProductMovement.type,
        ProductMovement.productId,
        ProductMovement.part_id,
        ProductMovement.quantity,
        ProductMovement.from_location,
        ProductMovement.to_location,
        ProductMovement.operationperson_id,
        ProductMovement.operationperson_phn,
        ProductMovement.movement_time
    ) \
        .group_by(ProductMovement.movement_id)\
        .all()
    data1 = [('Type', 'Part', 'Id', 'Quantity', "from_location",'to_location',
             'Person', 'Contact', 'Date',
             )] + [row[1:] for row in movements]
    df1 = pd.DataFrame(data1[1:], columns=data1[0])
    Outwards = Outwarding.query \
        .join(ProductMovement, Outwarding.productId == ProductMovement.productId) \
        .add_columns(
        Outwarding.type,
        Outwarding.productId,
        Outwarding.part_id,
        Outwarding.quantity,
        Outwarding.to_location,
        Outwarding.sales_id,
        Outwarding.operationperson_id,
        Outwarding.operationperson_phn,
        Outwarding.outward_time) \
        .group_by(Outwarding.outward_id) \
 \
    .all()
    inwards = Inwarding.query \
        .join(Product, Inwarding.productId == Product.productId) \
        .add_columns(
        Inwarding.inwarding_id,
        Inwarding.productId,
        Inwarding.part_id,
        Inwarding.cost,
        Inwarding.area,
        Inwarding.quantity,
        Inwarding.location_id,
        Inwarding.location_area,
        Inwarding.operationperson_id,
        Inwarding.operationperson_phn,
        Inwarding.vendor_id,
        Inwarding.vendor_address,
        Inwarding.vendor_phn,
        (Inwarding.cost * Inwarding.quantity).label('Tcost'),
        (Inwarding.area * Inwarding.quantity).label('Tarea'),
        Inwarding.inwarding_time,
        Inwarding.type,
    ) \
        .group_by(Inwarding.inwarding_id) \
        .all()

    # Compute total cost
    total_cost = sum(inward.Tcost for inward in inwards)
    data2 = [('Type', 'Part', 'Id', 'Quantity', "from_location", 'to_location',
              'Person', 'Contact', 'Date',
              )] + [row[1:] for row in Outwards]
    df2 = pd.DataFrame(data2[1:], columns=data2[0])
    merged_df = pd.concat([df1,df], axis=0)
    merged_df.fillna(0, inplace=True)
    merged_df['Date'] = pd.to_datetime(merged_df['Date']).dt.strftime('%Y-%m-%d')
    if start_date and end_date:
        merged_df = merged_df[(merged_df['Date'] >= start_date) & (merged_df['Date'] <= end_date)]
    merged_df.reset_index(drop=True, inplace=True)
    session['merged_df'] = merged_df.to_json()# reset the index to make it unique
    grouped = merged_df.groupby('to_location')
    print(merged_df)
    conn = sqlite3.connect('inventory.db')
    merged_df.to_sql('summary', conn, if_exists='replace', index=True)
    conn.close()
    tables = {}
    for name, group in grouped:
        tables[name] = group.to_html(index=False)
    print(tables[name])
    return render_template('table.html', tables=tables, merged_df=merged_df,total_cost=total_cost)
@app.route('/download_csv')
def download_csv():
    output = io.StringIO()
    df_json = session['merged_df']
    merged_df = pd.read_json(df_json)
    if 'start_date' in session and 'end_date' in session:
        start_date = session['start_date']
        end_date = session['end_date']
        merged_df = merged_df[(merged_df['Date'] >= start_date) & (merged_df['Date'] <= end_date)]
    grouped = merged_df.groupby('to_location')
    tables = {}
    for name, group in grouped:
        tables[name] = group.to_csv(index=False)
    zip_output = io.BytesIO()
    with zipfile.ZipFile(zip_output, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for name, csv_string in tables.items():
            zf.writestr(name + '.csv', csv_string)
    zip_output.seek(0)
    return send_file(zip_output, mimetype='application/zip', as_attachment=True, attachment_filename='data.zip')
@app.route("/",methods=['GET','POST'])
def table():
    start_date =request.form.get("start_date")
    end_date = request.form.get("end_date")
    inwards = Inwarding.query \
        .join(Product, Inwarding.productId == Product.productId) \
        .add_columns(
        Inwarding.type,
        Inwarding.productId,
        Inwarding.part_id,
        Inwarding.area,
        Inwarding.quantity,
        Inwarding.quantity1,
        Inwarding.location_id,
        Inwarding.operationperson_id,
        Inwarding.operationperson_phn,
        Inwarding.inwarding_time,
    ) \
        .group_by(Inwarding.inwarding_id) \
        .all()
    data = [('Type', 'Part', 'Id','Area', 'Quantity','Quantity1','to_location',
             'Person', 'Contact', 'Date',
             )] + [row[1:] for row in inwards]
    df = pd.DataFrame(data[1:], columns=data[0])
    df.fillna(0,inplace=True)
    print(df.to_string())
    movements = ProductMovement.query \
        .join(Inwarding, ProductMovement.productId == Inwarding.productId) \
        .add_columns(
        ProductMovement.type,
        ProductMovement.productId,
        ProductMovement.part_id,
        ProductMovement.area,
        ProductMovement.quantity,
        ProductMovement.from_location,
        ProductMovement.to_location,
        ProductMovement.operationperson_id,
        ProductMovement.operationperson_phn,
        ProductMovement.movement_time
    ) \
        .group_by(ProductMovement.movement_id)\
        .all()
    data1 = [('Type', 'Part', 'Id','Area', 'Quantity', "from_location",'to_location',
             'Person', 'Contact', 'Date',
             )] + [row[1:] for row in movements]
    df1 = pd.DataFrame(data1[1:], columns=data1[0])
    Outwards = Outwarding.query \
        .join(ProductMovement, Outwarding.productId == ProductMovement.productId) \
        .add_columns(
        Outwarding.type,
        Outwarding.productId,
        Outwarding.part_id,
        Outwarding.area,
        Outwarding.quantity,
        Outwarding.to_location,
        Outwarding.sales_id,
        Outwarding.operationperson_id,
        Outwarding.operationperson_phn,
        Outwarding.outward_time) \
        .group_by(Outwarding.outward_id) \
 \
    .all()
    inwards = Inwarding.query \
        .join(Product, Inwarding.productId == Product.productId) \
        .add_columns(
        Inwarding.inwarding_id,
        Inwarding.productId,
        Inwarding.part_id,
        Inwarding.cost,
        Inwarding.area,
        Inwarding.quantity,
        Inwarding.location_id,
        Inwarding.location_area,
        Inwarding.operationperson_id,
        Inwarding.operationperson_phn,
        Inwarding.vendor_id,
        Inwarding.vendor_address,
        Inwarding.vendor_phn,
        (Inwarding.cost * Inwarding.quantity).label('Tcost'),
        (Inwarding.area * Inwarding.quantity).label('Tarea'),
        Inwarding.inwarding_time,
        Inwarding.type,
    ) \
        .group_by(Inwarding.inwarding_id) \
        .all()
    data2 = [('Type', 'Part', 'Id','Area', 'Quantity', "from_location", 'to_location',
              'Person', 'Contact', 'Date',
              )] + [row[1:] for row in Outwards]
    df2 = pd.DataFrame(data2[1:], columns=data2[0])
    merged_df = pd.concat([df1,df], axis=0)
    merged_df.fillna(0, inplace=True)
    new_df = merged_df.assign(Area=lambda x: x['Area'] * x['Quantity'])
    pivot_df1 = new_df.pivot_table(values='Area', index=['Part', 'Id', 'Date'], columns='to_location', aggfunc=np.sum,
                                   fill_value=0)
    pivot_df1.loc['Total'] = pivot_df1.sum()
    pivot_df1 = pivot_df1.reset_index()
    pivot_dict = pivot_df1.to_dict('split')
    total_dict = {pivot_dict['columns'][i]: pivot_dict['data'][-1][i] for i in range(len(pivot_dict['columns']))}
    locations = Location.query.order_by(Location.date_created).all()
    location_dict = {location.location_id: location.location_area for location in locations}
    result_dict = {}
    for key, value in location_dict.items():
        if key in total_dict:
            result_dict[key] = value - total_dict[key]
    merged_df['Date'] = pd.to_datetime(merged_df['Date']).dt.strftime('%Y-%m-%d')
    print(merged_df.to_string())
    totals = {}
    for index, row in merged_df.iterrows():
        key = (row['Part'],row["Id"],row["Area"],row["Date"], row['to_location'])
        if key in totals:
            totals[key] += row['Quantity']
        else:
            totals[key] = row['Quantity']
    for index, row in df.iterrows():
        key = (row['Part'],row["Id"],row["Area"],row["Date"], row['to_location'])
        if key in totals:
            df.at[index, 'Quantity'] += totals[key]
    for index, row in df2.iterrows():
        key = (row['Part'],row["Id"],row["Area"],row["Date"],row['to_location'])
        if key in totals:
            df2.at[index, 'Quantity'] += totals[key]

    pivot_df = merged_df.pivot_table(values='Quantity', index=['Part', 'Id', 'Date'], columns='to_location',
                                     aggfunc=np.sum,
                                     fill_value=0)
    pivot_df['Total'] = pivot_df.sum(axis=1)
    total=pivot_df["Total"].sum()
    print(pivot_df.to_string())
    totals1={}
    for index, row in merged_df.iterrows():
        key = (row['Part'],row["Id"],row["Area"],row["Date"], row['to_location'])
        if key in totals1:
            totals[key] += row['Quantity1']
        else:
            totals[key] = row['Quantity1']
    initial_quantity = merged_df.pivot_table(values='Quantity1', index=['Part', 'Id', 'Date'], columns='to_location',
                                     aggfunc=np.sum,
                                     fill_value=0)
    initial_quantity["Total"]=initial_quantity.sum(axis=1)
    total1=initial_quantity["Total"].sum()
    print(initial_quantity.to_string())
    count = 0
    part_list = []
    for index, row in pivot_df.iterrows():
        if row['Total'] <= 20:
            count += 1
            part_list.append({'part': row.name[0], 'quantity': row['Total']})

    count1=0
    part_list1 =[]
    for index,row in pivot_df.iterrows():
         if row["Total"] ==0:
             count1+= 1
             part_list1.append({'part': row.name[0], 'quantity': row['Total']})
    if start_date and end_date:
        merged_df = merged_df[(merged_df['Date'] >= start_date) & (merged_df['Date'] <= end_date)]
    merged_df.reset_index(drop=True, inplace=True)
    new_df1 = merged_df.assign(Area=lambda x: x["Area"])
    grouped = merged_df.groupby('to_location')
    tables = {}
    for name, group in grouped:
        tables[name] = group.to_html(index=False)
    pivot_df3 = merged_df.pivot_table(values='Quantity', index=['Part', 'Id', 'Date'], columns='to_location',
                                     aggfunc=np.sum,
                                     fill_value=0)
    pivot_df3['Total'] = pivot_df3.sum(axis=1)
    pivot_df3 = pivot_df3.reset_index()
    total=pivot_df3["Total"].sum()
    session['pivot_df3'] = pivot_df3.to_json()
    conn = sqlite3.connect('inventory.db')
    pivot_df3.to_sql('overall product balance', conn, if_exists='replace', index=True)
    conn.close()
    table_html = pivot_df3.to_html()
    return render_template('newform.html', table_html=table_html,location_dict= location_dict,result_dict=result_dict,count=count,part_list=part_list,count1=count1,part_list1=part_list1)
@app.route('/download-pivot-csv')
def download_pivot_csv():
    output = io.StringIO()
    df_json = session['pivot_df3']
    pivot_df3 = pd.read_json(df_json)
    csv = pivot_df3.to_csv(index=False)
    response = make_response(csv)
    response.headers['Content-Disposition'] = 'attachment; filename=filtered.csv'
    response.headers['Content-type'] = 'text/csv'
    return response
@app.route('/locations/', methods=["POST", "GET"])
def viewLocation():
    if (request.method == "POST") and ('location_id' in request.form) and ('location_area' in request.form):
        location_id = request.form["location_id"]
        location_area = request.form["location_area"]
        new_location = Location(location_id=location_id, location_area=location_area)
        print(new_location)
        try:
            db.session.add(new_location)
            db.session.commit()
            return redirect("/locations/")
        except:
            locations = Location.query.order_by(Location.date_created).all()
            return "There Was an issue while add a new Location"
    else:
        locations = Location.query.order_by(Location.date_created).all()
        location_dict = {location.location_id: location.location_area for location in locations}
        print(location_dict)
        return render_template("locations.html", locations=locations)
@app.route('/sales/', methods=["POST", "GET"])
def viewSales():
    if (request.method == "POST") and ('sales_id' in request.form):
        sales_id = request.form["sales_id"]
        new_sales = Sales(sales_id=sales_id)
        try:
            db.session.add(new_sales)
            db.session.commit()
            return redirect("/sales/")
        except:
            sales = Sales.query.order_by(Sales.date_created).all()
            return "There Was an issue while add a new Location"
    else:
        sales = Sales.query.order_by(Sales.date_created).all()
        return render_template("sales.html", sales=sales)
@app.route("/inwarding/", methods=["POST", "GET"])
def viewMovement():
    if request.method == "POST":
        productId = request.form["productId"]
        part_id = request.form["part_id"]
        area = request.form["area"]
        cost = request.form["cost"]
        quantity = request.form["quantity"]
        location_id = request.form["location_id"]
        location_area = request.form["location_area"]
        vendor_id = request.form["vendor_id"]
        vendor_address = request.form["vendor_address"]
        vendor_phn = request.form["vendor_phn"]
        operationperson_id = request.form["operationperson_id"]
        operationperson_phn = request.form["operationperson_phn"]
        existing_inward = Inwarding.query.filter_by(productId=productId,part_id=part_id,area=area, vendor_address=vendor_address,
                                                     cost=cost, location_id=location_id,location_area=location_area,
                                                    operationperson_id=operationperson_id,
                                                    operationperson_phn=operationperson_phn, vendor_id=vendor_id,
                                                    vendor_phn=vendor_phn,
                                                    ).first()

        new_inward = Inwarding(
                productId=productId,
                part_id=part_id,
                area=area,
                cost=cost,
                quantity=quantity,
                quantity1=quantity,
                location_id=location_id,
                location_area=location_area,
                operationperson_id=operationperson_id,
                operationperson_phn=operationperson_phn,
                vendor_id=vendor_id,
                vendor_phn=vendor_phn,
                vendor_address=vendor_address)


        print(new_inward)
        try:
          db.session.add(new_inward)
          db.session.commit()
        except:
                return "There was an issue while adding a new entry"
        return redirect("/inwarding/")
    else:
        products = Product.query.order_by(Product.date_created).all()
        locations = Location.query.order_by(Location.date_created).all()
        persons = Person.query.order_by(Person.date_created).all()
        vendors = Vendor.query.order_by(Vendor.date_created).all()
        form_dict = request.form.to_dict()
        total_tarea_subquery = db.session.query(
            Inwarding.location_id,
            func.sum(Inwarding.area * Inwarding.quantity).label('total_tarea')
        ).group_by(Inwarding.location_id).subquery()
        inwards = Inwarding.query \
            .join(Product, Inwarding.productId == Product.productId) \
            .add_columns(
            Inwarding.inwarding_id,
            Inwarding.productId,
            Inwarding.part_id,
            Inwarding.cost,
            Inwarding.area,
            Inwarding.quantity,
            Inwarding.quantity1,
            Inwarding.location_id,
            Inwarding.location_area,
            Inwarding.operationperson_id,
            Inwarding.operationperson_phn,
            Inwarding.vendor_id,
            Inwarding.vendor_address,
            Inwarding.vendor_phn,
            (Inwarding.cost * Inwarding.quantity).label('Tcost'),
            (Inwarding.area * Inwarding.quantity).label('Tarea'),
            Inwarding.inwarding_time,
            Inwarding.type,
        ) \
            .group_by(Inwarding.inwarding_id) \
            .all()
        print(inwards)
        return render_template("inwarding.html", inwards=inwards, products=products, locations=locations,
                               persons=persons, vendors=vendors)
@app.route("/movements/", methods=["POST", "GET"])
def viewMovements():
    if request.method == "POST":
        productId = request.form["productId"]
        part_id = request.form["part_id"]
        quantity = int(request.form["quantity"])
        area = request.form["area"]
        operationperson_id = request.form["operationperson_id"]
        operationperson_phn = request.form["operationperson_phn"]
        fromLocation = request.form["fromLocation"]
        toLocation = request.form["toLocation"]
        zero_quantity_locations = ProductMovement.query.filter(ProductMovement.quantity == 0).all()
        location_entry = Inwarding.query.filter_by(location_id=fromLocation, productId=productId).first()
        location_entry1 = ProductMovement.query.filter_by(productId=productId, to_location=fromLocation).first()
        location_id = location_entry.location_id if location_entry else None
        to_location = location_entry1.to_location if location_entry1 else None
        inwarding_entry = Inwarding.query.filter_by(location_id=fromLocation, productId=productId).filter(Inwarding.quantity > 0) \
        .all()

        movements_entry = ProductMovement.query.filter_by(productId=productId, part_id=part_id, area=area,
                                                          to_location=fromLocation) \
            .filter(ProductMovement.quantity > 0) \
            .all()
        session['productId'] = productId
        remaining_quantity = quantity

        if inwarding_entry:
            for inwarding in inwarding_entry:
                if remaining_quantity <= inwarding.quantity:
                    inwarding.quantity -= remaining_quantity
                    db.session.commit()
                    break
                else:
                    remaining_quantity -= inwarding.quantity
                    inwarding.quantity = 0
                    db.session.commit()

        if movements_entry and remaining_quantity > 0:
            for movement in movements_entry:
                if remaining_quantity <= movement.quantity:
                    movement.quantity -= remaining_quantity
                    db.session.commit()
                    break
                else:
                    remaining_quantity -= movement.quantity
                    movement.quantity = 0
                    db.session.commit()

        existing_movement = ProductMovement.query.filter_by(productId=productId, from_location=fromLocation,
                                                            to_location=toLocation).first()

        if existing_movement:
            existing_movement.quantity += quantity
            db.session.commit()
        else:
            new_movement = ProductMovement(
                productId=productId, part_id=part_id, area=area, operationperson_id=operationperson_id,
                operationperson_phn=operationperson_phn, quantity=quantity, from_location=fromLocation,
                to_location=toLocation)
            try:
                db.session.add(new_movement)
                db.session.commit()
            except:
                return jsonify({"message": "There was an issue while adding a new Movement."})

        return redirect("/movements/")
    else:
        inwarding = Inwarding.query.order_by(Inwarding.inwarding_time).all()
        locations = Location.query.order_by(Location.location_id).all()
        movs = ProductMovement.query \
            .join(Inwarding, ProductMovement.productId == Inwarding.productId) \
            .add_columns(
            ProductMovement.movement_id,
            ProductMovement.quantity,
            ProductMovement.area,
            ProductMovement.productId,
            ProductMovement.part_id,
            ProductMovement.operationperson_id,
            ProductMovement.operationperson_phn,
            ProductMovement.from_location,
            ProductMovement.to_location,
            ProductMovement.area * ProductMovement.quantity.label('Tarea'),
            ProductMovement.type,
            ProductMovement.movement_time) \
            .all()
        movements = ProductMovement.query.order_by(ProductMovement.movement_time).all()
        inwards = Inwarding.query \
            .join(Product, Inwarding.productId == Product.productId) \
            .add_columns(
            Inwarding.inwarding_id,
            Inwarding.productId,
            Inwarding.part_id,
            Inwarding.cost,
            Inwarding.area,
            Inwarding.quantity,
            Inwarding.location_id,
            Inwarding.location_area,
            Inwarding.operationperson_id,
            Inwarding.operationperson_phn,
            Inwarding.vendor_id,
            Inwarding.vendor_address,
            Inwarding.vendor_phn,
            (Inwarding.cost * Inwarding.quantity).label('Tcost'),
            (Inwarding.area * Inwarding.quantity).label('Tarea'),
            func.sum(Inwarding.area).label('total_area'),
        ) \
            .group_by(Inwarding.inwarding_id) \
            .all()
        return render_template("movements.html", movements=movs, inwarding=inwarding, locations=locations,
                              )
@app.route("/get_locations/<productId>")
def getLocations(productId):
    locations = Inwarding.query.filter_by(productId=productId).all()
    movements = ProductMovement.query.filter_by(productId=productId).all()

    valid_movements = []
    for movement in movements:
        if movement.quantity > 0:
            valid_movements.append(movement)
    valid_locations = []
    for location in locations:
        if location.quantity > 0:
            valid_locations.append(location)
    data = [{"location_id": location.location_id} for location in valid_locations]
    data += [{"location_id": movement.to_location} for movement in valid_movements]

    return jsonify(data)
@app.route('/delete_zero_quantity/')
def delete_zero_quantity():
    zero_quantity_locations = ProductMovement.query.filter(ProductMovement.quantity == 0).all()
    for r in zero_quantity_locations:
        db.session.delete(r)
    db.session.commit()
    return 'Deleted records with quantity zero'
@app.route("/get_locations_mov/<productId>")
def getMLocations(productId):
    locations = ProductMovement.query.filter_by(productId=productId).all()
    valid_locations = []
    for location in locations:
        if location.quantity > 0:
            valid_locations.append(location)
    data = [{"to_location": location.to_location} for location in valid_locations]
    return jsonify(data)
@app.route("/outwards/", methods=["POST", "GET"])
def viewoutwards():
    if request.method == "POST":
        productId = request.form["productId"]
        part_id = request.form["part_id"]
        quantity = int(request.form["quantity"])
        area =request.form["area"]
        operationperson_id = request.form["operationperson_id"]
        operationperson_phn = request.form["operationperson_phn"]
        toLocation = request.form["toLocation"]
        sales_id   =request.form["sales_id"]
        sales     = Sales.query.filter_by(sales_id=sales_id).first().sales_id
        location_entry1 = ProductMovement.query.filter_by(productId=productId, part_id=part_id,area=area,
                                                    to_location=toLocation).first()

        to_location = location_entry1.to_location if location_entry1 else None
        movements_entry = ProductMovement.query.filter_by(productId=productId, part_id=part_id, area=area,
                                                          to_location=toLocation) \
            .filter(ProductMovement.quantity > 0) \
            .all()
        remaining_quantity = quantity
        if movements_entry and remaining_quantity > 0:
            for movement in movements_entry:
                if remaining_quantity <= movement.quantity:
                    movement.quantity -= remaining_quantity
                    db.session.commit()
                    break
                else:
                    remaining_quantity -= movement.quantity
                    movement.quantity = 0
                    db.session.commit()

        existing_outward = Outwarding.query.filter_by(productId=productId, part_id=part_id, quantity=quantity,
                                                      area=area, operationperson_id=operationperson_id,
                                                      operationperson_phn=operationperson_phn,
                                                      to_location=toLocation, sales_id=sales_id).first()
        if existing_outward:
             existing_outward.quantity += quantity
             db.session.commit()
        else:
             new_outwards = Outwarding(
                productId=productId, part_id=part_id,area=area, operationperson_id=operationperson_id,
                operationperson_phn=operationperson_phn, quantity=quantity,
                to_location=toLocation,sales_id=sales_id)
             try:
                db.session.add(new_outwards)
                db.session.commit()
             except:
                 return jsonify({"message": "There was an issue while adding a new Movement."})

        return redirect("/outwards/")
    else:
        movements = ProductMovement.query.order_by(ProductMovement.movement_time).all()
        locations = Location.query.order_by(Location.location_id).all()
        sales    =Sales.query.order_by(Sales.sales_id).all()
        Outwards = Outwarding.query \
            .join(ProductMovement, Outwarding.productId == ProductMovement.productId) \
            .add_columns(
            Outwarding.outward_id,
            Outwarding.quantity,
            Outwarding.area,
            Outwarding.productId,
            Outwarding.part_id,
            Outwarding.operationperson_id,
            Outwarding.operationperson_phn,
            Outwarding.to_location,
            Outwarding.sales_id,
            Outwarding.type,
            Outwarding.outward_time) \
            .all()
        outwards = Outwarding.query.order_by(Outwarding.outward_time).all()
        return render_template("outwards.html", outwards=Outwards, movements=movements, locations=locations,sales=sales)
@app.route("/product-balance/", methods=["POST", "GET"])
def table1():
    start_date =request.form.get("start_date")
    end_date = request.form.get("end_date")
    inwards = Inwarding.query \
        .join(Product, Inwarding.productId == Product.productId) \
        .add_columns(
        Inwarding.type,
        Inwarding.productId,
        Inwarding.part_id,
        Inwarding.area,
        Inwarding.quantity,
        Inwarding.quantity1,
        Inwarding.location_id,
        Inwarding.operationperson_id,
        Inwarding.operationperson_phn,
        Inwarding.inwarding_time,
    ) \
        .group_by(Inwarding.inwarding_id) \
        .all()
    data = [('Type', 'Part', 'Id','Area', 'Quantity','Quantity1','to_location',
             'Person', 'Contact', 'Date',
             )] + [row[1:] for row in inwards]
    df = pd.DataFrame(data[1:], columns=data[0])
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    df.fillna(0,inplace=True)
    print(df.to_string())
    if start_date and end_date:
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    totals1={}
    for index, row in df.iterrows():
        key = (row['Part'],row["Id"],row["Area"],row["Date"], row['to_location'])
        if key in totals1:
            totals1[key] += row['Quantity1']
        else:
            totals1[key] = row['Quantity1']
    initial_quantity = df.pivot_table(values='Quantity1', index=['Part', 'Id', 'Date'], columns='to_location',
                                     aggfunc=np.sum,
                                     fill_value=0)
    initial_quantity["Total"]=initial_quantity.sum(axis=1)
    initial_quantity = initial_quantity.reset_index()
    total1=initial_quantity["Total"].sum()
    session['initial_quantity'] = initial_quantity.to_json()
    conn = sqlite3.connect('inventory.db')
    initial_quantity.to_sql('Intial meterial quantities', conn, if_exists='replace', index=True)
    conn.close()
    table_html = initial_quantity.to_html()
    return render_template('product-balance.html', table_html=table_html)
@app.route('/download-pivot-csv_file')
def download_pivot_csv_file():
    output = io.StringIO()
    df_json = session['initial_quantity']
    initial_quantity = pd.read_json(df_json)
    csv = initial_quantity.to_csv(index=False)
    response = make_response(csv)
    response.headers['Content-Disposition'] = 'attachment; filename=filtered.csv'
    response.headers['Content-type'] = 'text/csv'
    return response
@app.route("/vendors/", methods=["POST", "GET"])
def viewVendors():
    if (request.method == "POST") and ('vendor_id' in request.form) and ("vendor_address" in request.form) and (
            "vendor_phn" in request.form):
        vendor_id = request.form["vendor_id"]
        vendor_address = request.form["vendor_address"]
        vendor_phn = request.form["vendor_phn"]
        new_vendor = Vendor(vendor_id=vendor_id, vendor_address=vendor_address, vendor_phn=vendor_phn)
        try:
            db.session.add(new_vendor)
            db.session.commit()
            return redirect("/vendors/")
        except:
            vendors = Vendor.query.order_by(Vendor.date_created).all()
            return "There Was an issue while add a new vendor"
    else:
        vendors = Vendor.query.order_by(Vendor.date_created).all()
        return render_template("vendors.html", vendors=vendors)
@app.route('/products/', methods=["POST", "GET"])
def viewProduct():
    if (request.method == "POST") and ('productId' in request.form) and ("part_id" in request.form) and (
            "area" in request.form):
        productId = request.form["productId"]
        part_id = request.form["part_id"]
        area = request.form["area"]
        new_product = Product(productId=productId, part_id=part_id, area=area)
        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/products/")
        except Exception as e:
            print(e)
            db.session.rollback()
            return "There Was an issue while add a new Product"
            products = Product.query.order_by(Product.date_created).all()
    else:
        products = Product.query.order_by(Product.date_created).all()
        return render_template("products.html", products=products)
@app.route('/operationperson/', methods=["POST", "GET"])
def viewPerson():
    if (request.method == "POST") and ('operationperson_id' in request.form) and (
            "operationperson_phn" in request.form):
        operationperson_id = request.form["operationperson_id"]
        operationperson_phn = request.form["operationperson_phn"]
        new_person = Person(operationperson_id=operationperson_id, operationperson_phn=operationperson_phn)
        try:
            db.session.add(new_person)
            db.session.commit()
            return redirect("/operationperson/")
        except:
            persons = Person.query.order_by(Person.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        persons = Person.query.order_by(Person.date_created).all()
        return render_template("operationperson.html", persons=persons)
@app.route("/get_part_id", methods=["POST"])
def get_part_id():
    productId = request.form["productId"]
    product = Product.query.filter_by(productId=productId).first()
    if product:
        return {"part_id": product.part_id, "area": product.area}
    else:
        return {"part_id": ""}
@app.route("/get_vend_id", methods=["POST"])
def get_vend_id():
    vendor_id = request.form["vendor_id"]
    vendor = Vendor.query.filter_by(vendor_id=vendor_id).first()
    if vendor:
        return {"vendor_address": vendor.vendor_address, "vendor_phn": vendor.vendor_phn}
    else:
        return {"vendor_address": ""}
@app.route("/get_person_id", methods=["POST"])
def get_person_id():
    operationperson_id = request.form["operationperson_id"]
    person = Person.query.filter_by(operationperson_id=operationperson_id).first()
    if person:
        return {"operationperson_phn": person.operationperson_phn}
    else:
        return {"operationperson_phn": ""}
@app.route("/get_location_area", methods=["POST"])
def get_location_area():
    location_id = request.form["location_id"]
    location = Location.query.filter_by(location_id=location_id).first()
    if location:
        return {"location_area": location.location_area}
    else:
        return {"location_area": ""}
@app.route("/delete-product/<name>")
def deleteProduct(name):
    product = Product.query.get_or_404(name)
    print(product)
    old_product_id = product.productId
    inwardings = Inwarding.query.filter_by(productId=old_product_id).all()
    movements = ProductMovement.query.filter_by(productId=old_product_id).all()
    out       = Outwarding.query.filter_by(productId =old_product_id).all()
    for inwarding in inwardings:
        db.session.delete(inwarding)
        db.session.delete(product)
        db.session.commit()
    for mov in movements:
        db.session.delete(mov)
    for outwarding in out:
        db.session.delete(outwarding)
    db.session.delete(product)
    db.session.commit()
    return redirect("/products/")
@app.route("/update-location/<name>", methods=["POST", "GET"])
def updateLocation(name):
    location = Location.query.get_or_404(name)
    old_location = location.location_id
    if request.method == "POST":
        location.location_id = request.form['location_id']
        location.location_area = request.form["location_area"]
        try:
            db.session.commit()
            updateLocationInMovements(old_location, request.form['location_id'],request.form["location_area"])
            return redirect("/locations/")
        except:
            return "There was an issue while updating the Location"
    else:
        location_area= request.args.get("location_area","")
        return render_template("update-location.html", location=location, location_area=location_area)
@app.route("/delete-location/<name>")
def deleteLocation(name):
    location = Location.query.get_or_404(name)
    old_location_id = location.location_id
    inwardings    = Inwarding.query.filter_by(location_id=old_location_id).all()
    movements     =ProductMovement.query.filter_by(from_location=old_location_id).all()
    movements1    =ProductMovement.query.filter_by(to_location= old_location_id).all()
    out           =Outwarding.query.filter_by(to_location=old_location_id).all()
    for inwarding in inwardings:
        db.session.delete(inwarding)
        db.session.delete(location)
        db.session.commit()
    for mov in movements:
        db.session.delete(mov)
    for mov1 in movements1:
        db.session.delete(mov1)
        db.session.commit()
    for outwarding in out:
        db.session.delete(outwarding)
    db.session.delete(location)
    db.session.commit()
    return redirect("/locations/")
@app.route("/delete-person/<name>")
def deletePerson(name):
    person = Person.query.get_or_404(name)
    old_person_id = person.operationperson_id
    inwardings = Inwarding.query.filter_by(operationperson_id=old_person_id).all()
    movements  = ProductMovement.query.filter_by(operationperson_id=old_person_id).all()
    out         =Outwarding.query.filter_by(operationperson_id=old_person_id).all()
    for inwarding in inwardings:
        db.session.delete(inwarding)
        db.session.delete(person)
        db.session.commit()
    for mov in movements:
        db.session.delete(mov)
        db.session.commit()
    for outwarding in out:
        db.session.delete(outwarding)
        db.session.commit()
    db.session.delete(person)
    db.session.commit()
    return redirect("/operationperson/")
@app.route("/delete-vendor/<name>")
def deleteVendor(name):
    vendor_to_delete = Vendor.query.get_or_404(name)
    try:
        db.session.delete(vendor_to_delete)
        db.session.commit()
        return redirect("/vendors/")
    except:
        return "There was an issue while deleting the Vendor"

@app.route("/dub-locations/", methods=["POST", "GET"])
def getDublicate():
    location = request.form["location"]
    locations = Location.query.\
        filter(Location.location_id == location).\
        all()
    print(locations)
    if locations:
        return {"output": False}
    else:
        return {"output": True}
@app.route("/dub-sales/", methods=["POST", "GET"])
def getSdublicate():
    sales_id = request.form["sales_id"]
    sales = Sales.query. \
        filter(Sales.sales_id == sales_id). \
        all()
    print(sales)
    if sales:
        return {"output": False}
    else:
        return {"output": True}
@app.route("/dub-products/", methods=["POST"])
def dubProducts():
    productId = request.form["productId"]
    part_id = request.form["part_id"]
    area = request.form["area"]
    product = Product.query.filter_by(productId=productId, part_id=part_id, area=area).first()
    if product:
        return jsonify({"output": False})
    else:
        return jsonify({"output": True})
@app.route("/dub-person/", methods=["POST"])
def getPeDublicate():
    operationperson_id = request.form["operationperson_id"]
    operationperson_phn = request.form["operationperson_phn"]
    person= Person.query.filter_by(operationperson_id =operationperson_id,operationperson_phn=operationperson_phn).first()
    if person:
        return jsonify({"output": False})
    else:
        return jsonify({"output": True})
@app.route("/dub-vendors/", methods=["POST", "GET"])
def getVDublicate():
    vendor_id = request.form["vendor_id"]
    vendors = Vendor.query. \
        filter(Vendor.vendor_id == vendor_id). \
        all()
    if vendors:
        return {"output": False}
    else:
        return {"output": True}

@app.route('/check_quantity/', methods=['POST'])
def check_quantity():
    productId = request.form['productId']
    quantity = int(request.form['quantity'])
    fromLocation = request.form["fromLocation"]
    inwarding_entries = Inwarding.query.filter_by(location_id=fromLocation, productId=productId).filter(Inwarding.quantity > 0).all()
    for inwarding_entry in inwarding_entries:
        if quantity <= inwarding_entry.quantity:
            return "true"
        quantity -= inwarding_entry.quantity
    movements_entries = ProductMovement.query.filter_by(productId=productId,to_location=fromLocation).filter(ProductMovement.quantity > 0).all()
    for movements_entry in movements_entries:
        if quantity <= movements_entry.quantity:
            return "true"
        quantity -= movements_entry.quantity
    return 'false'
@app.route('/check_quantity_mov/', methods=['POST'])
def check_quantity_mov():
    productId = request.form['productId']
    quantity = request.form['quantity']
    toLocation = request.form["toLocation"]
    location_entry1 = ProductMovement.query.filter_by(to_location=toLocation,productId=productId) \
        .filter(ProductMovement.quantity > 0) \
        .all()
    if location_entry1:
        movement_entry =location_entry1[0]
        to_location = movement_entry.to_location
        if int(quantity) <=movement_entry.quantity:
            return "true"
    return "false"
@app.route("/delete-inward/<int:id>")
def deleteInward(id):
    inward_to_delete = Inwarding.query.get_or_404(id)
    try:
        db.session.delete(inward_to_delete)
        db.session.commit()
        return redirect("/inwarding/")
    except:
        return "There was an issue while deleteing the Prodcut Movement"
@app.route("/delete-movement/<int:id>")
def deleteMovement(id):
    movement_to_delete = ProductMovement.query.get_or_404(id)
    try:
        db.session.delete(movement_to_delete)
        db.session.commit()
        return redirect("/movements/")
    except:
        return "There was an issue while deleteing the Inwarding"
@app.route("/update-product/<name>", methods=["POST", "GET"])
def updateProduct(name):
    product = Product.query.get_or_404(name)
    old_product = product.productId
    if request.method == "POST":
        product.productId    = request.form['productId']
        product.part_id = request.form['part_id']
        product.area = request.form['area']
        try:
            db.session.commit()
            updateProductInMovements(old_product, request.form['productId'], request.form['part_id'],request.form['area'])
            return redirect("/products/")
        except:
            return "There was an issue while updating the vendor"
    else:
        part_id = request.args.get('part_id', '')
        area = request.args.get('area', '')
        return render_template("update-product.html", product=product, part_id=part_id, area=area)
@app.route("/update-person/<name>", methods=["POST", "GET"])
def updatePerson(name):
    person = Person.query.get_or_404(name)
    old_person = person.operationperson_id
    if request.method == "POST":

        person.operationperson_id    = request.form['operationperson_id']
        person.operationperson_phn = request.form['operationperson_phn']
        try:
            db.session.commit()
            updatePersonInMovements(old_person, request.form['operationperson_id'], request.form['operationperson_phn'])
            return redirect("/operationperson/")
        except:
            return "There was an issue while updating the person"
    else:
        operationperson_phn = request.args.get('operationperson_phn', '')
        return render_template("update-person.html",person=person,operationperson_phn=operationperson_phn)
def updateLocationInMovements(oldLocation, newLocation,newArealocation):
    movement = ProductMovement.query.filter(ProductMovement.from_location == oldLocation).all()
    movement2 = ProductMovement.query.filter(ProductMovement.to_location == oldLocation).all()
    inwards = Inwarding.query.filter(Inwarding.location_id == oldLocation).all()
    outwards = Outwarding.query.filter(Outwarding.to_location == oldLocation).all()
    for inward in inwards:
        inward.location_id = newLocation
        inward.location_area = newArealocation
    for mov in movement2:
        mov.to_location = newLocation
        mov.location_area = newArealocation
    for mov in movement:
        mov.from_location = newLocation
        mov.location_area = newArealocation
    for outward in outwards:
        outward.to_location =newLocation
        outward.location_area =newArealocation
    db.session.commit()

def updateProductInMovements(old_product, newProduct, newPartId, newArea):
        movements = ProductMovement.query.filter(ProductMovement.productId == old_product).all()
        inwards = Inwarding.query.filter(Inwarding.productId == old_product).all()
        outwards = Outwarding.query.filter(Outwarding.productId == old_product).all()
        for inward in inwards:
            inward.productId = newProduct
            inward.part_id = newPartId
            inward.area = newArea
        for movement in movements:
            movement.productId = newProduct
            movement.part_id = newPartId
            movement.area = newArea
        for outward in outwards:
            outward.productId = newProduct
            outward.part_id = newPartId
            outward.area = newArea
        db.session.commit()
def updatePersonInMovements(old_person,newPerson,newPersonphn):
    movements =ProductMovement.query.filter(ProductMovement.operationperson_id ==old_person).all()
    inwards = Inwarding.query.filter(Inwarding.operationperson_id == old_person).all()
    outwards =Outwarding.query.filter(Outwarding.operationperson_id == old_person).all()
    for inward in inwards:
        inward.operationperson_id =newPerson
        inward.operationperson_phn=newPersonphn
    for movement in movements:
        movement.operationperson_id=newPerson
        movement.operationperson_phn = newPersonphn
    for outward in outwards:
        outward.operationperson_id =newPerson
        outward.operationperson_phn = newPersonphn
    db.session.commit()

if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=9068)
