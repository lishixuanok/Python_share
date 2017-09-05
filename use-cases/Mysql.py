from sqlalchemy import create_engine

# Documentation Refer
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

mysql_url = "your url"
engine = create_engine(mysql_url)


def select_execute(select_str):
    cur = engine.execute(select_str)
    rows = cur.fetchall()
    for row in rows:
        # TODO: add operation here
        print(row.mall_code_)


# Update/ Insert/ Delete
def execute(execute_str):
    engine.execute(execute_str)


if __name__ == '__main__':
    select_str = """SELECT DISTINCT mall_code_ FROM tb_member_copy"""
    select_execute(select_str)

    execute("""UPDATE tb_member_copy
               SET source_ = 'wechat'
               WHERE id_='6d5ad4865c7311e7a3db4ccc6aa75aa7'""")
