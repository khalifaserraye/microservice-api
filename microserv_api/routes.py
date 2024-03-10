from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from microserv_api import crud
from microserv_api import app, get_db

@app.get("/region")
async def get_regions(db: Session = Depends(get_db)):
    results = crud.get_regions(db)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No department found")
    return results

@app.get("/region/{region_id}")
async def get_region_by_id(region_id: int, db: Session = Depends(get_db)):
    results = crud.get_region_by_id(db, region_id=region_id)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No region found")
    return results

@app.get("/region/depts/{region_id}")
async def get_region_depts_by_id(region_id: int, db: Session = Depends(get_db)):
    results = crud.get_region_depts_by_id(db, region_id=region_id)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No region found")
    return results

@app.get("/department")
async def get_departments(db: Session = Depends(get_db)):
    results = crud.get_departments(db)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No department found")
    return results

@app.get("/department/{dept_id}")
async def get_department_by_id(dept_id: str, db: Session = Depends(get_db)):
    try:
        results = crud.get_department_by_id(db, dept_id=dept_id)
        if results is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No department found")
        return results
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@app.get("/department_by_ref/{dept_ref}")
async def get_department_by_ref(dept_ref: str, db: Session = Depends(get_db)):
    try:
        results = crud.get_department_by_ref(db, dept_ref=dept_ref)
        if results is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No department found with this reference")
        return results
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@app.get("/mun/code/{cp_value}")
async def get_municipality_by_code(cp_value: str, db: Session = Depends(get_db)):
    results = crud.get_municipality_by_code(db, cp_value=cp_value)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No municipality found")
    return results

# @app.get("/dept/{ref}")
# async def get_department_by_ref(ref: any, db: Session = Depends(get_db)):
#     results = crud.get_department_by_ref(db, ref=ref)
#     if results is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No dept found")
#     return results