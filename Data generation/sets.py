# categorical / numerical / option
class Manufacturing():
    cols = ['manu_coolent_temperature', 'manu_exhaust_temparature', 'manu_vibration', 'manu_preasure', 'manu_coolent_gasflow_rate', 'manu_airflow_gasflow_rate', 'manu_current']
    data = {
        'manu_coolent_temperature': ['int', 70, 100],
        'manu_exhaust_temparature': ['int', 200, 1000],

        'manu_vibration': ['float', 50, 500],

        'manu_preasure': ['int', 1, 10],

        'manu_coolent_gasflow_rate': ['int', 5, 50],
        'manu_airflow_gasflow_rate': ['int', 50, 500],

        'manu_current': ['int', 0, 500],
    }
    limit = 1000

# categorical / numerical / option
class Railway():
    cols = ['rail_temperature', 'rail_speed', 'rail_vibration']
    data = {
        'rail_temperature': ['int', -40, 125],

        'rail_speed': ['int', 60, 160],

        'rail_vibration': ['float', 0, 50],
    }
    limit = 1000

