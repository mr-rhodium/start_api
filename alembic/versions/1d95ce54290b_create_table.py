"""create table

Revision ID: 1d95ce54290b
Revises: d75d68c240f2
Create Date: 2024-10-02 17:08:32.150243

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d95ce54290b"
down_revision: Union[str, None] = "d75d68c240f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
