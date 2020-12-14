import dbconfig

if __name__ == '__main__':
    mysql_controller = dbconfig.MysqlController('localhost', 'd0rk', 'root-pass', 'test')
    table_name = 'users'
    mysql_controller.insert_value(table_name, ['"test"', '"test123"'])
    mysql_controller.insert_value_with(table_name, ['id'], ['"THIS IS ID"'])
