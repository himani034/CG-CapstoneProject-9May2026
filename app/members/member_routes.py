from fastapi import APIRouter

from app.members.member_schema import MemberCreate

from app.members.member_service import (
    add_member_service,
    get_members_service
)

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.post("/")
def add_member(member: MemberCreate):

    return add_member_service(
        member.dict()
    )

@router.get("/")
def get_members():

    return get_members_service()