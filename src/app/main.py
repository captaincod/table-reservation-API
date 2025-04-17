from fastapi import FastAPI

from app.api import hello


app = FastAPI()

app.include_router(hello.router)

# class Table(BaseModel):
#     id: int
#     name: str
#     seats: int
#     location: str

# class Reservation(BaseModel):
#     id: int
#     customer_name: str
#     table_id: int
#     seats: int
#     location: str

"""Столики"""

@app.get("/tables") # список всех столиков
def tables_list():
    return []

@app.post("/tables") # создать новый столик
def new_table():
    pass

@app.delete("/tables/{id}") # удалить столик
def del_table():
    pass

"""Брони"""

@app.get("/reservations") # список всех броней
def reserv_list():
    return []

@app.post("/reservations") # создать новую бронь
def new_reserv():
    pass

@app.delete("/reservations/{id}") # удалить бронь
def del_reserv():
    pass