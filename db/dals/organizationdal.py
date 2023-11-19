import uuid

import sqlalchemy
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import Optional

from db.models.organizations import Organizations
from views.organization.schemas import ShowOrganization


class OrganizationDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_organization(
            self,
            owner_id: uuid.UUID, title: str,
            address: str, logo: str, inn: str,
            ogrn: str
    ) -> Organizations:
        try:
            new_organization = Organizations(
                owner_id=owner_id,
                title=title,
                address=address,
                logo=logo,
                inn=inn,
                ogrn=ogrn
            )

            self.db_session.add(new_organization)
            await self.db_session.flush()
            return new_organization
        except IntegrityError as err:
            raise HTTPException(status_code=409, detail='inn already exists')

    async def search_organization_by_inn(self, inn: str, title: str, lim: int, offset: int):
        if lim < 0 or offset < 0:
            return {'response: ': 'value cannot be negative'}

        if inn:
            query = select(
                Organizations.title,
                Organizations.inn,
                Organizations.address,
                Organizations.logo).where(Organizations.inn.like(f'%{inn}%')).limit(lim).offset(offset)

            res = await self.db_session.execute(query)
            organization_row = [r._asdict() for r in res.fetchall()]

        elif title:
            query = select(
                Organizations.title,
                Organizations.inn,
                Organizations.address,
                Organizations.logo).where(Organizations.title.like(f'%{title}%')).limit(lim).offset(offset)

            res = await self.db_session.execute(query)
            organization_row = [r._asdict() for r in res.fetchall()]

        if organization_row:
            return {'response: ': organization_row}

    async def show_organization(self, inn: str):
        query = select(Organizations).where(Organizations.inn == inn)
        res = await self.db_session.execute(query)
        org_row = res.fetchone()

        if org_row:
            return {'response: ': org_row[0]}

        raise HTTPException(status_code=404, detail='Not Found')

    async def delete_organization(self, inn: str, owner_id: uuid.UUID):
        stmt = delete(Organizations).where(Organizations.owner_id == owner_id, Organizations.inn == inn)

        await self.db_session.execute(stmt)
        await self.db_session.commit()

        return {'response: ': 'successful'}

    async def show_all_owners_organizations(self, lim: int, offset: int, owner_id: uuid.UUID):
        print(f'================                            {owner_id}')
        if not owner_id:
            raise HTTPException(status_code=401, detail='Unauthorized')

        query = select(Organizations).where(Organizations.owner_id == owner_id).limit(lim).offset(offset)
        res = await self.db_session.execute(query)
        organization_row = [r._asdict() for r in res.fetchall()]

        if organization_row:
            return {'response: ': organization_row}

        raise HTTPException(status_code=404, detail='Not found')


