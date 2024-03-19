import sqlite3
import shutil
import datetime
import os
db_path = r'C:\Users\Aparna\My Flask webapps\pythonProject19\inventory.db'
backup_dir = r'C:\Users\Aparna\Desktop\backupinventory.db'
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
backup_filename = 'backup-{}.db'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
conn = sqlite3.connect(db_path)
shutil.copy(db_path, os.path.join(backup_dir, backup_filename))
conn.close()