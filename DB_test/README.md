编码：uft-8
作者：dxj728
说明：本目录用于说明python下部分数据库操作使用


使用pythonDB API 2.0数据库操作基本流程：
    开始-->打开数据库连接-->获取游标-->执行SQL语句(获取数据，处理数据)-->关闭游标-->关闭数据库连接-->结束

DB API 2.0协议必须提供的3个全局变量
    apillevel: 显示数据库模块的API版本号，通常就是2.0，如果此变量不存在，代表暂时不支持DB API 2.0
    threadsafety: 指定数据库模块的线程安全等级，范围0~3, 3代表该模块完全线程安全，1代表部分线程安全，0代表线程完全不能共享该模块
    paramstyle: 指定该数据模块SQL语句的参数风格，返回值format(python标准化字符串代表参数)、pyformat(python中扩展的格式代码代表参数)、qmark(使用问号?代表参数)、numeric(使用数字化占位符代表参数)、named(使用命名占位符带代表参数)


数据库模块通常具有方法和属性：
    connect(): 该函数用于连接数据库，并返回数据库连接对象

数据库连接对象通常具有方法和属性：
    cursor(factory=Cursor): 打开游标
    commit(): 提交事务
    rollback(): 回滚事务
    close(): 关闭数据库连接
    isolation_level: 返回或设置数据库连接中事务的隔离级别
    in_transaction: 判断当前是否处于事务中

游标对象通常具有方法和属性：
    execute(sql, para): 执行SQL语句，para参数用于为SQL与剧中的参数指定值
    executemany(sql, seq_para): 重复执行SQL语句，通过seq_para序列为SQL语句中的参数指定值，该序列中有多少个元素，则SQL语句执行多少次
    executescript(script): 此方法非DB API 2.0支持方法，但该方法可以直接执行包含多条SQL语句的SQL脚本
    fetchone(): 获取查询结果集的下一行，如果没有下一行，返回None
    fetchmany(size=cursor.arraysize): 返回查询结果集的下N行组成的列表，如果没有更多的数据行，返回空列表
    fetchall(): 返回查询结果集的全部行组成的列表
    close(): 关闭游标
    rowcount: 该只读属性返回受SQL语句影响的行数，对于executemany()方法，该方法所修改的记录条数也可以通过该属性获取
    lastrowid: 该只读属性可获取最后修改行rowid
    arraysize: 用于设置或获取fetchmany()默认获取的记录条数，该属性默认为1，有些数据库模块无该属性
    description: 该只读属性可获取最后一次查询返回的所有列的信息
    connection: 该只读属性返回创建游标的数据库连接对象，有些数据库模块没有该属性

