from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/variables", tags=["Variables"])

@router.get("/", response_model=list[schemas.Variable])
def get_all_variables(db: Session = Depends(get_db)):
    return db.query(models.Variable).all()

@router.post("/", response_model=schemas.Variable)
def create_variable(var_data: schemas.VariableCreate, db: Session = Depends(get_db)):
    new_var = models.Variable(name=var_data.name, value=var_data.value)
    db.add(new_var)
    db.commit()
    db.refresh(new_var)
    return new_var

@router.get("/{variable_id}", response_model=schemas.Variable)
def get_variable(variable_id: int, db: Session = Depends(get_db)):
    variable = db.query(models.Variable).filter(models.Variable.id == variable_id).first()
    if not variable:
        raise HTTPException(status_code=404, detail="Variable not found")
    return variable

@router.put("/{variable_id}", response_model=schemas.Variable)
def update_variable(variable_id: int, var_data: schemas.VariableCreate, db: Session = Depends(get_db)):
    variable = db.query(models.Variable).filter(models.Variable.id == variable_id).first()
    if not variable:
        raise HTTPException(status_code=404, detail="Variable not found")
    variable.name = var_data.name
    variable.value = var_data.value
    db.commit()
    db.refresh(variable)
    return variable

@router.delete("/{variable_id}")
def delete_variable(variable_id: int, db: Session = Depends(get_db)):
    variable = db.query(models.Variable).filter(models.Variable.id == variable_id).first()
    if not variable:
        raise HTTPException(status_code=404, detail="Variable not found")
    db.delete(variable)
    db.commit()
    return {"detail": f"Variable with id {variable_id} deleted"}