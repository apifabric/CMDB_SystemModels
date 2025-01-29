import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 3273861233231306240 in succeeded_hashes:  # avoid duplicate inserts
            instance = manufacturer1 = Manufacturer(id=1, name="TechCorp")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3273861233231306240)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2917562707169800919 in succeeded_hashes:  # avoid duplicate inserts
            instance = manufacturer2 = Manufacturer(id=2, name="GadgetWorks")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2917562707169800919)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1309937817643038083 in succeeded_hashes:  # avoid duplicate inserts
            instance = manufacturer3 = Manufacturer(id=3, name="DeviceMakers")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1309937817643038083)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -94812646310227210 in succeeded_hashes:  # avoid duplicate inserts
            instance = manufacturer4 = Manufacturer(id=4, name="Innovatech")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-94812646310227210)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7179555253235926926 in succeeded_hashes:  # avoid duplicate inserts
            instance = device1 = Device(id=1, name="Printer Model X", model_id=1, purchase_date=date(2021, 6, 1), warranty_expiry=date(2023, 6, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7179555253235926926)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3813350575382690852 in succeeded_hashes:  # avoid duplicate inserts
            instance = device2 = Device(id=2, name="Laptop Pro", model_id=2, purchase_date=date(2020, 9, 15), warranty_expiry=date(2022, 9, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3813350575382690852)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3366643638673491567 in succeeded_hashes:  # avoid duplicate inserts
            instance = device3 = Device(id=3, name="Server Prime", model_id=3, purchase_date=date(2019, 11, 18), warranty_expiry=date(2021, 11, 18))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3366643638673491567)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4315526267638105588 in succeeded_hashes:  # avoid duplicate inserts
            instance = device4 = Device(id=4, name="Router Spec", model_id=4, purchase_date=date(2022, 7, 10), warranty_expiry=date(2024, 7, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4315526267638105588)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2693551666605496246 in succeeded_hashes:  # avoid duplicate inserts
            instance = incident1 = Incident(id=1, device_id=1, description="Printer not responding", date_reported=date(2023, 3, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2693551666605496246)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6173021386793538604 in succeeded_hashes:  # avoid duplicate inserts
            instance = incident2 = Incident(id=2, device_id=2, description="Laptop overheating", date_reported=date(2023, 5, 12))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6173021386793538604)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4351872467666979231 in succeeded_hashes:  # avoid duplicate inserts
            instance = incident3 = Incident(id=3, device_id=3, description="Server downtime", date_reported=date(2023, 1, 22))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4351872467666979231)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 550488187979453254 in succeeded_hashes:  # avoid duplicate inserts
            instance = incident4 = Incident(id=4, device_id=4, description="Router latency", date_reported=date(2023, 4, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(550488187979453254)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
