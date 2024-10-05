"""create table

Revision ID: 460b61ca1573
Revises: 1d95ce54290b
Create Date: 2024-10-02 17:10:53.687980

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "460b61ca1573"
down_revision: Union[str, None] = "1d95ce54290b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
