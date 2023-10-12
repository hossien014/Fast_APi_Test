from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session

from ..orm_db.database import get_db
from app.oauth2 import get_currnt_user
from app.orm_db.models_orm import user_db,post_db, vote_db
from app.orm_db.schemas import vote_input


router=APIRouter(prefix="/vote", tags=['Votes'] )

@router.post("/")
def vote( vote:vote_input , db : Session=Depends(get_db), current_user:user_db=Depends(get_currnt_user)) :
      

      # this should move in crud.py 
      # check if post exist
      raw_post_query=db.query(post_db).filter(post_db.id==vote.post_id)
      first=raw_post_query.first()
      if first==None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"There is no post with id of {vote.post_id}")
      raw_vote_query=db.query(vote_db)\
      .filter(vote_db.post_id==vote.post_id, vote_db.user_id==current_user.id)
      
      if vote.dir == 1:
            if raw_vote_query.first()==None:
                  new_vote = vote_db(user_id=current_user.id,post_id=vote.post_id)
                  db.add(new_vote)
                  db.commit()
                  return {"msg" :"vote Successfully added"}
            else:
                  raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail=f"{current_user.username} already voted to tihs post({raw_post_query.first().title})")
            
      else:
            # remove vote !! i dont fell to do that :}
            pass 
      
      return{"vote input":vote , "current_user":current_user.username , "post_in_db":raw_vote_query.first() }

