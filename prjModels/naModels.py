from peewee import *

# файл моделей базы пример подключения к базе postgres локально
db = PostgresqlDatabase('postgres', user='postgres', password='postgres',
                        host='127.0.0.1', port=5432)
# файл моделей базы пример подключения к базе postgres удаленно
db2 = PostgresqlDatabase('asu', user='postgres', password='P@ssw0rd2021',
                        host='10.155.23.16', port=5432)
# файл моделей базы пример подключения к базе sqlite локально
# db = SqliteDatabase("E:\sandbox\MK500\mnsbase.db",pragmas = {"foreign_keys": "on"})#имя базы данных
# sheet_name = ['КЦ','УСО.1(1)', 'УСО.1(2)', 'УСО.1(3)', 'УСО.3', 'УСО.1(4)', 'УСО.4']


sheet_name = ['КЦ', 'УСО.1(1)', 'УСО.1(2)', 'УСО.1(3)', 'УСО.2', 'УСО.3', 'УСО.4', 'УСО.2(1)',
              'УСО.2(2)']  # имена листов для сбора данных
xls_filename = 'E:\sandbox\pog.xlsm'  # имя файла КЗФКП
zd_type = ['DM01-2(2)', 'DM01-5(2)', 'DM04-2(1)', 'DM03-2(2)', 'DM01-5(1)', 'DM01-1(2)', 'DM01-3', 'DM01-1', 'DM01-7',
           'DM03-3(2)', 'DM04-1(2)']  # типы схем задвижек
oip_type = ['AI22-V', 'AI12(2)', 'AI02(2)', 'AI23(2)']  # типы схем OIP
vs_type = ['DM07-1']

service_signal = ['']
column_name = ['шкаф', 'tэг', 'наименование', 'схема', 'клк', 'конт', 'корз', 'мод', 'кан']



class Uso(Model):
    uso_id = CharField(primary_key=True)
    description = CharField(unique=True)


class ModuleType(Model):
    module_type_id = CharField(primary_key=True)
    sign = CharField()  # подпись на мнемосхеме (МК-ХХХ-ХХХ)
    description = CharField()
    tooltips = CharField()
    hwdesc = CharField()
    quantity = IntegerField()


class UsoModule(Basemodel):
    uso_id = CharField(null=False)
    position = CharField(null=False)
    sign = CharField(null=False)
    module_type_id = CharField(null=False)
    uso_module_id = CharField(primary_key=True)
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ

class Analog(Model):
#    kzfkp_id = ForeignKeyField(Kzfkp, unique=True, primary_key=True)
    tag = CharField(null=True)
    description = CharField(null=True)
    egu = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхеме
    msggrp = CharField(null=True)

class AuxSystems(Model):
    tag = CharField(null=True)
    description = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхеме

class Discret(Model):
    tag = CharField(null=True)
    description = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхеме
    colorsheme = CharField(null=True)

class UTS(Model):
    tag = CharField(null=True)
    description = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхемеГЕ

class Valves(Model):
    tag = CharField(null=True)
    description = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхеме

class NA(Model):
    tag = CharField(null=True)
    description = CharField(null=True)
    sign = CharField(null=True)  # подпись на мнемокадре
    index_arr = IntegerField(null=True)  # № элемента в массиве СУ
    zone = CharField(null=True)  # принадлежность к мнемосхеме


class Sheme(Model):#схемы подключения
    sheme_id = CharField(primary_key=True)
    typeobj = CharField()
    description = CharField(null=True)


class ProjectNFT(Basemodel):
    lib_id = CharField(primary_key=True)
    lib_name = CharField(unique=True)
    description = CharField()
    system_type_1 = CharField(null=True, default='1')
    system_desc_1 = CharField(null=True, default='2')
    system_type_2 = CharField(null=True, default='None')
    system_desc_2 = CharField(null=True, default='None')
    system_type_3 = CharField(null=True, default='None')
    system_desc_3 = CharField(null=True, default='None')
    system_type_4 = CharField(null=True, default='None')
    system_desc_4 = CharField(null=True, default='None')
    system_type_5 = CharField(null=True, default='None')
    system_desc_5 = CharField(null=True, default='None')


class ObjectType(Basemodel):
    object_id = CharField(primary_key=True)
    description = CharField()
    lib_id = CharField(unique=True)


class PrjAttributes(Basemodel):
    attributes_id = CharField(primary_key=True)
    description = CharField()
    attributes_type = CharField()
    attributes_value = CharField()

class Ustgrp(Basemodel):
    msggrp_id = CharField(primary_key=True)
    name = CharField()
    min6 = CharField(null=True)
    min5 = CharField(null=True)
    min4 = CharField(null=True)
    min3 = CharField(null=True)
    min2 = CharField(null=True)
    min1 = CharField(null=True)
    max1 = CharField(null=True)
    max2 = CharField(null=True)
    max3 = CharField(null=True)
    max4 = CharField(null=True)
    max5 = CharField(null=True)
    max6 = CharField(null=True)

class xls_kzfkp(Model):
    typesignal = CharField(null=True)
    cabinet = CharField(null=True)
    tag = CharField(null=True)
    desc = CharField(null=True)
    sheme = CharField(null=True)
    termblock = CharField(null=True)
    contacts = CharField(null=True)
    unit = CharField(null=True)
    module = CharField(null=True)
    channel = CharField(null=True)
    class Meta:
        database = db
        db_table = 'KD'



def base_write_many(objtables, data):
    i = 0
    j = 0
    arr = []
    for el in data:
        i = i + 1
        arr.append(el)
        if i % 50 == 0:
            objtables.insert_many(arr).on_conflict('replace').execute()
            arr.clear()
    try:
        objtables.insert_many(arr).on_conflict('replace').execute()
        j = i
        print("запись завершена, записано", j, " элементов")
    except:
        print('запись не удалась')

    return j


def base_write_many2(objtables, data):
    try:
        for idx in range(0, len(data), 500):
            objtables.insert_many(data[idx:idx + 500]).on_conflict('replace').execute()
        print("обновлено", objtables)
    except:
        print('обновление не удалась', objtables)
    try:
        print(len(data))
        for idx in range(0, len(data), 500):
            objtables.insert_many(data[idx:idx + 500]).on_conflict('ignore').execute()
        print("запись завершена, записано", objtables)
    except:
        print("не записано", objtables)


def ReadTypeSheme():
    Sheme.create_table()
    data = []
    for el in oip_type:
        arr = dict(Sheme_id=el,
                   TypeObj="Analog",
                   Description="Аналоговый параметр")
        data.append(arr)
    base_write_many2(Sheme, data)
    data = []
    for el in zd_type:
        arr = dict(Sheme_id=el,
                   TypeObj="Valve",
                   Description="Задвижка")
        data.append(arr)
    base_write_many2(Sheme, data)
    data = []
    for el in vs_type:
        arr = dict(Sheme_id=el,
                   TypeObj="AuxSystems",
                   Description="Вспомсистема")
        data.append(arr)
    base_write_many2(Sheme, data)


def ReadValve():
    Valves.create_table()
    data = []
    query = Kzfkp.select(Kzfkp, Sheme).join(Sheme, on=(Sheme.TypeObj == "Valve")).where(
        Kzfkp.TypeSheme == Sheme.Sheme_id)
    print(len((query)))
    for el in query:
        Index = 0
        Zone = ""
        if Valves.select().where(Valve.kzfkp_id == el.Signal_id).exists():
            qr = Valve.select().where(Valve.kzfkp_id == el.Signal_id).get()
            index = qr.Index
            print(Index)
            Zone = qr.Zone
        Valve = str(el.signalname).split(" ")
        a_dict = dict(Tag=str(Valve[1]).replace("№", "ZD_"),
                      Description=Valve[0] + " " + Valve[1],
                      sname=str(Valve[1]).replace("№", "Зд-"),
                      kzfkp_id=el.signal_id,
                      num_ZD=index,
                      Zone=zone)
        data.append(a_dict)
    base_write_many2(Valves, data)


def UVS():
    VS.create_table()
    data = []
    query = kzfkp.select(kzfkp, TypeSheme).join(TypeSheme, on=(TypeSheme.TypeObj == "VS")).where(
        kzfkp.TypeSheme == TypeSheme.Sheme_id)
    print(len((query)))
    for el in query:
        num_VS = 0
        Zone = ""
        tags = ""
        sname = ""
        if VS.select().where(VS.kzfkp_id == el.Signal_id).exists():
            qr = VS.select().where(VS.kzfkp_id == el.Signal_id).get()
            tags = qr.Tag
            sname = qr.sname
            num_VS = qr.num_VS
            Zone = qr.Zone
        UVS = str(el.SignalName).split(" - ")
        a_dict = dict(Tag=tags,
                      Description=str(UVS[0]).replace("-", ""),
                      sname=sname,
                      kzfkp_id=el.Signal_id,
                      num_VS=num_VS,
                      Zone=Zone)
        data.append(a_dict)
    base_write_many2(VS, data)



