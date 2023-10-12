run:
	uvicorn app.main:app --reload

# به صورت خودکار بر اساس مدل های ساخته شده در الچمی مدل های المبیک را میسازد
alembic_auto :
	alembic -- revison --autogenrate -m "this is auto genrate "

